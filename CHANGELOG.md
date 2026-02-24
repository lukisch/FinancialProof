# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [Unreleased]

### Geplant
- Trading-Anbindung (Alpaca, CCXT)
- Strategy Engine mit Regelwerk
- Automatisiertes Trading
- Backtesting-Engine
- Multi-User Support

---

## [1.0.0] - 2026-01-20

### Hinzugefügt

#### Core
- Streamlit-basierte Web-Anwendung
- SQLite-Datenbank für Persistenz
- yfinance-Integration für Marktdaten
- Caching-System für API-Anfragen

#### Technische Indikatoren
- Simple Moving Average (SMA) - 20, 50, 200 Perioden
- Exponential Moving Average (EMA) - 12, 26 Perioden
- Relative Strength Index (RSI) - 14 Perioden
- Bollinger Bands - 20 Perioden, 2 Standardabweichungen
- MACD - 12/26/9 Konfiguration
- Stochastic Oscillator - 14/3/3 Konfiguration
- Average True Range (ATR) - 14 Perioden

#### Signal-Generierung
- Golden Cross / Death Cross (SMA 50/200)
- RSI Überkauft/Überverkauft Signale
- Bollinger Band Breakouts
- MACD Signal-Kreuzungen
- Candlestick-Muster (Hammer, Engulfing, Doji)

#### Analyse-Module
- **ARIMA**: Zeitreihen-Prognose mit statsmodels
- **Monte Carlo**: Value at Risk Simulation
- **Mean Reversion**: Rückkehr-zum-Mittelwert Analyse
- **Random Forest**: ML-basierte Trendvorhersage
- **Neural Network**: Deep Learning Pattern Recognition
- **Sentiment**: News-Stimmungsanalyse mit NLP
- **Research Agent**: Web-Recherche Agent

#### Job-System
- Asynchrone Job-Ausführung
- Job-Queue mit Status-Tracking (pending, running, completed, failed)
- SQLite-Persistenz für Jobs und Ergebnisse
- Automatische Methodenauswahl basierend auf Marktbedingungen

#### Benutzeroberfläche
- Responsive Sidebar mit Watchlist
- Interaktive Candlestick-Charts (Plotly)
- Indikator-Overlays
- Tab-basierte Navigation (Chart, Analyse, Jobs)
- Deutsche Benutzeroberfläche

### Technische Details
- Python 3.9+ Kompatibilität
- Modulare Architektur mit Registry-Pattern
- Abstrakte Basisklassen für Erweiterbarkeit
- Error Handling mit Fallback-Mechanismen

---

## Versionshistorie

| Version | Datum | Beschreibung |
|---------|-------|--------------|
| 1.0.0 | 2026-01-20 | Initiale Release mit allen Basis-Features |

---

## Upgrade-Hinweise

### Von 0.x auf 1.0.0
Dies ist die erste stabile Version. Keine Migration erforderlich.

### Zukünftige Upgrades
Bei Datenbank-Schema-Änderungen wird ein Migrations-Skript bereitgestellt.

---

## Links

- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- [GitHub Issues](https://github.com/username/FinancialProof/issues)
