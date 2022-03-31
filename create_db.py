from database import Base, engine
from db.models.users import User
Base.metadata.create_all(engine)