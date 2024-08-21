# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from invsy import Invsy, AsyncInvsy
from invsy.types import (
    ChatListResponse,
    ChatCreateResponse,
    ChatDeleteResponse,
    ChatUpdateResponse,
    ChatRetrieveResponse,
    ChatDeleteAllResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Invsy) -> None:
        chat = client.chats.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Invsy) -> None:
        response = client.chats.with_raw_response.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Invsy) -> None:
        with client.chats.with_streaming_response.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.chats.with_raw_response.create(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.chats.with_raw_response.create(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

    @parametrize
    def test_method_retrieve(self, client: Invsy) -> None:
        chat = client.chats.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Invsy) -> None:
        response = client.chats.with_raw_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Invsy) -> None:
        with client.chats.with_streaming_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.retrieve(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    def test_method_update(self, client: Invsy) -> None:
        chat = client.chats.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Invsy) -> None:
        chat = client.chats.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                    "id": "9f07c436ad3ecb7cb446e5e66400e1e3",
                    "created_at": "2024-08-08T21:19:38.855Z",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                    "id": "9f07c436ad3ecb7cb446e5e66400e1e3",
                    "created_at": "2024-08-08T21:19:38.855Z",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                    "id": "9f07c436ad3ecb7cb446e5e66400e1e3",
                    "created_at": "2024-08-08T21:19:38.855Z",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
            meta={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Invsy) -> None:
        response = client.chats.with_raw_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Invsy) -> None:
        with client.chats.with_streaming_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatUpdateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_project_id` but received ''"):
            client.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                path_project_id="",
                path_user_id="3db648cbb7f933aeb705b821c47c0e39",
                id="1febfa740898c02b25897949bf6961ad",
                created_at="2024-08-08T21:19:38.855Z",
                messages=[
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                ],
                body_project_id="",
                body_user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_user_id` but received ''"):
            client.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                path_user_id="",
                id="1febfa740898c02b25897949bf6961ad",
                created_at="2024-08-08T21:19:38.855Z",
                messages=[
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                ],
                body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body_user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.update(
                chat_id="",
                path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                path_user_id="3db648cbb7f933aeb705b821c47c0e39",
                id="1febfa740898c02b25897949bf6961ad",
                created_at="2024-08-08T21:19:38.855Z",
                messages=[
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                ],
                body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body_user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    def test_method_list(self, client: Invsy) -> None:
        chat = client.chats.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Invsy) -> None:
        response = client.chats.with_raw_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Invsy) -> None:
        with client.chats.with_streaming_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.chats.with_raw_response.list(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.chats.with_raw_response.list(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
            )

    @parametrize
    def test_method_delete(self, client: Invsy) -> None:
        chat = client.chats.delete(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Invsy) -> None:
        response = client.chats.with_raw_response.delete(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Invsy) -> None:
        with client.chats.with_streaming_response.delete(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatDeleteResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.chats.with_raw_response.delete(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.chats.with_raw_response.delete(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.delete(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    def test_method_delete_all(self, client: Invsy) -> None:
        chat = client.chats.delete_all(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_delete_all(self, client: Invsy) -> None:
        response = client.chats.with_raw_response.delete_all(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete_all(self, client: Invsy) -> None:
        with client.chats.with_streaming_response.delete_all(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_all(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.chats.with_raw_response.delete_all(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.chats.with_raw_response.delete_all(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
            )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.chats.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInvsy) -> None:
        response = await async_client.chats.with_raw_response.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInvsy) -> None:
        async with async_client.chats.with_streaming_response.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.chats.with_raw_response.create(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.chats.with_raw_response.create(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.chats.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInvsy) -> None:
        response = await async_client.chats.with_raw_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInvsy) -> None:
        async with async_client.chats.with_streaming_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.retrieve(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.chats.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.chats.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                    "id": "9f07c436ad3ecb7cb446e5e66400e1e3",
                    "created_at": "2024-08-08T21:19:38.855Z",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                    "id": "9f07c436ad3ecb7cb446e5e66400e1e3",
                    "created_at": "2024-08-08T21:19:38.855Z",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                    "id": "9f07c436ad3ecb7cb446e5e66400e1e3",
                    "created_at": "2024-08-08T21:19:38.855Z",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
            meta={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInvsy) -> None:
        response = await async_client.chats.with_raw_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInvsy) -> None:
        async with async_client.chats.with_streaming_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            path_user_id="3db648cbb7f933aeb705b821c47c0e39",
            id="1febfa740898c02b25897949bf6961ad",
            created_at="2024-08-08T21:19:38.855Z",
            messages=[
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
                {
                    "content": "Hello, this is a message.",
                    "role": "user",
                },
            ],
            body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body_user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatUpdateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_project_id` but received ''"):
            await async_client.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                path_project_id="",
                path_user_id="3db648cbb7f933aeb705b821c47c0e39",
                id="1febfa740898c02b25897949bf6961ad",
                created_at="2024-08-08T21:19:38.855Z",
                messages=[
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                ],
                body_project_id="",
                body_user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_user_id` but received ''"):
            await async_client.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                path_user_id="",
                id="1febfa740898c02b25897949bf6961ad",
                created_at="2024-08-08T21:19:38.855Z",
                messages=[
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                ],
                body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body_user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.update(
                chat_id="",
                path_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                path_user_id="3db648cbb7f933aeb705b821c47c0e39",
                id="1febfa740898c02b25897949bf6961ad",
                created_at="2024-08-08T21:19:38.855Z",
                messages=[
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                    {
                        "content": "Hello, this is a message.",
                        "role": "user",
                    },
                ],
                body_project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body_user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.chats.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInvsy) -> None:
        response = await async_client.chats.with_raw_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInvsy) -> None:
        async with async_client.chats.with_streaming_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.chats.with_raw_response.list(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.chats.with_raw_response.list(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.chats.delete(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInvsy) -> None:
        response = await async_client.chats.with_raw_response.delete(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInvsy) -> None:
        async with async_client.chats.with_streaming_response.delete(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatDeleteResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.chats.with_raw_response.delete(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.chats.with_raw_response.delete(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.delete(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    async def test_method_delete_all(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.chats.delete_all(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncInvsy) -> None:
        response = await async_client.chats.with_raw_response.delete_all(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncInvsy) -> None:
        async with async_client.chats.with_streaming_response.delete_all(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.chats.with_raw_response.delete_all(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.chats.with_raw_response.delete_all(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
            )
