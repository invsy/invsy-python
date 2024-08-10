# Projects

## Users

### Chats

Types:

```python
from invsy.types.projects.users import Chat, Chats
```

Methods:

- <code title="post /projects/{project_id}/users/{user_id}/chats">client.projects.users.chats.<a href="./src/invsy/resources/projects/users/chats.py">create</a>(user_id, \*, project_id, \*\*<a href="src/invsy/types/projects/users/chat_create_params.py">params</a>) -> <a href="./src/invsy/types/projects/users/chat.py">Chat</a></code>
- <code title="get /projects/{project_id}/users/{user_id}/chats/{chat_id}">client.projects.users.chats.<a href="./src/invsy/resources/projects/users/chats.py">retrieve</a>(chat_id, \*, project_id, user_id) -> <a href="./src/invsy/types/projects/users/chat.py">Chat</a></code>
- <code title="put /projects/{project_id}/users/{user_id}/chats/{chat_id}">client.projects.users.chats.<a href="./src/invsy/resources/projects/users/chats.py">update</a>(chat_id, \*, project_id, user_id, \*\*<a href="src/invsy/types/projects/users/chat_update_params.py">params</a>) -> <a href="./src/invsy/types/projects/users/chat.py">Chat</a></code>
- <code title="get /projects/{project_id}/users/{user_id}/chats">client.projects.users.chats.<a href="./src/invsy/resources/projects/users/chats.py">list</a>(user_id, \*, project_id) -> <a href="./src/invsy/types/projects/users/chats.py">Chats</a></code>
