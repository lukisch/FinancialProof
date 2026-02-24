"""
FinancialProof - Core Module
"""
from core.database import db, DatabaseManager
from core.data_provider import DataProvider

__all__ = ['db', 'DatabaseManager', 'DataProvider']
