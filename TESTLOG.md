# TESTLOG - FinancialProof

Dokumentation angeforderter Tests, Testergebnisse und Testabdeckung.

---

## Angeforderte Tests

### TEST-001: Basis-Funktionalität
**Angefordert:** 2026-01-20
**Priorität:** Hoch
**Status:** Ausstehend

**Testbereich:** Core-Funktionen
**Beschreibung:** Grundlegende App-Funktionalität testen

**Testfälle:**
- [ ] App startet ohne Fehler (`streamlit run app.py`)
- [ ] Sidebar rendert korrekt
- [ ] Symbol-Eingabe funktioniert (AAPL, MSFT, BTC-USD)
- [ ] Daten werden geladen und angezeigt
- [ ] Chart wird gerendert
- [ ] Tabs wechseln funktioniert

**Zugewiesen:** -
**Issue:** -

---

### TEST-002: Technische Indikatoren
**Angefordert:** 2026-01-20
**Priorität:** Hoch
**Status:** Ausstehend

**Testbereich:** Indicators
**Beschreibung:** Alle technischen Indikatoren validieren

**Testfälle:**
- [ ] SMA(20) Berechnung korrekt
- [ ] SMA(50) Berechnung korrekt
- [ ] SMA(200) Berechnung korrekt
- [ ] EMA(12) Berechnung korrekt
- [ ] EMA(26) Berechnung korrekt
- [ ] RSI(14) im Bereich 0-100
- [ ] Bollinger Bands (Upper > Mid > Lower)
- [ ] MACD Histogram korrekt
- [ ] Stochastic %K und %D im Bereich 0-100

**Zugewiesen:** -
**Issue:** -

---

### TEST-003: Signal-Generierung
**Angefordert:** 2026-01-20
**Priorität:** Mittel
**Status:** Ausstehend

**Testbereich:** Signals
**Beschreibung:** Kauf-/Verkaufssignale testen

**Testfälle:**
- [ ] Golden Cross wird erkannt (SMA50 kreuzt SMA200 nach oben)
- [ ] Death Cross wird erkannt (SMA50 kreuzt SMA200 nach unten)
- [ ] RSI Überkauft-Signal bei RSI > 70
- [ ] RSI Überverkauft-Signal bei RSI < 30
- [ ] Bollinger Breakout oben erkannt
- [ ] Bollinger Breakout unten erkannt
- [ ] MACD Crossover erkannt

**Zugewiesen:** -
**Issue:** -

---

### TEST-004: Analyse-Module
**Angefordert:** 2026-01-20
**Priorität:** Hoch
**Status:** Ausstehend

**Testbereich:** Analysis
**Beschreibung:** Alle KI-Analyse-Module testen

**Testfälle:**
- [ ] ARIMA läuft ohne Fehler
- [ ] ARIMA liefert Prognose mit Konfidenz
- [ ] Monte Carlo Simulation läuft
- [ ] Monte Carlo liefert VaR-Werte
- [ ] Mean Reversion Analyse funktioniert
- [ ] Random Forest Training erfolgreich
- [ ] Random Forest Prediction funktioniert
- [ ] Neural Network (falls TensorFlow installiert)
- [ ] Sentiment-Analyse mit News
- [ ] Research Agent (falls API-Key)

**Zugewiesen:** -
**Issue:** -

---

### TEST-005: Job-Queue System
**Angefordert:** 2026-01-20
**Priorität:** Hoch
**Status:** Ausstehend

**Testbereich:** Jobs
**Beschreibung:** Job-Verwaltung und Persistenz testen

**Testfälle:**
- [ ] Job erstellen funktioniert
- [ ] Job erscheint in Queue mit Status "pending"
- [ ] Job-Ausführung setzt Status auf "running"
- [ ] Erfolgreicher Job hat Status "completed"
- [ ] Fehlerhafter Job hat Status "failed"
- [ ] Ergebnisse werden in DB gespeichert
- [ ] Jobs überleben App-Neustart
- [ ] Job-Queue Ansicht zeigt alle Jobs

**Zugewiesen:** -
**Issue:** -

---

### TEST-006: Datenbank
**Angefordert:** 2026-01-20
**Priorität:** Mittel
**Status:** Ausstehend

**Testbereich:** Database
**Beschreibung:** SQLite-Datenbank Operationen testen

**Testfälle:**
- [ ] DB wird automatisch erstellt
- [ ] Watchlist hinzufügen funktioniert
- [ ] Watchlist abrufen funktioniert
- [ ] Job erstellen funktioniert
- [ ] Job aktualisieren funktioniert
- [ ] Ergebnis speichern funktioniert
- [ ] Ergebnis abrufen funktioniert

**Zugewiesen:** -
**Issue:** -

---

## In Durchführung

_Aktuell keine Tests in Durchführung_

---

## Abgeschlossene Tests

_Noch keine Tests abgeschlossen_

<!--
### TEST-XXX: Beispiel abgeschlossener Test
**Durchgeführt:** 2026-01-20
**Tester:** @username
**Status:** Bestanden | Fehlgeschlagen | Teilweise bestanden

**Ergebnisse:**
| Testfall | Ergebnis | Notizen |
|----------|----------|---------|
| Testfall 1 | ✅ Bestanden | - |
| Testfall 2 | ❌ Fehlgeschlagen | Bug-001 erstellt |
| Testfall 3 | ⚠️ Übersprungen | Abhängigkeit fehlt |

**Zusammenfassung:**
- Bestanden: 8/10
- Fehlgeschlagen: 1/10
- Übersprungen: 1/10

**Bugs gefunden:** BUG-001, BUG-002
**Commit:** abc1234
-->

---

## Testabdeckung

| Modul | Abdeckung | Status |
|-------|-----------|--------|
| core/ | 0% | Ausstehend |
| indicators/ | 0% | Ausstehend |
| analysis/ | 0% | Ausstehend |
| jobs/ | 0% | Ausstehend |
| ui/ | 0% | Ausstehend |

**Gesamtabdeckung:** 0%
**Ziel:** 80%

---

## Test-Kategorien

| Kategorie | Beschreibung |
|-----------|--------------|
| **Unit** | Einzelne Funktionen/Klassen isoliert |
| **Integration** | Zusammenspiel mehrerer Komponenten |
| **E2E** | Kompletter Workflow von UI bis DB |
| **Regression** | Nach Bug-Fix, um Rückfall zu verhindern |
| **Performance** | Ladezeiten, Speicherverbrauch |

---

## Test ausführen

```bash
# Alle Tests
pytest

# Mit Coverage
pytest --cov=. --cov-report=html

# Einzelnes Modul
pytest tests/test_indicators.py

# Nur markierte Tests
pytest -m "slow"
```

---

## Neuen Test anfordern

1. Erstelle ein [GitHub Issue](../../issues/new?template=testlog.md)
2. Verwende das Test-Request Template
3. Beschreibe den Testbereich und erwartete Testfälle

---

*Letzte Aktualisierung: 2026-01-20*
