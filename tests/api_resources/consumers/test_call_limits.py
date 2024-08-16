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


class TestCallLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        call_limit = client.consumers.call_limits.retrieve(
            "CONSUMER_ID",
        )
        assert call_limit.is_closed
        assert call_limit.json() == {"foo": "bar"}
        assert cast(Any, call_limit.is_closed) is True
        assert isinstance(call_limit, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        call_limit = client.consumers.call_limits.with_raw_response.retrieve(
            "CONSUMER_ID",
        )

        assert call_limit.is_closed is True
        assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"
        assert call_limit.json() == {"foo": "bar"}
        assert isinstance(call_limit, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.consumers.call_limits.with_streaming_response.retrieve(
            "CONSUMER_ID",
        ) as call_limit:
            assert not call_limit.is_closed
            assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"

            assert call_limit.json() == {"foo": "bar"}
            assert cast(Any, call_limit.is_closed) is True
            assert isinstance(call_limit, StreamedBinaryAPIResponse)

        assert cast(Any, call_limit.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            client.consumers.call_limits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        call_limit = client.consumers.call_limits.update(
            consumer_id="CONSUMER_ID",
            body={},
        )
        assert call_limit.is_closed
        assert call_limit.json() == {"foo": "bar"}
        assert cast(Any, call_limit.is_closed) is True
        assert isinstance(call_limit, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        call_limit = client.consumers.call_limits.with_raw_response.update(
            consumer_id="CONSUMER_ID",
            body={},
        )

        assert call_limit.is_closed is True
        assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"
        assert call_limit.json() == {"foo": "bar"}
        assert isinstance(call_limit, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.consumers.call_limits.with_streaming_response.update(
            consumer_id="CONSUMER_ID",
            body={},
        ) as call_limit:
            assert not call_limit.is_closed
            assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"

            assert call_limit.json() == {"foo": "bar"}
            assert cast(Any, call_limit.is_closed) is True
            assert isinstance(call_limit, StreamedBinaryAPIResponse)

        assert cast(Any, call_limit.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            client.consumers.call_limits.with_raw_response.update(
                consumer_id="",
                body={},
            )


class TestAsyncCallLimits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        call_limit = await async_client.consumers.call_limits.retrieve(
            "CONSUMER_ID",
        )
        assert call_limit.is_closed
        assert await call_limit.json() == {"foo": "bar"}
        assert cast(Any, call_limit.is_closed) is True
        assert isinstance(call_limit, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        call_limit = await async_client.consumers.call_limits.with_raw_response.retrieve(
            "CONSUMER_ID",
        )

        assert call_limit.is_closed is True
        assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await call_limit.json() == {"foo": "bar"}
        assert isinstance(call_limit, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.consumers.call_limits.with_streaming_response.retrieve(
            "CONSUMER_ID",
        ) as call_limit:
            assert not call_limit.is_closed
            assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await call_limit.json() == {"foo": "bar"}
            assert cast(Any, call_limit.is_closed) is True
            assert isinstance(call_limit, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, call_limit.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            await async_client.consumers.call_limits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        call_limit = await async_client.consumers.call_limits.update(
            consumer_id="CONSUMER_ID",
            body={},
        )
        assert call_limit.is_closed
        assert await call_limit.json() == {"foo": "bar"}
        assert cast(Any, call_limit.is_closed) is True
        assert isinstance(call_limit, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        call_limit = await async_client.consumers.call_limits.with_raw_response.update(
            consumer_id="CONSUMER_ID",
            body={},
        )

        assert call_limit.is_closed is True
        assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await call_limit.json() == {"foo": "bar"}
        assert isinstance(call_limit, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/consumers/CONSUMER_ID/consumer/call-limits").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.consumers.call_limits.with_streaming_response.update(
            consumer_id="CONSUMER_ID",
            body={},
        ) as call_limit:
            assert not call_limit.is_closed
            assert call_limit.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await call_limit.json() == {"foo": "bar"}
            assert cast(Any, call_limit.is_closed) is True
            assert isinstance(call_limit, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, call_limit.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            await async_client.consumers.call_limits.with_raw_response.update(
                consumer_id="",
                body={},
            )
