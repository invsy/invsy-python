# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["Chat"]


class Chat(BaseModel):
    id: str

    created_at: str

    messages: str

    project_id: str

    user_id: str

    meta: Optional[Dict[str, str]] = None
    """Metadata for the chat"""
