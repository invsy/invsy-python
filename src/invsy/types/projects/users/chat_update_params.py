# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatUpdateParams", "Message", "MessageContentUnionMember1"]


class ChatUpdateParams(TypedDict, total=False):
    path_project_id: Required[Annotated[str, PropertyInfo(alias="project_id")]]

    path_user_id: Required[Annotated[str, PropertyInfo(alias="user_id")]]

    id: Required[str]

    created_at: Required[str]

    messages: Required[Iterable[Message]]

    body_project_id: Required[Annotated[str, PropertyInfo(alias="project_id")]]

    body_user_id: Required[Annotated[str, PropertyInfo(alias="user_id")]]

    meta: Dict[str, str]
    """Metadata for the chat"""


class MessageContentUnionMember1(TypedDict, total=False):
    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]

    tool_name: Required[Annotated[str, PropertyInfo(alias="toolName")]]

    type: Required[str]

    result: Optional[object]


class Message(TypedDict, total=False):
    id: Required[str]

    content: Required[Union[str, Iterable[MessageContentUnionMember1]]]
    """The content of the message."""

    created_at: Required[str]

    role: Required[Literal["user", "assistant", "tool"]]
