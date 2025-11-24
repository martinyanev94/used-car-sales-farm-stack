from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    zip_code: Optional[str] = None  # Default to None if not provided
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Elm St",
        "city": "Somewhere"
    }
}
