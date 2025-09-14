from dataclasses import dataclass

@dataclass
class CategoryEntity:
    id: str
    name: str
    status: str
    user_id: str
    created_at: str
    updated_at: str