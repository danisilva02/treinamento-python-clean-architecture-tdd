from pydantic import BaseModel

# Create Category
class PresentationCategoryCreateRequestDTO(BaseModel):
    name: str
    status: str
    
class PresentationCategoryCreateResponseDTO(BaseModel):
    id: str
    name: str
    status: str
    user_id: str
    created_at: str
    updated_at: str
    
# List Category
class PresentationCategoryListResponseDTO(BaseModel):
    id: str
    name: str
    status: str
    user_id: str
    created_at: str
    updated_at: str
    
# Update Category
class PresentationCategoryUpdateRequestDTO(BaseModel):
    name: str | None = None
    status: str | None = None
    
class PresentationCategoryUpdateResponseDTO(BaseModel):
    id: str
    name: str
    status: str
    user_id: str
    created_at: str
    updated_at: str
    
# Get Category
class PresentationCategoryGetRequestDTO(BaseModel):
    id: str

class PresentationCategoryGetResponseDTO(BaseModel):
    id: str
    name: str
    status: str
    user_id: str
    created_at: str
    updated_at: str