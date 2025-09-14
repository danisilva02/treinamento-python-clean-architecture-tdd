from typing import Protocol, Optional, TypedDict

class Claims(TypedDict, total=False):
    user_id: str

"""
Contrato para gerenciar a segurança da aplicação
"""
class SecurityContract(Protocol):
    """Gera e verifica tokens JWT"""
    def generate_token(self, user_id: str) -> str:
        pass
    
    def verify_token(self, token: str) -> tuple[dict, Optional[Claims]]:
        """retorna (ok, error_code, claims)"""
        pass
    
    def hash_password(self, password: str) -> str:
        """Retorna o hash da senha"""
        pass