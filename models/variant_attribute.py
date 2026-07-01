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


class VariantAttribute(Base):

    __tablename__ = "variant_attributes"

    id: Mapped[int] = mapped_column(primary_key=True)

    variant_id: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
        nullable=False
    )

    attribute_id: Mapped[int] = mapped_column(
        ForeignKey("attributes.id"),
        nullable=False
    )

    value: Mapped[str] = mapped_column(
        String(1000)
    )

    # ---------- Relationships ----------

    variant = relationship(
        "Variant",
        back_populates="attributes"
    )

    attribute = relationship(
        "Attribute",
        back_populates="variant_attributes"
    )