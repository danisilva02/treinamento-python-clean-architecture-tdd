from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .presentation import health
from .presentation import routers
from .infra.driver.driver import Driver
from .infra.migration.migrate import Migrate
from dotenv import load_dotenv
import uvicorn

load_dotenv()

def lifespan(app: FastAPI):
    driver = Driver()
    app.state.driver = driver
    migrate = Migrate(driver=driver)
    migrate.perform()
    yield
    return app

app = FastAPI(
    title="Treinamento Python Clean Architecture + TDD",
    description="Crud de usuário, categoria e produto",
    summary="API para o Treinamento Python Clean Architecture + TDD 🚀",
    version="0.0.1",
    root_path="/api",
    terms_of_service="https://areteacademy.com.br",
    contact={
        "name": "Arete Academy",
        "url": "https://areteacademy.com.br",
        "email": "areteacademy.dev@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=80)
