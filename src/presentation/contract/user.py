from pydantic import BaseModel

# Create User
class PresentationUserCreateRequestDTO(BaseModel):
    email: str
    name: str
    password: str
    
class PresentationUserCreateResponseDTO(BaseModel):
    id: str
    email: str
    name: str
    created_at: str
    updated_at: str
    
# Login User
class PresentationUserLoginRequestDTO(BaseModel):
    email: str
    password: str
    
class PresentationUserLoginResponseDTO(BaseModel):
    token: str
    
# Me User
class PresentationUserMeRequestDTO(BaseModel):
    user_id: str
    
class PresentationUserMeResponseDTO(BaseModel):
    id: str
    email: str
    name: str
    created_at: str
    updated_at: str
    
# Update User
class PresentationUserUpdateRequestDTO(BaseModel):
    name: str
    email: str | None = None
    
class PresentationUserUpdateResponseDTO(BaseModel):
    id: str
    name: str
    email: str
    created_at: str
    updated_at: str