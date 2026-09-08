from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.space import Space
from app.schemas import SpaceCreate, SpaceResponse


router = APIRouter(
    prefix="/spaces",
    tags=["Spaces"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SpaceResponse)
def create_space(
    space: SpaceCreate,
    db: Session = Depends(get_db)
):
    new_space = Space(
        name=space.name,
        description=space.description
    )

    db.add(new_space)
    db.commit()
    db.refresh(new_space)

    return new_space