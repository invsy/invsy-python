# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatDeleteAllResponse"]


class ChatDeleteAllResponse(BaseModel):
    success: bool

    result: Optional[object] = None
