import reflex as rx
from typing import Literal


class UserProfile(rx.Base):
    id: int
    name: str
    email: str
    phone: str | None = None
    status: Literal["active", "paused", "breathing"]
    avatar_seed: str | None = None


class Connection(rx.Base):
    id: int
    peer_name: str
    email: str | None = None
    tier: int
    state: Literal["engaged", "active_72h", "paused", "dormant"]
    last_event_date: str
    avatar_url: str
    mutual_connection_ids: list[int] = []


class Event(rx.Base):
    id: int
    title: str
    date: str
    time: str
    location: str
    connection_id: int


class UserStats(rx.Base):
    active_connections: int
    total_exchanges: int
    events_coordinated: int
    longest_relationship_days: int
    revived_connections: int


class Suggestion(rx.Base):
    id: int
    icon: str
    title: str
    description: str
    type: Literal["individual", "group", "system"] = "system"
    involved_connections: list[int] = []