from sqlalchemy import (
    ForeignKey,
    String,
    DateTime,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from datetime import datetime

from database.base import Base


class ChannelMapping(Base):

    __tablename__ = "channel_mappings"

    id: Mapped[int] = mapped_column(primary_key=True)

    variant_id: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
        nullable=False
    )

    # channel_id: Mapped[int] = mapped_column(
    #     ForeignKey("channel_fields.id"),
    #     nullable=False
    # )

    external_id: Mapped[str | None] = mapped_column(
        String(255)
    )

    offer_id: Mapped[str | None] = mapped_column(
        String(255)
    )

    status: Mapped[str | None] = mapped_column(
        String(100)
    )

    last_sync: Mapped[datetime | None]

    last_error: Mapped[str | None] = mapped_column(
        String(1000)
    )

    # ---------- Relationships ----------

    variant = relationship(
        "Variant",
        back_populates="channel_mappings"
    )


    channel_fields = relationship(
        "ChannelField",
        back_populates="channel_mappings",
        cascade="all, delete-orphan"
    )