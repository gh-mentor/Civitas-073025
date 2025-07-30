# Represents a row in the 'products' table

from datetime import datetime
from typing import Optional

class Product:
    def __init__(
        self,
        product_id: Optional[int] = None,
        product_name: str = "",
        description: Optional[str] = None,
        category_id: Optional[int] = None,
        quantity: int = 0,
        price: float = 0.0,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.category_id = category_id
        self.quantity = quantity
        self.price = price
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __repr__(self):
        return (
            f"Product(product_id={self.product_id}, product_name='{self.product_name}', "
            f"description='{self.description}', category_id={self.category_id}, "
            f"quantity={self.quantity}, price={self.price}, "
            f"created_at={self.created_at}, updated_at={self.updated_at})"
        )
    
    def update_quantity(self, amount: int):
        """Update the quantity of the product."""
        self.quantity += amount
        self.updated_at = datetime.now()
        
    def update_price(self, new_price: float):
        """Update the price of the product."""
        self.price = new_price
        self.updated_at = datetime.now()
    def to_dict(self):
        """Convert the product to a dictionary."""
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "description": self.description,
            "category_id": self.category_id,
            "quantity": self.quantity,
            "price": self.price,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }   
    @classmethod
    def from_dict(cls, data: dict):
        """Create a product from a dictionary."""
        return cls(
            product_id=data.get("product_id"),
            product_name=data.get("product_name"),
            description=data.get("description"),
            category_id=data.get("category_id"),
            quantity=data.get("quantity", 0),
            price=data.get("price", 0.0),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None,
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else None
        )
