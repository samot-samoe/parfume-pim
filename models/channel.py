from sqlalchemy import (
    Boolean,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from database.base import Base


class Channel(Base):

    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    type: Mapped[str | None] = mapped_column(
        String(100)
    )

    description: Mapped[str | None]

    api_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    # ---------- Relationships ----------
    prices = relationship(
        "Price",
        back_populates="channel",
        cascade="all, delete-orphan"
    )
    def __repr__(self):

        return f"<Channel(name='{self.name}')>"