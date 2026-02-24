"""
FinancialProof - Signal-Generierung
Automatische Kauf-/Verkaufssignale basierend auf technischen Indikatoren
"""
import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

from indicators.technical import TechnicalIndicators


class SignalType(str, Enum):
    """Signaltypen"""
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"


class SignalStrength(str, Enum):
    """Signalstärke"""
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"


@dataclass
class Signal:
    """Ein einzelnes Trading-Signal"""
    date: datetime
    signal_type: SignalType
    strength: SignalStrength
    indicator: str
    description: str
    price: float
    confidence: float = 0.0  # 0-1
    metadata: Dict = field(default_factory=dict)


class SignalGenerator:
    """Generiert Trading-Signale aus verschiedenen Indikatoren"""

    def __init__(self):
        self.signals: List[Signal] = []

    def generate_all_signals(self, df: pd.DataFrame) -> List[Signal]:
        """
        Generiert alle Signale für einen DataFrame.

        Args:
            df: DataFrame mit OHLCV und berechneten Indikatoren

        Returns:
            Liste von Signal-Objekten, sortiert nach Datum
        """
        self.signals = []

        # Stelle sicher, dass Indikatoren berechnet sind
        if 'sma_20' not in df.columns:
            df = TechnicalIndicators.calculate_all(df)

        # Verschiedene Signal-Quellen
        self._ma_crossover_signals(df)
        self._rsi_signals(df)
        self._bollinger_signals(df)
        self._macd_signals(df)
        self._price_action_signals(df)

        # Nach Datum sortieren
        self.signals.sort(key=lambda x: x.date, reverse=True)

        return self.signals

    def get_latest_signal(self, df: pd.DataFrame) -> Optional[Signal]:
        """Gibt das aktuellste Signal zurück"""
        signals = self.generate_all_signals(df)
        return signals[0] if signals else None

    def get_signal_summary(self, df: pd.DataFrame) -> Dict:
        """
        Erstellt eine Zusammenfassung aller aktuellen Signale.

        Returns:
            Dict mit 'overall_signal', 'buy_count', 'sell_count', 'signals'
        """
        signals = self.generate_all_signals(df)

        # Nur die neuesten Signale (letzte 5 Tage)
        recent_signals = [s for s in signals if s.date >= df.index[-5]]

        buy_count = sum(1 for s in recent_signals if s.signal_type == SignalType.BUY)
        sell_count = sum(1 for s in recent_signals if s.signal_type == SignalType.SELL)

        # Gesamtbewertung
        if buy_count > sell_count + 1:
            overall = SignalType.BUY
        elif sell_count > buy_count + 1:
            overall = SignalType.SELL
        else:
            overall = SignalType.HOLD

        # Gewichtete Konfidenz
        if recent_signals:
            avg_confidence = np.mean([s.confidence for s in recent_signals])
        else:
            avg_confidence = 0.5

        return {
            'overall_signal': overall,
            'overall_confidence': avg_confidence,
            'buy_count': buy_count,
            'sell_count': sell_count,
            'recent_signals': recent_signals[:10]  # Top 10
        }

    # ===== SIGNAL-GENERATOREN =====

    def _ma_crossover_signals(self, df: pd.DataFrame):
        """
        MA Crossover Signale:
        - Golden Cross (SMA20 kreuzt SMA50 nach oben) -> Kaufen
        - Death Cross (SMA20 kreuzt SMA50 nach unten) -> Verkaufen
        """
        if 'sma_20' not in df.columns or 'sma_50' not in df.columns:
            return

        sma_20 = df['sma_20']
        sma_50 = df['sma_50']

        # Golden Cross erkennen
        golden_cross = (sma_20 > sma_50) & (sma_20.shift(1) <= sma_50.shift(1))

        # Death Cross erkennen
        death_cross = (sma_20 < sma_50) & (sma_20.shift(1) >= sma_50.shift(1))

        for idx in df.index[golden_cross]:
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.BUY,
                strength=SignalStrength.STRONG,
                indicator="MA Crossover",
                description="Golden Cross: SMA20 kreuzte SMA50 nach oben",
                price=df.loc[idx, 'Close'],
                confidence=0.75,
                metadata={'sma_20': sma_20.loc[idx], 'sma_50': sma_50.loc[idx]}
            ))

        for idx in df.index[death_cross]:
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.SELL,
                strength=SignalStrength.STRONG,
                indicator="MA Crossover",
                description="Death Cross: SMA20 kreuzte SMA50 nach unten",
                price=df.loc[idx, 'Close'],
                confidence=0.75,
                metadata={'sma_20': sma_20.loc[idx], 'sma_50': sma_50.loc[idx]}
            ))

    def _rsi_signals(self, df: pd.DataFrame):
        """
        RSI Signale:
        - RSI < 30 (Überverkauft) -> Kaufen
        - RSI > 70 (Überkauft) -> Verkaufen
        - Divergenzen erkennen
        """
        if 'rsi' not in df.columns:
            return

        rsi = df['rsi']

        # Überverkauft -> Kaufsignal (wenn RSI von unter 30 wieder steigt)
        oversold_exit = (rsi > 30) & (rsi.shift(1) <= 30)

        # Überkauft -> Verkaufssignal (wenn RSI von über 70 wieder fällt)
        overbought_exit = (rsi < 70) & (rsi.shift(1) >= 70)

        for idx in df.index[oversold_exit]:
            strength = SignalStrength.STRONG if rsi.shift(1).loc[idx] < 25 else SignalStrength.MODERATE
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.BUY,
                strength=strength,
                indicator="RSI",
                description=f"RSI verlässt überverkaufte Zone (RSI war: {rsi.shift(1).loc[idx]:.1f})",
                price=df.loc[idx, 'Close'],
                confidence=0.7 if strength == SignalStrength.STRONG else 0.55,
                metadata={'rsi': rsi.loc[idx]}
            ))

        for idx in df.index[overbought_exit]:
            strength = SignalStrength.STRONG if rsi.shift(1).loc[idx] > 75 else SignalStrength.MODERATE
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.SELL,
                strength=strength,
                indicator="RSI",
                description=f"RSI verlässt überkaufte Zone (RSI war: {rsi.shift(1).loc[idx]:.1f})",
                price=df.loc[idx, 'Close'],
                confidence=0.7 if strength == SignalStrength.STRONG else 0.55,
                metadata={'rsi': rsi.loc[idx]}
            ))

    def _bollinger_signals(self, df: pd.DataFrame):
        """
        Bollinger Band Signale:
        - Kurs berührt unteres Band -> Kaufen
        - Kurs berührt oberes Band -> Verkaufen
        - Squeeze-Ausbrüche erkennen
        """
        if 'bb_lower' not in df.columns:
            return

        close = df['Close']
        bb_upper = df['bb_upper']
        bb_lower = df['bb_lower']
        bb_middle = df['bb_middle']

        # Kurs durchbricht unteres Band und kehrt zurück
        lower_touch = (close.shift(1) < bb_lower.shift(1)) & (close > bb_lower)

        # Kurs durchbricht oberes Band und kehrt zurück
        upper_touch = (close.shift(1) > bb_upper.shift(1)) & (close < bb_upper)

        for idx in df.index[lower_touch]:
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.BUY,
                strength=SignalStrength.MODERATE,
                indicator="Bollinger Bänder",
                description="Kurs erholt sich vom unteren Bollinger Band",
                price=df.loc[idx, 'Close'],
                confidence=0.6,
                metadata={'bb_lower': bb_lower.loc[idx], 'bb_upper': bb_upper.loc[idx]}
            ))

        for idx in df.index[upper_touch]:
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.SELL,
                strength=SignalStrength.MODERATE,
                indicator="Bollinger Bänder",
                description="Kurs prallt vom oberen Bollinger Band ab",
                price=df.loc[idx, 'Close'],
                confidence=0.6,
                metadata={'bb_lower': bb_lower.loc[idx], 'bb_upper': bb_upper.loc[idx]}
            ))

        # Bollinger Squeeze (enge Bänder -> Ausbruch erwartet)
        if 'bb_width' in df.columns:
            width = df['bb_width']
            avg_width = width.rolling(50).mean()

            # Squeeze erkannt wenn aktuelle Breite < 50% der durchschnittlichen Breite
            squeeze = width < avg_width * 0.5

            # Ausbruch nach Squeeze
            squeeze_breakout_up = squeeze.shift(1) & ~squeeze & (close > bb_middle)
            squeeze_breakout_down = squeeze.shift(1) & ~squeeze & (close < bb_middle)

            for idx in df.index[squeeze_breakout_up]:
                self.signals.append(Signal(
                    date=idx,
                    signal_type=SignalType.BUY,
                    strength=SignalStrength.STRONG,
                    indicator="Bollinger Squeeze",
                    description="Ausbruch nach oben nach Bollinger Squeeze",
                    price=df.loc[idx, 'Close'],
                    confidence=0.7
                ))

            for idx in df.index[squeeze_breakout_down]:
                self.signals.append(Signal(
                    date=idx,
                    signal_type=SignalType.SELL,
                    strength=SignalStrength.STRONG,
                    indicator="Bollinger Squeeze",
                    description="Ausbruch nach unten nach Bollinger Squeeze",
                    price=df.loc[idx, 'Close'],
                    confidence=0.7
                ))

    def _macd_signals(self, df: pd.DataFrame):
        """
        MACD Signale:
        - MACD kreuzt Signal-Linie nach oben -> Kaufen
        - MACD kreuzt Signal-Linie nach unten -> Verkaufen
        """
        if 'macd' not in df.columns or 'macd_signal' not in df.columns:
            return

        macd = df['macd']
        signal = df['macd_signal']
        histogram = df.get('macd_histogram', macd - signal)

        # Bullish Crossover
        bullish_cross = (macd > signal) & (macd.shift(1) <= signal.shift(1))

        # Bearish Crossover
        bearish_cross = (macd < signal) & (macd.shift(1) >= signal.shift(1))

        for idx in df.index[bullish_cross]:
            # Stärker wenn unter der Nulllinie (Trendwende)
            strength = SignalStrength.STRONG if macd.loc[idx] < 0 else SignalStrength.MODERATE

            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.BUY,
                strength=strength,
                indicator="MACD",
                description="MACD kreuzte Signal-Linie nach oben",
                price=df.loc[idx, 'Close'],
                confidence=0.65 if strength == SignalStrength.STRONG else 0.55,
                metadata={'macd': macd.loc[idx], 'signal': signal.loc[idx]}
            ))

        for idx in df.index[bearish_cross]:
            strength = SignalStrength.STRONG if macd.loc[idx] > 0 else SignalStrength.MODERATE

            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.SELL,
                strength=strength,
                indicator="MACD",
                description="MACD kreuzte Signal-Linie nach unten",
                price=df.loc[idx, 'Close'],
                confidence=0.65 if strength == SignalStrength.STRONG else 0.55,
                metadata={'macd': macd.loc[idx], 'signal': signal.loc[idx]}
            ))

    def _price_action_signals(self, df: pd.DataFrame):
        """
        Preis-Aktions-Signale:
        - Wichtige Kerzenmuster erkennen
        - Support/Resistance Durchbrüche
        """
        # Bullish Engulfing
        bullish_engulfing = (
            (df['Close'].shift(1) < df['Open'].shift(1)) &  # Vorherige Kerze war bearish
            (df['Close'] > df['Open']) &                    # Aktuelle Kerze ist bullish
            (df['Open'] <= df['Close'].shift(1)) &          # Open unter vorherigem Close
            (df['Close'] >= df['Open'].shift(1))            # Close über vorherigem Open
        )

        # Bearish Engulfing
        bearish_engulfing = (
            (df['Close'].shift(1) > df['Open'].shift(1)) &  # Vorherige Kerze war bullish
            (df['Close'] < df['Open']) &                    # Aktuelle Kerze ist bearish
            (df['Open'] >= df['Close'].shift(1)) &          # Open über vorherigem Close
            (df['Close'] <= df['Open'].shift(1))            # Close unter vorherigem Open
        )

        for idx in df.index[bullish_engulfing]:
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.BUY,
                strength=SignalStrength.MODERATE,
                indicator="Kerzenmuster",
                description="Bullish Engulfing Muster erkannt",
                price=df.loc[idx, 'Close'],
                confidence=0.55
            ))

        for idx in df.index[bearish_engulfing]:
            self.signals.append(Signal(
                date=idx,
                signal_type=SignalType.SELL,
                strength=SignalStrength.MODERATE,
                indicator="Kerzenmuster",
                description="Bearish Engulfing Muster erkannt",
                price=df.loc[idx, 'Close'],
                confidence=0.55
            ))


# ===== SIGNAL-FORMATTER =====

def format_signal_for_display(signal: Signal) -> Dict:
    """Formatiert ein Signal für die Anzeige in der UI"""
    emoji_map = {
        SignalType.BUY: "🟢",
        SignalType.SELL: "🔴",
        SignalType.HOLD: "🟡"
    }

    strength_map = {
        SignalStrength.STRONG: "Stark",
        SignalStrength.MODERATE: "Mittel",
        SignalStrength.WEAK: "Schwach"
    }

    return {
        'emoji': emoji_map.get(signal.signal_type, "⚪"),
        'type': "Kaufen" if signal.signal_type == SignalType.BUY else "Verkaufen" if signal.signal_type == SignalType.SELL else "Halten",
        'strength': strength_map.get(signal.strength, ""),
        'indicator': signal.indicator,
        'description': signal.description,
        'price': f"{signal.price:.2f}",
        'confidence': f"{signal.confidence * 100:.0f}%",
        'date': signal.date.strftime("%d.%m.%Y") if hasattr(signal.date, 'strftime') else str(signal.date)
    }
