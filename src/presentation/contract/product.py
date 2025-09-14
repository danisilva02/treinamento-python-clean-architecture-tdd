from pydantic import BaseModel

# Create Product
class PresentationProductCreateRequestDTO(BaseModel):
    name: str
    description: str
    price: int
    status: str
    category_id: str
    
class PresentationProductCreateResponseDTO(BaseModel):
    id: str
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str
    created_at: str
    updated_at: str
    
# Update Product
class PresentationProductUpdateRequestDTO(BaseModel):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    status: str | None = None
    category_id: str | None = None
    
class PresentationProductUpdateResponseDTO(BaseModel):
    id: str
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str
    created_at: str
    updated_at: str
    
# List Product
class PresentationProductListRequestDTO(BaseModel):
    user_id: str
    
class PresentationProductListResponseDTO(BaseModel):
    id: str
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str
    created_at: str
    updated_at: str
    
# Get Product
class PresentationProductGetRequestDTO(BaseModel):
    id: str
    
class PresentationProductGetResponseDTO(BaseModel):
    id: str
    name: str
    description: str
    price: int
    status: str
    category_id: str
    user_id: str
    created_at: str
    updated_at: str