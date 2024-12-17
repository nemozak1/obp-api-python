# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from obp_api import ObpAPI, AsyncObpAPI
from obp_api._utils import parse_date
from obp_api._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = client.cards.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )
        assert card.is_closed
        assert card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = client.cards.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
            collected=parse_date("2019-12-27"),
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
        )
        assert card.is_closed
        assert card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = client.cards.with_raw_response.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert card.json() == {"foo": "bar"}
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cards.with_streaming_response.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, StreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.cards.with_raw_response.create(
                bank_id="",
                account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
                allows=["string"],
                brand="Visa",
                card_number="364435172576215",
                card_type="Credit",
                customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
                enabled=True,
                expires_date=parse_date("2019-12-27"),
                issue_number="1",
                name_on_card="SusanSmith",
                networks=["string"],
                pin_reset=[
                    {
                        "reason_requested": "GOOD_SECURITY_PRACTICE",
                        "requested_date": parse_date("2019-12-27"),
                    }
                ],
                serial_number="1324234",
                technology="technology1",
                valid_from_date=parse_date("2019-12-27"),
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = client.cards.retrieve(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )
        assert card.is_closed
        assert card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = client.cards.with_raw_response.retrieve(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert card.json() == {"foo": "bar"}
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cards.with_streaming_response.retrieve(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, StreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.cards.with_raw_response.retrieve(
                card_id="CARD_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.retrieve(
                card_id="",
                bank_id="BANK_ID",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = client.cards.update(
            card_id="CARD_ID",
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            card_type="Credit",
            collected=parse_date("2019-12-27"),
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )
        assert card.is_closed
        assert card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = client.cards.with_raw_response.update(
            card_id="CARD_ID",
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            card_type="Credit",
            collected=parse_date("2019-12-27"),
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert card.json() == {"foo": "bar"}
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cards.with_streaming_response.update(
            card_id="CARD_ID",
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            card_type="Credit",
            collected=parse_date("2019-12-27"),
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, StreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.cards.with_raw_response.update(
                card_id="CARD_ID",
                bank_id="",
                account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
                allows=["string"],
                card_type="Credit",
                collected=parse_date("2019-12-27"),
                customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
                enabled=True,
                expires_date=parse_date("2019-12-27"),
                issue_number="1",
                name_on_card="SusanSmith",
                networks=["string"],
                pin_reset=[
                    {
                        "reason_requested": "GOOD_SECURITY_PRACTICE",
                        "requested_date": parse_date("2019-12-27"),
                    }
                ],
                posted=parse_date("2019-12-27"),
                replacement={
                    "reason_requested": "RENEW",
                    "requested_date": parse_date("2019-12-27"),
                },
                serial_number="1324234",
                technology="technology1",
                valid_from_date=parse_date("2019-12-27"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.update(
                card_id="",
                bank_id="BANK_ID",
                account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
                allows=["string"],
                card_type="Credit",
                collected=parse_date("2019-12-27"),
                customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
                enabled=True,
                expires_date=parse_date("2019-12-27"),
                issue_number="1",
                name_on_card="SusanSmith",
                networks=["string"],
                pin_reset=[
                    {
                        "reason_requested": "GOOD_SECURITY_PRACTICE",
                        "requested_date": parse_date("2019-12-27"),
                    }
                ],
                posted=parse_date("2019-12-27"),
                replacement={
                    "reason_requested": "RENEW",
                    "requested_date": parse_date("2019-12-27"),
                },
                serial_number="1324234",
                technology="technology1",
                valid_from_date=parse_date("2019-12-27"),
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = client.cards.list(
            "BANK_ID",
        )
        assert card.is_closed
        assert card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = client.cards.with_raw_response.list(
            "BANK_ID",
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert card.json() == {"foo": "bar"}
        assert isinstance(card, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cards.with_streaming_response.list(
            "BANK_ID",
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, StreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.cards.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: ObpAPI) -> None:
        card = client.cards.delete(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )
        assert card is None

    @parametrize
    def test_raw_response_delete(self, client: ObpAPI) -> None:
        response = client.cards.with_raw_response.delete(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert card is None

    @parametrize
    def test_streaming_response_delete(self, client: ObpAPI) -> None:
        with client.cards.with_streaming_response.delete(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert card is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.cards.with_raw_response.delete(
                card_id="CARD_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.delete(
                card_id="",
                bank_id="BANK_ID",
            )


class TestAsyncCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = await async_client.cards.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )
        assert card.is_closed
        assert await card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = await async_client.cards.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
            collected=parse_date("2019-12-27"),
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
        )
        assert card.is_closed
        assert await card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = await async_client.cards.with_raw_response.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await card.json() == {"foo": "bar"}
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cards.with_streaming_response.create(
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            brand="Visa",
            card_number="364435172576215",
            card_type="Credit",
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.cards.with_raw_response.create(
                bank_id="",
                account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
                allows=["string"],
                brand="Visa",
                card_number="364435172576215",
                card_type="Credit",
                customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
                enabled=True,
                expires_date=parse_date("2019-12-27"),
                issue_number="1",
                name_on_card="SusanSmith",
                networks=["string"],
                pin_reset=[
                    {
                        "reason_requested": "GOOD_SECURITY_PRACTICE",
                        "requested_date": parse_date("2019-12-27"),
                    }
                ],
                serial_number="1324234",
                technology="technology1",
                valid_from_date=parse_date("2019-12-27"),
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = await async_client.cards.retrieve(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )
        assert card.is_closed
        assert await card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = await async_client.cards.with_raw_response.retrieve(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await card.json() == {"foo": "bar"}
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cards.with_streaming_response.retrieve(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.cards.with_raw_response.retrieve(
                card_id="CARD_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.with_raw_response.retrieve(
                card_id="",
                bank_id="BANK_ID",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = await async_client.cards.update(
            card_id="CARD_ID",
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            card_type="Credit",
            collected=parse_date("2019-12-27"),
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )
        assert card.is_closed
        assert await card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = await async_client.cards.with_raw_response.update(
            card_id="CARD_ID",
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            card_type="Credit",
            collected=parse_date("2019-12-27"),
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await card.json() == {"foo": "bar"}
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/banks/BANK_ID/cards/CARD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cards.with_streaming_response.update(
            card_id="CARD_ID",
            bank_id="BANK_ID",
            account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
            allows=["string"],
            card_type="Credit",
            collected=parse_date("2019-12-27"),
            customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
            enabled=True,
            expires_date=parse_date("2019-12-27"),
            issue_number="1",
            name_on_card="SusanSmith",
            networks=["string"],
            pin_reset=[
                {
                    "reason_requested": "GOOD_SECURITY_PRACTICE",
                    "requested_date": parse_date("2019-12-27"),
                }
            ],
            posted=parse_date("2019-12-27"),
            replacement={
                "reason_requested": "RENEW",
                "requested_date": parse_date("2019-12-27"),
            },
            serial_number="1324234",
            technology="technology1",
            valid_from_date=parse_date("2019-12-27"),
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.cards.with_raw_response.update(
                card_id="CARD_ID",
                bank_id="",
                account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
                allows=["string"],
                card_type="Credit",
                collected=parse_date("2019-12-27"),
                customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
                enabled=True,
                expires_date=parse_date("2019-12-27"),
                issue_number="1",
                name_on_card="SusanSmith",
                networks=["string"],
                pin_reset=[
                    {
                        "reason_requested": "GOOD_SECURITY_PRACTICE",
                        "requested_date": parse_date("2019-12-27"),
                    }
                ],
                posted=parse_date("2019-12-27"),
                replacement={
                    "reason_requested": "RENEW",
                    "requested_date": parse_date("2019-12-27"),
                },
                serial_number="1324234",
                technology="technology1",
                valid_from_date=parse_date("2019-12-27"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.with_raw_response.update(
                card_id="",
                bank_id="BANK_ID",
                account_id="8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
                allows=["string"],
                card_type="Credit",
                collected=parse_date("2019-12-27"),
                customer_id="7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
                enabled=True,
                expires_date=parse_date("2019-12-27"),
                issue_number="1",
                name_on_card="SusanSmith",
                networks=["string"],
                pin_reset=[
                    {
                        "reason_requested": "GOOD_SECURITY_PRACTICE",
                        "requested_date": parse_date("2019-12-27"),
                    }
                ],
                posted=parse_date("2019-12-27"),
                replacement={
                    "reason_requested": "RENEW",
                    "requested_date": parse_date("2019-12-27"),
                },
                serial_number="1324234",
                technology="technology1",
                valid_from_date=parse_date("2019-12-27"),
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        card = await async_client.cards.list(
            "BANK_ID",
        )
        assert card.is_closed
        assert await card.json() == {"foo": "bar"}
        assert cast(Any, card.is_closed) is True
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        card = await async_client.cards.with_raw_response.list(
            "BANK_ID",
        )

        assert card.is_closed is True
        assert card.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await card.json() == {"foo": "bar"}
        assert isinstance(card, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/cards").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cards.with_streaming_response.list(
            "BANK_ID",
        ) as card:
            assert not card.is_closed
            assert card.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await card.json() == {"foo": "bar"}
            assert cast(Any, card.is_closed) is True
            assert isinstance(card, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, card.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.cards.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncObpAPI) -> None:
        card = await async_client.cards.delete(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )
        assert card is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncObpAPI) -> None:
        response = await async_client.cards.with_raw_response.delete(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert card is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncObpAPI) -> None:
        async with async_client.cards.with_streaming_response.delete(
            card_id="CARD_ID",
            bank_id="BANK_ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert card is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.cards.with_raw_response.delete(
                card_id="CARD_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.with_raw_response.delete(
                card_id="",
                bank_id="BANK_ID",
            )
