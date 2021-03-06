from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from endpoints.api_endpoints import api_router
from loguru import logger
from .settings import get_settings


@logger.catch
def start_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        debug=settings.debug,
        title=settings.project_name,
        openapi_url=f"{settings.api_v1_str}/openapi.json",
        default_response_class=ORJSONResponse,
    )

    app.include_router(api_router)
    app.add_middleware(SessionMiddleware, secret_key=settings.api_secret_key)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def startup() -> None:
        pass

    @app.on_event("shutdown")
    async def shutdown() -> None:
        pass

    @app.get("/")
    async def index() -> ORJSONResponse:
        return ORJSONResponse({"test": True})

    return app
