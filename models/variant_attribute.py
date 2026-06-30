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


class VariantAttribute(Base):

    __tablename__ = "variant_attributes"

    id: Mapped[int] = mapped_column(primary_key=True)

    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(255)
    )

    data_type: Mapped[str] = mapped_column(
        String(50)
    )

    unit: Mapped[str | None] = mapped_column(
        String(50)
    )

    is_required: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # ---------- Relationships ----------

    attributes = relationship(
        "Attribute",
        back_populates="variant_attribute",
        cascade="all, delete-orphan"
    )