from pyramid.authorization import Allow, Everyone

from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import register

# 🔹 Session global yang "scoped" per thread/request
DBSession = scoped_session(sessionmaker())
register(DBSession)

# 🔹 Base class untuk semua model
Base = declarative_base()


class Page(Base):
    __tablename__ = 'wikipages'
    uid = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    body = Column(Text)


class Root:
    # 🔹 ACL cuma dipakai kalau nanti pakai auth/permission
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, 'group:editors', 'edit'),
    ]

    def __init__(self, request):
        pass
