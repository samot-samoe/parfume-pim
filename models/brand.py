from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import String

from database.base import Base


class Brand(Base):

    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    country: Mapped[str | None]

    website: Mapped[str | None]

    description: Mapped[str | None]

    products = relationship(
        "Product",
        back_populates="brand"
    )

    def __repr__(self):

        return f"<Brand {self.name}>"