
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from React dev server
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)
#for dict
'''products= products = [
    {"id": 1, "name": "phone", "description": "iphone", "price": 2000.90, "quantity": 30},
    {"id": 2, "name": "laptop", "description": "gaming laptop", "price": 35000.90, "quantity": 20}
]'''

#for pydantic model
products = [
    Product(id=1, name="phone", description="iphone", price=2000.90, quantity=30),
    Product(id=2, name="laptop", description="gaming laptop", price=35000.90, quantity=20)
]

#It creates and manages a database session for each request
def get_db():
    db = session()
    try:
        yield db #sends data to the API and waits for the next request to continue execution
    finally:
        db.close()#closes the database session after the request is completed, ensuring that resources are properly released.

def init_db():
    db=session()
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()

#Operations without database.
'''@app.get("/")
def getAllProducts():
    return products'''

#for dict
"""@app.get("/product/{id}")
def getproductby_id(id:int):
    for product in products:
        if product["id"] == id:
            return product
        
    return "product not found" """

'''@app.get("/product/{id}")
def getproductby_id(id:int):
    for product in products:
        if product.id == id:
            return product
        
    return "product not found"'''

'''@app.post("/product")
def addproduct(product :Product):
    products.append(product)
    return product'''

'''@app.put("/product")
def update_product(id:int, update_product:Product):
    for index, product in enumerate(products):
        if product.id == id:
            products[index] = update_product
            return update_product
    return "No product found"'''
            
"""@app.delete("/product")
def delete_product(id:int):
    for product in products:
        if product.id==id:
            products.remove(product)
            return "product with id {id} is removed"
    return "Product not Found" """

'''@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id ==id:
            del products[i]
            return "product is removed"
    return "Product not Found"'''

#Operations with database
@app.get("/products")
def getAllProducts(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def getproductby_id(id:int, db: Session = Depends(get_db) ):
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
        
    return "product not found" 

@app.post("/products")
def addproduct(product :Product, db: Session = Depends(get_db) ):
  db.add(database_models.Product(**product.model_dump()))
  db.commit()#for changes we need to add commit , no need for fetching
  return product 

@app.put("/products/{id}")
def update_product(id:int, product:Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()     
        return "product updated"
    else:
        return "No product found" 
    
@app.delete("/products/{id}")
def delete_product(id:int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product not Found"