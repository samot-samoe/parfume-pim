from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey
from sqlalchemy import String

from database.base import Base


class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    brand_id: Mapped[int] = mapped_column(
        ForeignKey("brands.id")
    )

    internal_sku: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    name: Mapped[str]

    line: Mapped[str | None]

    product_type: Mapped[str]

    gender: Mapped[str | None]

    status: Mapped[str] = mapped_column(default="draft")

    brand = relationship(
        "Brand",
        back_populates="products"
    )

    variants = relationship(
        "Variant",
        back_populates="product",
        cascade="all, delete-orphan"
    )

    def __repr__(self):

        return f"<Product {self.name}>"