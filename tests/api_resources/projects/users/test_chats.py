# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from invsy import Invsy, AsyncInvsy
from tests.utils import assert_matches_type
from invsy.types.projects.users import Chat, Chats

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Invsy) -> None:
        chat = client.projects.users.chats.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Invsy) -> None:
        response = client.projects.users.chats.with_raw_response.create(
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
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Invsy) -> None:
        with client.projects.users.chats.with_streaming_response.create(
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
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.chats.with_raw_response.create(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.chats.with_raw_response.create(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

    @parametrize
    def test_method_retrieve(self, client: Invsy) -> None:
        chat = client.projects.users.chats.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Invsy) -> None:
        response = client.projects.users.chats.with_raw_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Invsy) -> None:
        with client.projects.users.chats.with_streaming_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.projects.users.chats.with_raw_response.retrieve(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    def test_method_update(self, client: Invsy) -> None:
        chat = client.projects.users.chats.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            content="Hello, this is a message.",
            role="user",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Invsy) -> None:
        response = client.projects.users.chats.with_raw_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            content="Hello, this is a message.",
            role="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Invsy) -> None:
        with client.projects.users.chats.with_streaming_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            content="Hello, this is a message.",
            role="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                content="Hello, this is a message.",
                role="user",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
                content="Hello, this is a message.",
                role="user",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.projects.users.chats.with_raw_response.update(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                content="Hello, this is a message.",
                role="user",
            )

    @parametrize
    def test_method_list(self, client: Invsy) -> None:
        chat = client.projects.users.chats.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )
        assert_matches_type(Chats, chat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Invsy) -> None:
        response = client.projects.users.chats.with_raw_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chats, chat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Invsy) -> None:
        with client.projects.users.chats.with_streaming_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chats, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Invsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.chats.with_raw_response.list(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.chats.with_raw_response.list(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
            )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.projects.users.chats.create(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            body={
                "share_path": "/custom/path",
                "group_id": "group123",
            },
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInvsy) -> None:
        response = await async_client.projects.users.chats.with_raw_response.create(
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
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInvsy) -> None:
        async with async_client.projects.users.chats.with_streaming_response.create(
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
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.create(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.create(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                body={
                    "share_path": "/custom/path",
                    "group_id": "group123",
                },
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.projects.users.chats.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInvsy) -> None:
        response = await async_client.projects.users.chats.with_raw_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInvsy) -> None:
        async with async_client.projects.users.chats.with_streaming_response.retrieve(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.retrieve(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.retrieve(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.projects.users.chats.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            content="Hello, this is a message.",
            role="user",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInvsy) -> None:
        response = await async_client.projects.users.chats.with_raw_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            content="Hello, this is a message.",
            role="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInvsy) -> None:
        async with async_client.projects.users.chats.with_streaming_response.update(
            chat_id="1febfa740898c02b25897949bf6961ad",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            content="Hello, this is a message.",
            role="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                content="Hello, this is a message.",
                role="user",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.update(
                chat_id="1febfa740898c02b25897949bf6961ad",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="",
                content="Hello, this is a message.",
                role="user",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.update(
                chat_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                content="Hello, this is a message.",
                role="user",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncInvsy) -> None:
        chat = await async_client.projects.users.chats.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )
        assert_matches_type(Chats, chat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInvsy) -> None:
        response = await async_client.projects.users.chats.with_raw_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chats, chat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInvsy) -> None:
        async with async_client.projects.users.chats.with_streaming_response.list(
            user_id="3db648cbb7f933aeb705b821c47c0e39",
            project_id="7240303bcfc8a079bf67c2caa08b5d29",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chats, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncInvsy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.list(
                user_id="3db648cbb7f933aeb705b821c47c0e39",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.chats.with_raw_response.list(
                user_id="",
                project_id="7240303bcfc8a079bf67c2caa08b5d29",
            )
