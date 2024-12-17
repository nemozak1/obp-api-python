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


class TestConsumers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/dynamic-registration/consumers").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        consumer = client.dynamic_registration.consumers.create(
            jwt="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXNjcmlwdGlvbiI6IlRQUCBkZXNjcmlwdGlvbiJ9.c5gPPsyUmnVW774y7h2xyLXg0wdtu25nbU2AvOmyzcWa7JTdCKuuy3CblxueGwqYkQDDQIya1Qny4blyAvh_a1Q28LgzEKBcH7Em9FZXerhkvR9v4FWbCC5AgNLdQ7sR8-rUQdShmJcGDKdVmsZjuO4XhY2Zx0nFnkcvYfsU9bccoAvkKpVJATXzwBqdoEOuFlplnbxsMH1wWbAd3hbcPPWTdvO43xavNZTB5ybgrXVDEYjw8D-98_ZkqxS0vfvhJ4cGefHViaFzp6zXm7msdBpcE__O9rFbdl9Gvup_bsMbrHJioIrmc2d15Yc-tTNTF9J4qjD_lNxMRlx5o2TZEw",
        )
        assert consumer.is_closed
        assert consumer.json() == {"foo": "bar"}
        assert cast(Any, consumer.is_closed) is True
        assert isinstance(consumer, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/dynamic-registration/consumers").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        consumer = client.dynamic_registration.consumers.with_raw_response.create(
            jwt="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXNjcmlwdGlvbiI6IlRQUCBkZXNjcmlwdGlvbiJ9.c5gPPsyUmnVW774y7h2xyLXg0wdtu25nbU2AvOmyzcWa7JTdCKuuy3CblxueGwqYkQDDQIya1Qny4blyAvh_a1Q28LgzEKBcH7Em9FZXerhkvR9v4FWbCC5AgNLdQ7sR8-rUQdShmJcGDKdVmsZjuO4XhY2Zx0nFnkcvYfsU9bccoAvkKpVJATXzwBqdoEOuFlplnbxsMH1wWbAd3hbcPPWTdvO43xavNZTB5ybgrXVDEYjw8D-98_ZkqxS0vfvhJ4cGefHViaFzp6zXm7msdBpcE__O9rFbdl9Gvup_bsMbrHJioIrmc2d15Yc-tTNTF9J4qjD_lNxMRlx5o2TZEw",
        )

        assert consumer.is_closed is True
        assert consumer.http_request.headers.get("X-Stainless-Lang") == "python"
        assert consumer.json() == {"foo": "bar"}
        assert isinstance(consumer, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/dynamic-registration/consumers").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.dynamic_registration.consumers.with_streaming_response.create(
            jwt="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXNjcmlwdGlvbiI6IlRQUCBkZXNjcmlwdGlvbiJ9.c5gPPsyUmnVW774y7h2xyLXg0wdtu25nbU2AvOmyzcWa7JTdCKuuy3CblxueGwqYkQDDQIya1Qny4blyAvh_a1Q28LgzEKBcH7Em9FZXerhkvR9v4FWbCC5AgNLdQ7sR8-rUQdShmJcGDKdVmsZjuO4XhY2Zx0nFnkcvYfsU9bccoAvkKpVJATXzwBqdoEOuFlplnbxsMH1wWbAd3hbcPPWTdvO43xavNZTB5ybgrXVDEYjw8D-98_ZkqxS0vfvhJ4cGefHViaFzp6zXm7msdBpcE__O9rFbdl9Gvup_bsMbrHJioIrmc2d15Yc-tTNTF9J4qjD_lNxMRlx5o2TZEw",
        ) as consumer:
            assert not consumer.is_closed
            assert consumer.http_request.headers.get("X-Stainless-Lang") == "python"

            assert consumer.json() == {"foo": "bar"}
            assert cast(Any, consumer.is_closed) is True
            assert isinstance(consumer, StreamedBinaryAPIResponse)

        assert cast(Any, consumer.is_closed) is True


class TestAsyncConsumers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/dynamic-registration/consumers").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        consumer = await async_client.dynamic_registration.consumers.create(
            jwt="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXNjcmlwdGlvbiI6IlRQUCBkZXNjcmlwdGlvbiJ9.c5gPPsyUmnVW774y7h2xyLXg0wdtu25nbU2AvOmyzcWa7JTdCKuuy3CblxueGwqYkQDDQIya1Qny4blyAvh_a1Q28LgzEKBcH7Em9FZXerhkvR9v4FWbCC5AgNLdQ7sR8-rUQdShmJcGDKdVmsZjuO4XhY2Zx0nFnkcvYfsU9bccoAvkKpVJATXzwBqdoEOuFlplnbxsMH1wWbAd3hbcPPWTdvO43xavNZTB5ybgrXVDEYjw8D-98_ZkqxS0vfvhJ4cGefHViaFzp6zXm7msdBpcE__O9rFbdl9Gvup_bsMbrHJioIrmc2d15Yc-tTNTF9J4qjD_lNxMRlx5o2TZEw",
        )
        assert consumer.is_closed
        assert await consumer.json() == {"foo": "bar"}
        assert cast(Any, consumer.is_closed) is True
        assert isinstance(consumer, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/dynamic-registration/consumers").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        consumer = await async_client.dynamic_registration.consumers.with_raw_response.create(
            jwt="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXNjcmlwdGlvbiI6IlRQUCBkZXNjcmlwdGlvbiJ9.c5gPPsyUmnVW774y7h2xyLXg0wdtu25nbU2AvOmyzcWa7JTdCKuuy3CblxueGwqYkQDDQIya1Qny4blyAvh_a1Q28LgzEKBcH7Em9FZXerhkvR9v4FWbCC5AgNLdQ7sR8-rUQdShmJcGDKdVmsZjuO4XhY2Zx0nFnkcvYfsU9bccoAvkKpVJATXzwBqdoEOuFlplnbxsMH1wWbAd3hbcPPWTdvO43xavNZTB5ybgrXVDEYjw8D-98_ZkqxS0vfvhJ4cGefHViaFzp6zXm7msdBpcE__O9rFbdl9Gvup_bsMbrHJioIrmc2d15Yc-tTNTF9J4qjD_lNxMRlx5o2TZEw",
        )

        assert consumer.is_closed is True
        assert consumer.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await consumer.json() == {"foo": "bar"}
        assert isinstance(consumer, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/dynamic-registration/consumers").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.dynamic_registration.consumers.with_streaming_response.create(
            jwt="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXNjcmlwdGlvbiI6IlRQUCBkZXNjcmlwdGlvbiJ9.c5gPPsyUmnVW774y7h2xyLXg0wdtu25nbU2AvOmyzcWa7JTdCKuuy3CblxueGwqYkQDDQIya1Qny4blyAvh_a1Q28LgzEKBcH7Em9FZXerhkvR9v4FWbCC5AgNLdQ7sR8-rUQdShmJcGDKdVmsZjuO4XhY2Zx0nFnkcvYfsU9bccoAvkKpVJATXzwBqdoEOuFlplnbxsMH1wWbAd3hbcPPWTdvO43xavNZTB5ybgrXVDEYjw8D-98_ZkqxS0vfvhJ4cGefHViaFzp6zXm7msdBpcE__O9rFbdl9Gvup_bsMbrHJioIrmc2d15Yc-tTNTF9J4qjD_lNxMRlx5o2TZEw",
        ) as consumer:
            assert not consumer.is_closed
            assert consumer.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await consumer.json() == {"foo": "bar"}
            assert cast(Any, consumer.is_closed) is True
            assert isinstance(consumer, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, consumer.is_closed) is True
