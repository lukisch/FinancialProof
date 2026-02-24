"""
FinancialProof - Konfigurationsmodul
Zentrale Konfiguration für Pfade, API-Keys und App-Einstellungen
"""
import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
from cryptography.fernet import Fernet
import json


@dataclass
class Config:
    """Zentrale Konfigurationsklasse"""

    # Pfade
    BASE_DIR: Path = field(default_factory=lambda: Path(__file__).parent)
    DATA_DIR: Path = field(init=False)
    DB_PATH: Path = field(init=False)
    SECRETS_PATH: Path = field(init=False)

    # App Settings
    APP_NAME: str = "FinancialProof"
    APP_VERSION: str = "1.0.0"
    DEFAULT_TICKER: str = "AAPL"
    DEFAULT_PERIOD: str = "1y"

    # Chart Settings
    CHART_THEME: str = "plotly_dark"
    CHART_HEIGHT: int = 600

    # Cache Settings (in Sekunden)
    CACHE_TTL_MARKET_DATA: int = 3600      # 1 Stunde
    CACHE_TTL_TICKER_INFO: int = 86400     # 1 Tag
    CACHE_TTL_NEWS: int = 1800             # 30 Minuten

    # Analyse-Einstellungen
    DEFAULT_SMA_PERIODS: list = field(default_factory=lambda: [20, 50, 200])
    DEFAULT_RSI_PERIOD: int = 14
    DEFAULT_BOLLINGER_PERIOD: int = 20
    DEFAULT_BOLLINGER_STD: float = 2.0

    def __post_init__(self):
        self.DATA_DIR = self.BASE_DIR / "data"
        self.DB_PATH = self.DATA_DIR / "financial.db"
        self.SECRETS_PATH = self.DATA_DIR / ".secrets"
        self._ensure_directories()

    def _ensure_directories(self):
        """Erstellt notwendige Verzeichnisse"""
        self.DATA_DIR.mkdir(exist_ok=True)


class APIKeyManager:
    """Verwaltet API-Keys mit Verschlüsselung"""

    def __init__(self, config: Config):
        self.config = config
        self._key_file = config.DATA_DIR / ".key"
        self._secrets_file = config.SECRETS_PATH
        self._fernet: Optional[Fernet] = None
        self._init_encryption()

    def _init_encryption(self):
        """Initialisiert oder lädt den Verschlüsselungsschlüssel"""
        if self._key_file.exists():
            with open(self._key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self._key_file, "wb") as f:
                f.write(key)
        self._fernet = Fernet(key)

    def save_api_key(self, service: str, api_key: str):
        """Speichert einen API-Key verschlüsselt"""
        secrets = self._load_secrets()
        encrypted = self._fernet.encrypt(api_key.encode()).decode()
        secrets[service] = encrypted
        self._save_secrets(secrets)

    def get_api_key(self, service: str) -> Optional[str]:
        """Lädt einen API-Key"""
        secrets = self._load_secrets()
        if service in secrets:
            try:
                decrypted = self._fernet.decrypt(secrets[service].encode()).decode()
                return decrypted
            except Exception:
                return None
        return None

    def has_api_key(self, service: str) -> bool:
        """Prüft ob ein API-Key existiert"""
        return self.get_api_key(service) is not None

    def delete_api_key(self, service: str):
        """Löscht einen API-Key"""
        secrets = self._load_secrets()
        if service in secrets:
            del secrets[service]
            self._save_secrets(secrets)

    def _load_secrets(self) -> dict:
        """Lädt die Secrets-Datei"""
        if self._secrets_file.exists():
            with open(self._secrets_file, "r") as f:
                return json.load(f)
        return {}

    def _save_secrets(self, secrets: dict):
        """Speichert die Secrets-Datei"""
        with open(self._secrets_file, "w") as f:
            json.dump(secrets, f)


# Globale Instanz
config = Config()
api_keys = APIKeyManager(config)


# ===== UI-Texte (Deutsch) =====
class UIText:
    """Deutsche Beschriftungen für die Benutzeroberfläche"""

    # Allgemein
    APP_TITLE = "FinancialProof - Finanz-Analyst"

    # Sidebar
    SIDEBAR_TITLE = "Markt-Auswahl"
    SIDEBAR_SYMBOL = "Symbol eingeben"
    SIDEBAR_PERIOD = "Zeitraum"
    SIDEBAR_INDICATORS = "Technische Indikatoren"
    SIDEBAR_WATCHLIST = "Watchlist"
    SIDEBAR_SETTINGS = "Einstellungen"
    SIDEBAR_ADD_ASSET = "Asset hinzufügen"

    # Zeiträume
    PERIODS = {
        "1mo": "1 Monat",
        "3mo": "3 Monate",
        "6mo": "6 Monate",
        "1y": "1 Jahr",
        "2y": "2 Jahre",
        "5y": "5 Jahre",
        "max": "Maximum"
    }

    # Tabs
    TAB_CHART = "Chart & Technik"
    TAB_ANALYSIS = "Tiefen-Analyse"
    TAB_JOBS = "Aufträge"

    # Indikatoren
    IND_SMA = "Gleitender Durchschnitt (SMA)"
    IND_EMA = "Exponentieller MA (EMA)"
    IND_RSI = "Relative Stärke Index (RSI)"
    IND_BOLLINGER = "Bollinger Bänder"
    IND_MACD = "MACD"
    IND_STOCHASTIC = "Stochastic Oscillator"

    # Analysen
    ANALYSIS_ARIMA = "Zeitreihenanalyse (ARIMA)"
    ANALYSIS_MEAN_REV = "Mean Reversion Prüfung"
    ANALYSIS_MONTE_CARLO = "Monte-Carlo-Simulation"
    ANALYSIS_CORRELATION = "Korrelation & Kointegration"
    ANALYSIS_DEEP_LEARNING = "Deep Learning / Pattern"
    ANALYSIS_RL = "Reinforcement Learning"
    ANALYSIS_SENTIMENT = "Sentiment & Recherche"

    # Job-Status
    JOB_PENDING = "Wartend"
    JOB_RUNNING = "Läuft"
    JOB_COMPLETED = "Abgeschlossen"
    JOB_FAILED = "Fehlgeschlagen"

    # Signale
    SIGNAL_BUY = "Kaufsignal"
    SIGNAL_SELL = "Verkaufssignal"
    SIGNAL_HOLD = "Halten"

    # Meldungen
    MSG_NO_DATA = "Keine Daten gefunden. Bitte Symbol prüfen."
    MSG_LOADING = "Daten werden geladen..."
    MSG_JOB_STARTED = "Analyse-Auftrag wurde gestartet"
    MSG_JOB_COMPLETED = "Analyse abgeschlossen"

    # API-Keys
    API_KEYS_TITLE = "API-Keys einrichten"
    API_TWITTER = "Twitter/X Bearer Token"
    API_YOUTUBE = "YouTube API Key"
    API_SAVE = "Speichern"
    API_LATER = "Später"


# Singleton für einfachen Import
texts = UIText()
