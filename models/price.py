from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy import String

from database.base import Base

from datetime import datetime


class Price(Base):

    __tablename__ = "prices"

    id: Mapped[int] = mapped_column(primary_key=True)

    variant_id: Mapped[int] = mapped_column(
        ForeignKey("variants.id")
        )

    channel_id: Mapped[int] = mapped_column(
        ForeignKey("channels.id")
        )
    
    price: Mapped[int]

    old_price: Mapped[int ]
    
    currency: Mapped[int]

    valid_from: Mapped[datetime | None]

    valid_to: Mapped[datetime | None]

    # ---------- Relationships ----------

    variant = relationship(
        "Variant",
        back_populates="prices"
    )

    channel = relationship(
        "Channel",
        back_populates="prices"
    )

    def __repr__(self):
# 
        return f"<Price {self.name}>"