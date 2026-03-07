# FinancialProof

Eine browserbasierte Finanz-Analyse Web-App mit KI-gestuetzten Tiefenanalysen.

## Features

- **Technische Indikatoren**: SMA, EMA, RSI, Bollinger Bands, MACD, Stochastic, ATR
- **Automatische Signale**: Kauf-/Verkaufssignale basierend auf technischen Mustern
- **KI-Analysen**:
  - ARIMA Zeitreihenprognose
  - Monte Carlo Simulation (VaR)
  - Mean Reversion Analyse
  - Random Forest Trendvorhersage
  - Neural Network Pattern Recognition
  - Sentiment-Analyse (News)
  - Web Research Agent
- **Job-Queue System**: Asynchrone Analyse-Auftraege mit SQLite-Persistenz
- **Watchlist**: Portfolio-Uebersicht mit mehreren Assets
- **Deutsche Benutzeroberflaeche**

## Screenshots

```
┌──────────────────────────────────────────────────────────────────┐
│  📊 Chart    │  🧠 Tiefen-Analyse    │  📋 Auftraege            │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Candlestick Chart mit Indikatoren]                             │
│                                                                  │
│  ────────────────────────────────────────────────────────────  │
│  RSI: 45.2  │  Signal: NEUTRAL  │  Trend: Seitwaerts           │
└──────────────────────────────────────────────────────────────────┘
```

## Installation

### Voraussetzungen

- Python 3.9+
- pip

### Setup

1. **Repository klonen**
   ```bash
   git clone https://github.com/lukisch/FinancialProof.git
   cd FinancialProof
   ```

2. **Virtuelle Umgebung erstellen** (empfohlen)
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Dependencies installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen konfigurieren** (optional)
   ```bash
   cp .env.example .env
   # .env Datei bearbeiten und API-Keys eintragen
   ```

5. **App starten**
   ```bash
   streamlit run app.py
   ```

6. **Browser oeffnen**
   ```
   http://localhost:8501
   ```

## Projektstruktur

```
FinancialProof/
├── app.py                   # Hauptanwendung
├── config.py                # Konfiguration
├── requirements.txt         # Dependencies
│
├── core/
│   ├── database.py          # SQLite Datenbank
│   └── data_provider.py     # yfinance Wrapper
│
├── indicators/
│   ├── technical.py         # Technische Indikatoren
│   └── signals.py           # Signal-Generierung
│
├── analysis/
│   ├── base.py              # Abstrakte Basisklasse
│   ├── registry.py          # Analyse-Registry
│   ├── statistical/         # ARIMA, Monte Carlo, Mean Reversion
│   ├── ml/                  # Random Forest, Neural Network
│   └── nlp/                 # Sentiment, Research Agent
│
├── jobs/
│   ├── manager.py           # Job-Verwaltung
│   └── executor.py          # Job-Ausfuehrung
│
├── ui/
│   ├── sidebar.py           # Sidebar-Komponente
│   ├── chart_view.py        # Chart-Ansicht
│   ├── analysis_view.py     # Analyse-Tab
│   └── job_queue.py         # Job-Queue-Ansicht
│
└── data/
    └── financial.db         # SQLite Datenbank
```

## Verwendung

### Symbol eingeben

Gib ein Ticker-Symbol in der Sidebar ein:
- Aktien: `AAPL`, `MSFT`, `GOOGL`
- ETFs: `SPY`, `QQQ`, `VOO`
- Krypto: `BTC-USD`, `ETH-USD`
- Indizes: `^GSPC`, `^DJI`

### Analyse starten

1. Waehle einen Zeitraum (1M - 5J)
2. Aktiviere gewuenschte Indikatoren
3. Wechsle zum Tab "Tiefen-Analyse"
4. Waehle eine Analysemethode und starte den Auftrag

### Ergebnisse ansehen

- Tab "Auftraege" zeigt alle laufenden und abgeschlossenen Jobs
- Klicke auf einen Job fuer Details und Empfehlungen

## Konfiguration

### Umgebungsvariablen

| Variable | Beschreibung | Standard |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API Key fuer Research Agent | - |
| `TWITTER_BEARER_TOKEN` | Twitter API fuer Sentiment | - |
| `YOUTUBE_API_KEY` | YouTube API fuer Video-Analyse | - |

### Einstellungen in `config.py`

```python
DEFAULT_TICKER = "AAPL"      # Standard-Symbol
CACHE_TTL_MARKET_DATA = 3600 # Cache-Dauer (Sekunden)
```

## Analyse-Module

| Modul | Kategorie | Beschreibung |
|-------|-----------|-------------|
| ARIMA | Statistik | Zeitreihen-Prognose |
| Monte Carlo | Statistik | Value at Risk Simulation |
| Mean Reversion | Statistik | Rueckkehr-zum-Mittelwert Analyse |
| Random Forest | ML | Trend-Klassifikation |
| Neural Network | ML | Muster-Erkennung |
| Sentiment | NLP | News-Stimmungsanalyse |
| Research Agent | NLP | Web-Recherche |

## Technologie-Stack

- **Frontend**: Streamlit
- **Charts**: Plotly
- **Daten**: yfinance, pandas, numpy
- **ML**: scikit-learn, TensorFlow (optional)
- **NLP**: transformers, TextBlob
- **Datenbank**: SQLite

## Roadmap

Siehe [ROADMAP.md](ROADMAP.md) fuer geplante Features:

- [ ] Phase 7: Trading-Anbindung (Alpaca, CCXT)
- [ ] Phase 8: Strategy Engine
- [ ] Phase 9: Automatisiertes Trading
- [ ] Phase 10: Erweiterte Analysen
- [ ] Phase 11: Performance & Skalierung
- [ ] Phase 12: Backtesting & Reporting

## Mitwirken

Beitraege sind willkommen! Siehe [CONTRIBUTING.md](CONTRIBUTING.md) fuer Details.

## Lizenz

GPL v3 - Siehe [LICENSE](LICENSE)

## Haftungsausschluss

**Dieses Tool dient nur zu Informationszwecken und stellt keine Anlageberatung dar.**

Die bereitgestellten Analysen und Signale sind keine Empfehlung zum Kauf oder Verkauf von Wertpapieren. Investitionen in Finanzmaerkte sind mit Risiken verbunden. Vergangene Performance ist kein Indikator fuer zukuenftige Ergebnisse.

## Changelog

Siehe [CHANGELOG.md](CHANGELOG.md) fuer alle Aenderungen.

---

🇬🇧 [English version](README.md)
