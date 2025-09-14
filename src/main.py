from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .presentation import health
from .presentation import routers
from dotenv import load_dotenv
import uvicorn
load_dotenv()

app = FastAPI(
    title="Treinamento Python Clean Architecture + TDD",
    description="Crud de usuário, categoria e produto",
    summary="API para o Treinamento Python Clean Architecture + TDD 🚀",
    version="0.0.1",
    root_path="/api",
    terms_of_service="https://www.google.com/",
    contact={
        "name": "Daniel Silva",
        "url": "https://www.google.com/",
        "email": "daniel.silvamiranda02@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(routers.router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
