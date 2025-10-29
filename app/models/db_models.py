import reflex as rx
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    Enum,
    Table,
    Boolean,
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
import enum

Base = declarative_base()


class UserStatus(enum.Enum):
    active = "active"
    paused = "paused"
    breathing = "breathing"


class ConnectionState(enum.Enum):
    engaged = "engaged"
    active_72h = "active_72h"
    paused = "paused"
    dormant = "dormant"


mutual_connections_table = Table(
    "mutual_connections",
    Base.metadata,
    Column("connection_id", Integer, ForeignKey("connections.id"), primary_key=True),
    Column("mutual_id", Integer, ForeignKey("connections.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    status = Column(Enum(UserStatus), default=UserStatus.active)
    avatar_seed = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    connections = relationship(
        "Connection", back_populates="owner", cascade="all, delete-orphan"
    )


class Connection(Base):
    __tablename__ = "connections"
    id = Column(Integer, primary_key=True, index=True)
    peer_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    tier = Column(Integer, default=1)
    state = Column(Enum(ConnectionState), default=ConnectionState.active_72h)
    last_event_date = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="connections")
    events = relationship("Event", back_populates="connection")
    mutual_connections = relationship(
        "Connection",
        secondary=mutual_connections_table,
        primaryjoin=id == mutual_connections_table.c.connection_id,
        secondaryjoin=id == mutual_connections_table.c.mutual_id,
        backref="mutual_of",
    )


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    location = Column(String, nullable=False)
    connection_id = Column(Integer, ForeignKey("connections.id"))
    connection = relationship("Connection", back_populates="events")