# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from obp_api import ObpAPI, AsyncObpAPI
from obp_api._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactionRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/transaction-request-types/CARD/transaction-requests").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        transaction_request = client.transaction_requests.create(
            body={},
        )
        assert transaction_request.is_closed
        assert transaction_request.json() == {"foo": "bar"}
        assert cast(Any, transaction_request.is_closed) is True
        assert isinstance(transaction_request, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/transaction-request-types/CARD/transaction-requests").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        transaction_request = client.transaction_requests.with_raw_response.create(
            body={},
        )

        assert transaction_request.is_closed is True
        assert transaction_request.http_request.headers.get("X-Stainless-Lang") == "python"
        assert transaction_request.json() == {"foo": "bar"}
        assert isinstance(transaction_request, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/transaction-request-types/CARD/transaction-requests").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.transaction_requests.with_streaming_response.create(
            body={},
        ) as transaction_request:
            assert not transaction_request.is_closed
            assert transaction_request.http_request.headers.get("X-Stainless-Lang") == "python"

            assert transaction_request.json() == {"foo": "bar"}
            assert cast(Any, transaction_request.is_closed) is True
            assert isinstance(transaction_request, StreamedBinaryAPIResponse)

        assert cast(Any, transaction_request.is_closed) is True


class TestAsyncTransactionRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/transaction-request-types/CARD/transaction-requests").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        transaction_request = await async_client.transaction_requests.create(
            body={},
        )
        assert transaction_request.is_closed
        assert await transaction_request.json() == {"foo": "bar"}
        assert cast(Any, transaction_request.is_closed) is True
        assert isinstance(transaction_request, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/transaction-request-types/CARD/transaction-requests").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        transaction_request = await async_client.transaction_requests.with_raw_response.create(
            body={},
        )

        assert transaction_request.is_closed is True
        assert transaction_request.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await transaction_request.json() == {"foo": "bar"}
        assert isinstance(transaction_request, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/transaction-request-types/CARD/transaction-requests").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.transaction_requests.with_streaming_response.create(
            body={},
        ) as transaction_request:
            assert not transaction_request.is_closed
            assert transaction_request.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await transaction_request.json() == {"foo": "bar"}
            assert cast(Any, transaction_request.is_closed) is True
            assert isinstance(transaction_request, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, transaction_request.is_closed) is True
