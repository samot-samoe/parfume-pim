from database.base import Base
from database.database import engine

import models.brand
import models.product
import models.variant

Base.metadata.create_all(engine)