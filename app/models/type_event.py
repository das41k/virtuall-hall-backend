from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer

from ..core.database import Base
from .event import Event

class TypeEvent(Base):
    __tablename__ = "types_events"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(String(100))
    events: Mapped[list[Event]] = relationship("Event", back_populates="type_event", lazy="selectin")