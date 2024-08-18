# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatUpdateParams", "ContentUnionMember1"]


class ChatUpdateParams(TypedDict, total=False):
    project_id: Required[str]

    user_id: Required[str]

    content: Required[Union[str, Iterable[ContentUnionMember1]]]

    role: Required[Literal["user", "assistant", "tool"]]


class ContentUnionMember1(TypedDict, total=False):
    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]

    tool_name: Required[Annotated[str, PropertyInfo(alias="toolName")]]

    type: Required[str]

    result: Optional[object]
