# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateParams"]


class ChatCreateParams(TypedDict, total=False):
    project_id: Required[str]

    body: Required[Dict[str, str]]
    """Metadata for the chat"""
