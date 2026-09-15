from ..core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, DateTime, Integer
from sqlalchemy import ForeignKey
from typing import Optional
from datetime import datetime

from .type_event import TypeEvent

class Event(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(40), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100))
    imgUrl: Mapped[Optional[str]] = mapped_column(String)
    eventAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    
    event_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("types_events.id"), nullable=False)
    type_event = Mapped[TypeEvent] = relationship("TypeEvent", back_populates="events")