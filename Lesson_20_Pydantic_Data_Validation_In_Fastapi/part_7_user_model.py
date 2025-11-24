from pydantic import constr

class User(BaseModel):
    id: int
    name: constr(strip_whitespace=True, min_length=1)  # Strip spaces and ensure there's at least one character
    email: EmailStr
    address: Address
