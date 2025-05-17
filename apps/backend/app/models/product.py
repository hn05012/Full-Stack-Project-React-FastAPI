from pydantic import BaseModel

class Product(BaseModel):
    name: str
    color: str
    description: str
    image: str
    category: str
