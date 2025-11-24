from pydantic import validator

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Address

    @validator('name')
    def name_must_not_contain_digits(cls, v):
        if any(char.isdigit() for char in v):
            raise ValueError('Name must not contain digits')
        return v
