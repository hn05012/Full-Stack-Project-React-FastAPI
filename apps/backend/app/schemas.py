from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: int
    color: str
    category: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True  # Allows returning ORM objects directly
