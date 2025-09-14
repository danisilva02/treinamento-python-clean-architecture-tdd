from dataclasses import dataclass

# General
@dataclass
class ProductOutputDTO:
    id: str
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str
    created_at: str
    updated_at: str
    
# Create
@dataclass
class ProductCreateInputDTO:
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str

# Update
@dataclass
class ProductUpdateInputDTO:
    id: str
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str
    
# Get
@dataclass
class ProductGetInputDTO:
    id: str
    
# List
@dataclass
class ProductListInputDTO:
    user_id: str