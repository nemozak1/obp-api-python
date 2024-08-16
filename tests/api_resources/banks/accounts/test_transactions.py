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


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/my/banks/BANK_ID/accounts/ACCOUNT_ID/transactions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        transaction = client.banks.accounts.transactions.list(
            account_id="ACCOUNT_ID",
            bank_id="BANK_ID",
        )
        assert transaction.is_closed
        assert transaction.json() == {"foo": "bar"}
        assert cast(Any, transaction.is_closed) is True
        assert isinstance(transaction, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/my/banks/BANK_ID/accounts/ACCOUNT_ID/transactions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        transaction = client.banks.accounts.transactions.with_raw_response.list(
            account_id="ACCOUNT_ID",
            bank_id="BANK_ID",
        )

        assert transaction.is_closed is True
        assert transaction.http_request.headers.get("X-Stainless-Lang") == "python"
        assert transaction.json() == {"foo": "bar"}
        assert isinstance(transaction, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/my/banks/BANK_ID/accounts/ACCOUNT_ID/transactions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.banks.accounts.transactions.with_streaming_response.list(
            account_id="ACCOUNT_ID",
            bank_id="BANK_ID",
        ) as transaction:
            assert not transaction.is_closed
            assert transaction.http_request.headers.get("X-Stainless-Lang") == "python"

            assert transaction.json() == {"foo": "bar"}
            assert cast(Any, transaction.is_closed) is True
            assert isinstance(transaction, StreamedBinaryAPIResponse)

        assert cast(Any, transaction.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.banks.accounts.transactions.with_raw_response.list(
                account_id="ACCOUNT_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.banks.accounts.transactions.with_raw_response.list(
                account_id="",
                bank_id="BANK_ID",
            )


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/my/banks/BANK_ID/accounts/ACCOUNT_ID/transactions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        transaction = await async_client.banks.accounts.transactions.list(
            account_id="ACCOUNT_ID",
            bank_id="BANK_ID",
        )
        assert transaction.is_closed
        assert await transaction.json() == {"foo": "bar"}
        assert cast(Any, transaction.is_closed) is True
        assert isinstance(transaction, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/my/banks/BANK_ID/accounts/ACCOUNT_ID/transactions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        transaction = await async_client.banks.accounts.transactions.with_raw_response.list(
            account_id="ACCOUNT_ID",
            bank_id="BANK_ID",
        )

        assert transaction.is_closed is True
        assert transaction.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await transaction.json() == {"foo": "bar"}
        assert isinstance(transaction, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/my/banks/BANK_ID/accounts/ACCOUNT_ID/transactions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.banks.accounts.transactions.with_streaming_response.list(
            account_id="ACCOUNT_ID",
            bank_id="BANK_ID",
        ) as transaction:
            assert not transaction.is_closed
            assert transaction.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await transaction.json() == {"foo": "bar"}
            assert cast(Any, transaction.is_closed) is True
            assert isinstance(transaction, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, transaction.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.banks.accounts.transactions.with_raw_response.list(
                account_id="ACCOUNT_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.banks.accounts.transactions.with_raw_response.list(
                account_id="",
                bank_id="BANK_ID",
            )
