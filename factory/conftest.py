import sqlalchemy
from sqlalchemy import orm

import pytest
from models import Base, User, Address


SESSION = orm.scoped_session(orm.sessionmaker())
BOUND = False


def pytest_addoption(paraser):
    paraser.addoption("--small_only", action="store_true")
