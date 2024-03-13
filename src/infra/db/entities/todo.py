from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base


class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=255), nullable=False)

    def __repr__(self):
        return f"ToDo [id={self.id}, title={self.title}]"
