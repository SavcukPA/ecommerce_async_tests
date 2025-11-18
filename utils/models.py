from pydantic import BaseModel
from typing import List, Any, Optional


class ErrorData(BaseModel):
    loc: List[str]
    msg: str
    type: str
    input: Any
    ctx: Optional[dict] = None
    url: Optional[str] = None


class ErrorResponseModel(BaseModel):
    detail: List[ErrorData]


class ErrorDetail(BaseModel):
    detail: str
