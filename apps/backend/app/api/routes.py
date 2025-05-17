from fastapi import APIRouter
from app.models.product import Product

router = APIRouter()

products_db = []

@router.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}


@router.post("/products")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Product created", "product": product}

@router.get("/products")
def list_products():
    return products_db