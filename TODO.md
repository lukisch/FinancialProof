# TODO - FinancialProof

Aufgabenliste im [TODO.md Format](https://github.com/todomd/todo.md) - kompatibel mit Kanban-Visualisierung.

---

## Backlog

### Phase 7: Trading-Anbindung
- [ ] Alpaca Paper Trading Integration ~5d #feature @dev
- [ ] TradingBot Klasse implementieren ~2d #core
- [ ] Broker-Abstraktionsschicht ~2d #architecture
- [ ] CCXT Integration für Krypto ~3d #feature
- [ ] Trading-Dashboard UI ~2d #ui
- [ ] Konto-Übersicht Komponente ~1d #ui
- [ ] Order-Formular mit Validierung ~1d #ui
- [ ] Sicherheitsmaßnahmen implementieren ~2d #security
  - [ ] Paper Trading als Standard
  - [ ] Bestätigungs-Dialog vor echten Trades
  - [ ] Maximale Order-Größe konfigurierbar
  - [ ] Tägliches Trading-Limit

### Phase 8: Strategy Engine
- [ ] Datenbank-Schema für Strategien erweitern ~1d #database
- [ ] StrategyEngine Klasse ~2d #core
- [ ] StrategyManager CRUD ~1d #core
- [ ] Regel-JSON Parser ~1d #core
- [ ] Strategie-Konfigurator UI ~2d #ui
- [ ] Asset-Typ spezifische Regeln ~1d #feature

### Phase 9: Automatisiertes Trading
- [ ] Auto-Trade Workflow implementieren ~3d #feature
- [ ] Automatisierungs-Level System ~1d #feature
- [ ] Kill Switch für Notfälle ~1d #security
- [ ] Benachrichtigungen (Email/Telegram) ~2d #feature
- [ ] Zeitfenster-Konfiguration ~1d #feature

### Phase 10: Erweiterte Analysen
- [ ] Korrelationsmatrix für Watchlist ~2d #analysis
- [ ] Kointegration für Pairs Trading ~2d #analysis
- [ ] Reinforcement Learning Agent ~5d #ml
- [ ] Twitter/X Sentiment Integration ~2d #nlp
- [ ] Reddit Sentiment (PRAW) ~2d #nlp
- [ ] YouTube Video-Analyse ~2d #nlp

### Phase 11: Performance & Skalierung
- [ ] Redis Cache Integration ~2d #performance
- [ ] Inkrementelle Daten-Updates ~2d #performance
- [ ] Benutzer-Authentifizierung ~3d #feature
- [ ] Multi-User Support ~3d #feature
- [ ] Docker Container ~1d #devops
- [ ] Streamlit Cloud Deployment ~1d #devops

### Phase 12: Backtesting & Reporting
- [ ] Backtesting Engine ~5d #feature
- [ ] Performance-Metriken (Sharpe, Drawdown) ~2d #analysis
- [ ] Trade-Protokoll Export (CSV/PDF) ~1d #feature
- [ ] Täglicher Performance-Report ~2d #feature
- [ ] Steuer-Übersicht ~2d #feature

---

## In Progress

- [ ] App testen und Bugs fixen #testing

---

## Review

_Keine Aufgaben in Review_

---

## Done ✓

### v1.0.0 - Basis-Features
- [x] Streamlit Web-App Grundgerüst #core
- [x] SQLite Datenbank Setup #database
- [x] yfinance Integration #data
- [x] Technische Indikatoren (SMA, EMA, RSI, BB, MACD) #indicators
- [x] Signal-Generierung #indicators
- [x] ARIMA Analyse-Modul #analysis
- [x] Monte Carlo Simulation #analysis
- [x] Mean Reversion Analyse #analysis
- [x] Random Forest Trendvorhersage #ml
- [x] Neural Network Pattern Recognition #ml
- [x] Sentiment-Analyse (News) #nlp
- [x] Research Agent #nlp
- [x] Job-Queue System #core
- [x] Automatische Methodenauswahl #core
- [x] Sidebar mit Watchlist #ui
- [x] Chart-View mit Overlays #ui
- [x] Analyse-Tab #ui
- [x] Job-Queue-Ansicht #ui
- [x] Deutsche Benutzeroberfläche #ui

### Dokumentation
- [x] README.md erstellen #docs
- [x] CHANGELOG.md erstellen #docs
- [x] CONTRIBUTING.md erstellen #docs
- [x] ROADMAP.md erstellen #docs
- [x] LICENSE hinzufügen #docs
- [x] .gitignore konfigurieren #devops
- [x] .env.example erstellen #devops

---

## Technische Schulden

- [ ] Unit Tests für alle Module schreiben ~5d #testing
- [ ] Error Handling verbessern ~2d #quality
- [ ] Logging-System einführen ~1d #quality
- [ ] API Rate Limiting implementieren ~1d #quality
- [ ] Docstrings vervollständigen ~2d #docs
- [ ] Type Hints überall hinzufügen ~2d #quality

---

## Bugs

_Keine bekannten Bugs_

---

## Legende

**Tags:**
- `#feature` - Neue Funktionalität
- `#core` - Kern-Komponente
- `#ui` - Benutzeroberfläche
- `#analysis` - Analyse-Modul
- `#ml` - Machine Learning
- `#nlp` - Natural Language Processing
- `#database` - Datenbank
- `#security` - Sicherheit
- `#performance` - Performance
- `#devops` - DevOps/Deployment
- `#testing` - Tests
- `#quality` - Code-Qualität
- `#docs` - Dokumentation

**Zeitschätzungen:**
- `~1d` - 1 Tag
- `~2d` - 2 Tage
- `~3d` - 3 Tage
- `~5d` - 5 Tage (1 Woche)
