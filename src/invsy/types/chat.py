# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Chat", "Message", "MessageContentUnionMember1"]


class MessageContentUnionMember1(BaseModel):
    tool_call_id: str = FieldInfo(alias="toolCallId")

    tool_name: str = FieldInfo(alias="toolName")

    type: str

    result: Optional[object] = None


class Message(BaseModel):
    content: Union[str, List[MessageContentUnionMember1]]
    """The content of the message."""

    role: Literal["user", "assistant", "tool", "system"]

    id: Optional[str] = None

    created_at: Optional[str] = None


class Chat(BaseModel):
    id: str

    created_at: str

    messages: List[Message]

    project_id: str

    user_id: str

    meta: Optional[Dict[str, str]] = None
    """Metadata for the chat"""
