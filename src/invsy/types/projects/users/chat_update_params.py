# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatUpdateParams"]


class ChatUpdateParams(TypedDict, total=False):
    project_id: Required[str]

    user_id: Required[str]

    content: Required[str]

    role: Required[Literal["user", "assistant", "tool"]]
