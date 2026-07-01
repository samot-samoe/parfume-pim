from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from database.base import Base


class ChannelField(Base):

    __tablename__ = "channel_fields"

    id: Mapped[int] = mapped_column(primary_key=True)

    channel_mapping_id: Mapped[int] = mapped_column(
        ForeignKey("channel_mappings.id"),
        nullable=False
    )

    field_name: Mapped[str] = mapped_column(
        String(255)
    )

    field_value: Mapped[str | None] = mapped_column(
        String(5000)
    )

    # ---------- Relationships ----------

    channel_mapping = relationship(
        "ChannelMapping",
        back_populates="channel_fields"
    )