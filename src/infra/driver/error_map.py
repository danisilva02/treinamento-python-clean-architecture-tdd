from sqlalchemy.exc import (
    IntegrityError,
    OperationalError,
    ProgrammingError,
    DataError,
    SQLAlchemyError,
)

def map_sqlalchemy_error(exc: SQLAlchemyError) -> str:
    """Traduz erros do SQLAlchemy para mensagens de domínio legíveis."""

    if isinstance(exc, IntegrityError):
        msg = str(exc).lower()
        
        print(msg, flush=True)

        if "unique constraint" in msg or "duplicate key" in msg:
            return "Já existe um registro com esses dados."

        if "foreign key constraint" in msg or "foreign key violation" in msg:
            if "update or delete" in msg:
                return "Não é possível excluir este registro, pois ele está sendo usado em outros cadastros."
            return "O registro referenciado não existe ou foi removido."

        return "Violação de integridade nos dados fornecidos."

    elif isinstance(exc, OperationalError):
        return "Erro de conexão com o banco de dados. Tente novamente em alguns instantes."

    elif isinstance(exc, ProgrammingError):
        return "Erro interno na consulta SQL. Contate o suporte técnico."

    elif isinstance(exc, DataError):
        return "Os dados enviados não estão no formato esperado."

    else:
        return "Erro inesperado ao acessar o banco de dados."
