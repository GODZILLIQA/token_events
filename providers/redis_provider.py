from bin.settings import get_settings
from redis import Redis


def start_redis() -> Redis:
    return Redis(host=get_settings().redis_server, port=6379, db=0)
