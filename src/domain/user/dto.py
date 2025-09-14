from dataclasses import dataclass

# Generic
@dataclass(frozen=True)
class UserOutputDTO:
    id: str
    email: str
    name: str
    created_at: str
    updated_at: str

# User
@dataclass
class UserCreateDTO:
    email: str
    name: str
    password: str

UserCreateOutputDTO = UserOutputDTO

# Login
@dataclass
class UserLoginDTO:
    email: str
    password: str

@dataclass
class UserLoginOutputDTO:
    token: str

# Me
@dataclass
class UserMeDTO:
    user_id: str
 
UserMeOutputDTO = UserOutputDTO

# Update
@dataclass
class UserUpdateInputDTO:
    id: str
    name: str
    email: str

UserUpdateOutputDTO = UserOutputDTO