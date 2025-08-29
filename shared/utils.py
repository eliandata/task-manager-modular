from typing import Any, Dict

from pydantic import BaseModel


class APIResponse(BaseModel):
    ok: bool
    data: Any | None = None
    error: str | None = None


def success(data: Any) -> Dict:
    return APIResponse(ok=True, data=data).model_dump()


def failure(msg: str) -> Dict:
    return APIResponse(ok=False, error=msg).model_dump()
