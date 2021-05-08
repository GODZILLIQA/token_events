from fastapi import APIRouter
from .token_event_endpoints import token_events_router

api_router = APIRouter()
api_router.include_router(router=token_events_router, tags=["token_events"])
