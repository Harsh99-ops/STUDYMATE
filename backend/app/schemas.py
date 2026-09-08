from datetime import datetime

from pydantic import BaseModel


class SpaceCreate(BaseModel):
    name: str
    description: str | None = None


class SpaceResponse(BaseModel):
    id: int
    name: str
    description: str | None
    created_at: datetime

    class Config:
        from_attributes = True