from dataclasses import dataclass

@dataclass
class ProductEntity:
    id: str
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str
    created_at: str
    updated_at: str