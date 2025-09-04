from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=120)  
    phone: Optional[str] = Field(None, regex=r"^\+?\d{7,15}$")  
    # Ejemplo de validador extra
    @validator("username")
    def username_must_be_capitalized(cls, value):
        return value.title()
