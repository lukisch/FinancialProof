"""
Tests fuer Datenbank-Modul
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
import tempfile
import os
from unittest.mock import patch
from config import Config


@pytest.fixture
def temp_config():
    """Erstellt eine Config mit temporaerem Datenbankpfad"""
    with tempfile.TemporaryDirectory() as tmpdir:
        cfg = Config.__new__(Config)
        cfg.BASE_DIR = Path(tmpdir)
        cfg.DATA_DIR = Path(tmpdir) / "data"
        cfg.DB_PATH = cfg.DATA_DIR / "test.db"
        cfg.SECRETS_PATH = cfg.DATA_DIR / ".secrets"
        cfg.DATA_DIR.mkdir(exist_ok=True)
        yield cfg


@pytest.fixture
def temp_db(temp_config):
    """Erstellt eine temporaere DatabaseManager-Instanz"""
    with patch("core.database.config", temp_config):
        from core.database import DatabaseManager, WatchlistItem, Job, JobStatus
        db = DatabaseManager()
        yield db, WatchlistItem, Job, JobStatus


class TestWatchlist:
    def test_add_and_get(self, temp_db):
        db, WatchlistItem, _, _ = temp_db
        item = WatchlistItem(symbol="AAPL", name="Apple Inc.", asset_type="stock")
        db.add_to_watchlist(item)
        result = db.get_watchlist()
        assert len(result) == 1
        assert result[0].symbol == "AAPL"

    def test_remove(self, temp_db):
        db, WatchlistItem, _, _ = temp_db
        item = WatchlistItem(symbol="MSFT", name="Microsoft")
        db.add_to_watchlist(item)
        db.remove_from_watchlist("MSFT")
        assert len(db.get_watchlist()) == 0

    def test_is_in_watchlist(self, temp_db):
        db, WatchlistItem, _, _ = temp_db
        item = WatchlistItem(symbol="GOOG", name="Google")
        db.add_to_watchlist(item)
        assert db.is_in_watchlist("GOOG") is True
        assert db.is_in_watchlist("TSLA") is False

    def test_update_notes(self, temp_db):
        db, WatchlistItem, _, _ = temp_db
        item = WatchlistItem(symbol="AMZN", name="Amazon")
        db.add_to_watchlist(item)
        db.update_watchlist_notes("AMZN", "Gute Aktie")
        result = db.get_watchlist_item("AMZN")
        assert result.notes == "Gute Aktie"


class TestJobs:
    def test_create_and_get_job(self, temp_db):
        db, _, Job, JobStatus = temp_db
        job = Job(symbol="AAPL", analysis_type="arima", status=JobStatus.PENDING)
        job_id = db.create_job(job)
        assert job_id > 0
        result = db.get_job(job_id)
        assert result.symbol == "AAPL"
        assert result.analysis_type == "arima"

    def test_update_job_status(self, temp_db):
        db, _, Job, JobStatus = temp_db
        job = Job(symbol="MSFT", analysis_type="monte_carlo", status=JobStatus.PENDING)
        job_id = db.create_job(job)
        db.update_job_status(job_id, JobStatus.COMPLETED, progress=100)
        result = db.get_job(job_id)
        assert result.status == JobStatus.COMPLETED
        assert result.progress == 100

    def test_delete_job(self, temp_db):
        db, _, Job, JobStatus = temp_db
        job = Job(symbol="TSLA", analysis_type="sentiment", status=JobStatus.PENDING)
        job_id = db.create_job(job)
        db.delete_job(job_id)
        assert db.get_job(job_id) is None

    def test_get_job_counts(self, temp_db):
        db, _, Job, JobStatus = temp_db
        db.create_job(Job(symbol="A", analysis_type="t1", status=JobStatus.PENDING))
        db.create_job(Job(symbol="B", analysis_type="t2", status=JobStatus.PENDING))
        counts = db.get_job_counts()
        assert counts.get("pending", 0) == 2
