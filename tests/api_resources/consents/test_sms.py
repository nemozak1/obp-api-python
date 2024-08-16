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


class TestSMS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/my/consents/SMS").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        sms = client.consents.sms.create(
            bank_id="BANK_ID",
            body={},
        )
        assert sms.is_closed
        assert sms.json() == {"foo": "bar"}
        assert cast(Any, sms.is_closed) is True
        assert isinstance(sms, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/my/consents/SMS").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        sms = client.consents.sms.with_raw_response.create(
            bank_id="BANK_ID",
            body={},
        )

        assert sms.is_closed is True
        assert sms.http_request.headers.get("X-Stainless-Lang") == "python"
        assert sms.json() == {"foo": "bar"}
        assert isinstance(sms, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/my/consents/SMS").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.consents.sms.with_streaming_response.create(
            bank_id="BANK_ID",
            body={},
        ) as sms:
            assert not sms.is_closed
            assert sms.http_request.headers.get("X-Stainless-Lang") == "python"

            assert sms.json() == {"foo": "bar"}
            assert cast(Any, sms.is_closed) is True
            assert isinstance(sms, StreamedBinaryAPIResponse)

        assert cast(Any, sms.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.consents.sms.with_raw_response.create(
                bank_id="",
                body={},
            )


class TestAsyncSMS:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/my/consents/SMS").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        sms = await async_client.consents.sms.create(
            bank_id="BANK_ID",
            body={},
        )
        assert sms.is_closed
        assert await sms.json() == {"foo": "bar"}
        assert cast(Any, sms.is_closed) is True
        assert isinstance(sms, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/my/consents/SMS").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        sms = await async_client.consents.sms.with_raw_response.create(
            bank_id="BANK_ID",
            body={},
        )

        assert sms.is_closed is True
        assert sms.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await sms.json() == {"foo": "bar"}
        assert isinstance(sms, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/my/consents/SMS").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.consents.sms.with_streaming_response.create(
            bank_id="BANK_ID",
            body={},
        ) as sms:
            assert not sms.is_closed
            assert sms.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await sms.json() == {"foo": "bar"}
            assert cast(Any, sms.is_closed) is True
            assert isinstance(sms, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, sms.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.consents.sms.with_raw_response.create(
                bank_id="",
                body={},
            )
