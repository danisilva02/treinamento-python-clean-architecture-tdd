from dataclasses import dataclass

# Generic
@dataclass(frozen=True)
class CategoryOutputDTO:
    id: str
    name: str
    status: str
    user_id: str
    created_at: str
    updated_at: str

# Create
@dataclass
class CategoryCreateInputDTO:
    name: str
    status: str
    user_id: str

CategoryCreateOutputDTO = CategoryOutputDTO

# List
@dataclass
class CategoryListInputDTO:
    user_id: str
    
UsecaseCategoryListOutputDTO = CategoryOutputDTO

# Update
@dataclass
class CategoryUpdateInputDTO:
    name: str
    status: str
    
CategoryUpdateOutputDTO = CategoryOutputDTO
    
# Get
UsecaseCategoryGetOutputDTO = CategoryOutputDTO