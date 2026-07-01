from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Numeric

from database.base import Base


class Variant(Base):

    __tablename__ = "variants"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id")
    )

    sku: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    barcode: Mapped[str | None]

    ean: Mapped[str | None]

    volume_ml: Mapped[float | None] = mapped_column(
        Numeric(6,2)
    )#????

    weight_g: Mapped[float | None]

    length_mm: Mapped[float | None]

    width_mm: Mapped[float | None]

    height_mm: Mapped[float | None]

    active: Mapped[bool] = mapped_column(default=True)

  # ---------- Relationships ----------

    product = relationship(
        "Product",
        back_populates="variant"
    )

    prices = relationship(
        "Price",
        back_populates="variant",
        cascade="all, delete-orphan"
    )

    stocks = relationship(
        "Stock",
        back_populates="variant",
        cascade="all, delete-orphan"
    )

    images = relationship(
        "Image",
        back_populates="variant",
        cascade="all, delete-orphan"
    )

    attributes = relationship(
        "VariantAttribute",
        back_populates="variant",
        cascade="all, delete-orphan"
    )

    channel_mappings = relationship(
        "ChannelMapping",
        back_populates="variant",
        cascade="all, delete-orphan"
    )

    def __repr__(self):

        return f"<Variant {self.sku}>"