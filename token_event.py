import orjson
from pydantic.json import pydantic_encoder
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import Any, Callable, Optional


def orjson_dumps(value: Any, *, default: Callable) -> str:
    return orjson.dumps(
        value, default=default, option=orjson.OPT_SERIALIZE_UUID
    ).decode()


class TokenEvent(BaseModel):
    class Config:
        allow_population_by_field_name = True
        anystr_strip_whitespace = True
        json_dumps = orjson_dumps
        json_encoders = {UUID: lambda x: pydantic_encoder(x)}
        json_loads = orjson.loads
        orm_mode = False
        validate_all = True
        use_enum_values = False
        validate_assignment = True
        extra = "allow"
        allow_mutation = False
        frozen = True

    event_id: int
    parent_event_id: int
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    max_supply: Optional[float]
    current_supply: Optional[float]
    description: Optional[str]
    extra_data: Optional[dict]
