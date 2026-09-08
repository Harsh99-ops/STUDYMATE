from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.connection import Base


class Space(Base):
    __tablename__ = "spaces"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    description = Column(Text, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )