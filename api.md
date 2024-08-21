# Chats

Types:

```python
from invsy.types import (
    Chat,
    Chats,
    ChatCreateResponse,
    ChatRetrieveResponse,
    ChatUpdateResponse,
    ChatListResponse,
    ChatDeleteResponse,
    ChatDeleteAllResponse,
)
```

Methods:

- <code title="post /projects/{project_id}/users/{user_id}/chats">client.chats.<a href="./src/invsy/resources/chats.py">create</a>(user_id, \*, project_id, \*\*<a href="src/invsy/types/chat_create_params.py">params</a>) -> <a href="./src/invsy/types/chat_create_response.py">ChatCreateResponse</a></code>
- <code title="get /projects/{project_id}/users/{user_id}/chats/{chat_id}">client.chats.<a href="./src/invsy/resources/chats.py">retrieve</a>(chat_id, \*, project_id, user_id) -> <a href="./src/invsy/types/chat_retrieve_response.py">ChatRetrieveResponse</a></code>
- <code title="put /projects/{project_id}/users/{user_id}/chats/{chat_id}">client.chats.<a href="./src/invsy/resources/chats.py">update</a>(chat_id, \*, path_project_id, path_user_id, \*\*<a href="src/invsy/types/chat_update_params.py">params</a>) -> <a href="./src/invsy/types/chat_update_response.py">ChatUpdateResponse</a></code>
- <code title="get /projects/{project_id}/users/{user_id}/chats">client.chats.<a href="./src/invsy/resources/chats.py">list</a>(user_id, \*, project_id) -> <a href="./src/invsy/types/chat_list_response.py">ChatListResponse</a></code>
- <code title="delete /projects/{project_id}/users/{user_id}/chats/{chat_id}">client.chats.<a href="./src/invsy/resources/chats.py">delete</a>(chat_id, \*, project_id, user_id) -> <a href="./src/invsy/types/chat_delete_response.py">ChatDeleteResponse</a></code>
- <code title="delete /projects/{project_id}/users/{user_id}/chats">client.chats.<a href="./src/invsy/resources/chats.py">delete_all</a>(user_id, \*, project_id) -> <a href="./src/invsy/types/chat_delete_all_response.py">ChatDeleteAllResponse</a></code>
