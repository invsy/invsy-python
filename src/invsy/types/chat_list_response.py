# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .chats import Chats
from .._models import BaseModel

__all__ = ["ChatListResponse"]


class ChatListResponse(BaseModel):
    result: Chats

    success: bool
