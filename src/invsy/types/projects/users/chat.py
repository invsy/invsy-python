# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Chat", "Message"]


class Message(BaseModel):
    id: str

    content: str

    created_at: str

    role: Literal["user", "assistant"]


class Chat(BaseModel):
    id: str

    created_at: str

    messages: List[Message]

    project_id: str

    user_id: str

    meta: Optional[Dict[str, str]] = None
    """Metadata for the chat"""
