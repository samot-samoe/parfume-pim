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


class Attribute(Base):

    __tablename__ = "attributes"

    id: Mapped[int] = mapped_column(primary_key=True)

    variant_id: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
        nullable=False
    )

    attribute_id: Mapped[int] = mapped_column(
        ForeignKey("variant_attributes.id"),
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

    variant_attribute = relationship(
        "VariantAttribute",
        back_populates="attributes"
    )