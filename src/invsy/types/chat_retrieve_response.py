# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .chat import Chat
from .._models import BaseModel

__all__ = ["ChatRetrieveResponse"]


class ChatRetrieveResponse(BaseModel):
    result: Chat

    success: bool
