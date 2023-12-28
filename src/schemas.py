from typing import Optional

from pydantic import BaseModel, Field


class ContactSchema(BaseModel):
    first_name: str = Field(max_length=50, min_length=3)
    last_name: str = Field(max_length=50, min_length=3)
    email: str = Field(max_length=30, min_length=5)
    phone_number: str = Field(max_length=30, min_length=5)
    birthday: str = Field(max_length=30, min_length=8)
    data: Optional[bool] = False


class ContactUpdateSchema(ContactSchema):
    data: bool


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: str
    data: bool

    class Config:
        from_attributes = True
