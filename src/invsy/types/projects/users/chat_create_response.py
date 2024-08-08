# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ...._models import BaseModel

__all__ = ["ChatCreateResponse"]


class ChatCreateResponse(BaseModel):
    id: str

    created_at: str

    project_id: str

    user_id: str
