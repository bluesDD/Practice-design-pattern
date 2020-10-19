import sqlalchemy
from sqlalchemy import orm

import pytest
from models import Base, User, Address


SESSION = orm.scoped_session(orm.sessionmaker())
BOUND = False


def pytest_addoption(paraser):
    paraser.addoption("--small_only", action="store_true")

def pytest_configure(config):
    config.addinivalue_line("makers", "small: Small test")

def pytest_runtest_setup(item):
    small_only = item.config.getoption("small_only")
    if not small_only:
        global SESSION, BOUND
        if not BOUND:
            engine = sqlalchemy.create_engine("sqlite://")

