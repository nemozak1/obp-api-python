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


class TestAttribute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/customers/CUSTOMER_ID/attribute").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        attribute = client.customers.attribute.create(
            customer_id="CUSTOMER_ID",
            bank_id="BANK_ID",
            body={},
        )
        assert attribute.is_closed
        assert attribute.json() == {"foo": "bar"}
        assert cast(Any, attribute.is_closed) is True
        assert isinstance(attribute, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/customers/CUSTOMER_ID/attribute").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        attribute = client.customers.attribute.with_raw_response.create(
            customer_id="CUSTOMER_ID",
            bank_id="BANK_ID",
            body={},
        )

        assert attribute.is_closed is True
        assert attribute.http_request.headers.get("X-Stainless-Lang") == "python"
        assert attribute.json() == {"foo": "bar"}
        assert isinstance(attribute, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/customers/CUSTOMER_ID/attribute").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.customers.attribute.with_streaming_response.create(
            customer_id="CUSTOMER_ID",
            bank_id="BANK_ID",
            body={},
        ) as attribute:
            assert not attribute.is_closed
            assert attribute.http_request.headers.get("X-Stainless-Lang") == "python"

            assert attribute.json() == {"foo": "bar"}
            assert cast(Any, attribute.is_closed) is True
            assert isinstance(attribute, StreamedBinaryAPIResponse)

        assert cast(Any, attribute.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.customers.attribute.with_raw_response.create(
                customer_id="CUSTOMER_ID",
                bank_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.attribute.with_raw_response.create(
                customer_id="",
                bank_id="BANK_ID",
                body={},
            )


class TestAsyncAttribute:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/customers/CUSTOMER_ID/attribute").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        attribute = await async_client.customers.attribute.create(
            customer_id="CUSTOMER_ID",
            bank_id="BANK_ID",
            body={},
        )
        assert attribute.is_closed
        assert await attribute.json() == {"foo": "bar"}
        assert cast(Any, attribute.is_closed) is True
        assert isinstance(attribute, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/customers/CUSTOMER_ID/attribute").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        attribute = await async_client.customers.attribute.with_raw_response.create(
            customer_id="CUSTOMER_ID",
            bank_id="BANK_ID",
            body={},
        )

        assert attribute.is_closed is True
        assert attribute.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await attribute.json() == {"foo": "bar"}
        assert isinstance(attribute, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/customers/CUSTOMER_ID/attribute").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.customers.attribute.with_streaming_response.create(
            customer_id="CUSTOMER_ID",
            bank_id="BANK_ID",
            body={},
        ) as attribute:
            assert not attribute.is_closed
            assert attribute.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await attribute.json() == {"foo": "bar"}
            assert cast(Any, attribute.is_closed) is True
            assert isinstance(attribute, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, attribute.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.customers.attribute.with_raw_response.create(
                customer_id="CUSTOMER_ID",
                bank_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.attribute.with_raw_response.create(
                customer_id="",
                bank_id="BANK_ID",
                body={},
            )
