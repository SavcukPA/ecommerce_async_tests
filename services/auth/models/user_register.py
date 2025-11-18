from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: UUID
    email: EmailStr = Field(..., description="Валидный email адрес")
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=256,
        description="Имя (2-256 символов)",
    )
    last_name: str = Field(
        ...,
        min_length=2,
        max_length=256,
        description="Фамилия (2-256 символов)",
    )
