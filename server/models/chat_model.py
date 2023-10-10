from pydantic import BaseModel, EmailStr, Field


class ChatSchema(BaseModel):
  fullname: str = Field(...)
  email: EmailStr = Field(...)
  content: str = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "fullname": "Hong Mei",
        "email": "hongmei@edu.ng",
        "content": "This is the first chat"
      }
    }
    