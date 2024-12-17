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


class TestAtms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        atm = client.banks.atms.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )
        assert atm.is_closed
        assert atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        atm = client.banks.atms.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            id="atme-9a0f-4bfa-b30b-9003aa467f51",
        )
        assert atm.is_closed
        assert atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        atm = client.banks.atms.with_raw_response.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert atm.json() == {"foo": "bar"}
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.banks.atms.with_streaming_response.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, StreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_bank_id` but received ''"):
            client.banks.atms.with_raw_response.create(
                path_bank_id="",
                accessibility_features=["string"],
                address={
                    "city": "Berlin",
                    "country_code": "DE",
                    "county": "",
                    "line_1": "No 1 the Road",
                    "line_2": "The Place",
                    "line_3": "The Hill",
                    "postcode": "13359",
                    "state": "Brandenburg",
                },
                atm_type="",
                balance_inquiry_fee="",
                body_bank_id="gh.29.uk",
                branch_identification="",
                cash_withdrawal_international_fee="",
                cash_withdrawal_national_fee="",
                friday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                has_deposit_capability="false",
                is_accessible="false",
                located_at="",
                location={
                    "latitude": 11.45,
                    "longitude": 11.45,
                },
                location_categories=["string"],
                meta={
                    "license": {
                        "id": "ODbL-1.0",
                        "name": "Open Database License",
                    }
                },
                minimum_withdrawal="5",
                monday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                more_info="More information about this fee",
                name="Atm by the Lake",
                notes=["string"],
                phone="",
                saturday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                services=["string"],
                site_identification="",
                site_name="",
                sunday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                supported_currencies=["string"],
                supported_languages=["string"],
                thursday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                tuesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                wednesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        atm = client.banks.atms.retrieve(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )
        assert atm.is_closed
        assert atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        atm = client.banks.atms.with_raw_response.retrieve(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert atm.json() == {"foo": "bar"}
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.banks.atms.with_streaming_response.retrieve(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, StreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.banks.atms.with_raw_response.retrieve(
                atm_id="ATM_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atm_id` but received ''"):
            client.banks.atms.with_raw_response.retrieve(
                atm_id="",
                bank_id="BANK_ID",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        atm = client.banks.atms.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )
        assert atm.is_closed
        assert atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        atm = client.banks.atms.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            id="atme-9a0f-4bfa-b30b-9003aa467f51",
            attributes=[
                {
                    "atm_attribute_id": "xxaf2a-9a0f-4bfa-b30b-9003aa467f51",
                    "atm_id": "atme-9a0f-4bfa-b30b-9003aa467f51",
                    "bank_id": "gh.29.uk",
                    "name": "ACCOUNT_MANAGEMENT_FEE",
                    "type": "",
                    "value": "5987953",
                    "is_active": False,
                }
            ],
        )
        assert atm.is_closed
        assert atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        atm = client.banks.atms.with_raw_response.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert atm.json() == {"foo": "bar"}
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.banks.atms.with_streaming_response.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, StreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_bank_id` but received ''"):
            client.banks.atms.with_raw_response.update(
                atm_id="ATM_ID",
                path_bank_id="",
                accessibility_features=["string"],
                address={
                    "city": "Berlin",
                    "country_code": "DE",
                    "county": "",
                    "line_1": "No 1 the Road",
                    "line_2": "The Place",
                    "line_3": "The Hill",
                    "postcode": "13359",
                    "state": "Brandenburg",
                },
                atm_type="",
                balance_inquiry_fee="",
                body_bank_id="gh.29.uk",
                branch_identification="",
                cash_withdrawal_international_fee="",
                cash_withdrawal_national_fee="",
                friday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                has_deposit_capability="false",
                is_accessible="false",
                located_at="",
                location={
                    "latitude": 11.45,
                    "longitude": 11.45,
                },
                location_categories=["string"],
                meta={
                    "license": {
                        "id": "ODbL-1.0",
                        "name": "Open Database License",
                    }
                },
                minimum_withdrawal="5",
                monday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                more_info="More information about this fee",
                name="Atm by the Lake",
                notes=["string"],
                phone="",
                saturday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                services=["string"],
                site_identification="",
                site_name="",
                sunday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                supported_currencies=["string"],
                supported_languages=["string"],
                thursday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                tuesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                wednesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atm_id` but received ''"):
            client.banks.atms.with_raw_response.update(
                atm_id="",
                path_bank_id="BANK_ID",
                accessibility_features=["string"],
                address={
                    "city": "Berlin",
                    "country_code": "DE",
                    "county": "",
                    "line_1": "No 1 the Road",
                    "line_2": "The Place",
                    "line_3": "The Hill",
                    "postcode": "13359",
                    "state": "Brandenburg",
                },
                atm_type="",
                balance_inquiry_fee="",
                body_bank_id="gh.29.uk",
                branch_identification="",
                cash_withdrawal_international_fee="",
                cash_withdrawal_national_fee="",
                friday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                has_deposit_capability="false",
                is_accessible="false",
                located_at="",
                location={
                    "latitude": 11.45,
                    "longitude": 11.45,
                },
                location_categories=["string"],
                meta={
                    "license": {
                        "id": "ODbL-1.0",
                        "name": "Open Database License",
                    }
                },
                minimum_withdrawal="5",
                monday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                more_info="More information about this fee",
                name="Atm by the Lake",
                notes=["string"],
                phone="",
                saturday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                services=["string"],
                site_identification="",
                site_name="",
                sunday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                supported_currencies=["string"],
                supported_languages=["string"],
                thursday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                tuesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                wednesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        atm = client.banks.atms.list(
            "BANK_ID",
        )
        assert atm.is_closed
        assert atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        atm = client.banks.atms.with_raw_response.list(
            "BANK_ID",
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert atm.json() == {"foo": "bar"}
        assert isinstance(atm, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.banks.atms.with_streaming_response.list(
            "BANK_ID",
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, StreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.banks.atms.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: ObpAPI) -> None:
        atm = client.banks.atms.delete(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )
        assert atm is None

    @parametrize
    def test_raw_response_delete(self, client: ObpAPI) -> None:
        response = client.banks.atms.with_raw_response.delete(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        atm = response.parse()
        assert atm is None

    @parametrize
    def test_streaming_response_delete(self, client: ObpAPI) -> None:
        with client.banks.atms.with_streaming_response.delete(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            atm = response.parse()
            assert atm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.banks.atms.with_raw_response.delete(
                atm_id="ATM_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atm_id` but received ''"):
            client.banks.atms.with_raw_response.delete(
                atm_id="",
                bank_id="BANK_ID",
            )


class TestAsyncAtms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        atm = await async_client.banks.atms.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )
        assert atm.is_closed
        assert await atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        atm = await async_client.banks.atms.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            id="atme-9a0f-4bfa-b30b-9003aa467f51",
        )
        assert atm.is_closed
        assert await atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        atm = await async_client.banks.atms.with_raw_response.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await atm.json() == {"foo": "bar"}
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.banks.atms.with_streaming_response.create(
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_bank_id` but received ''"):
            await async_client.banks.atms.with_raw_response.create(
                path_bank_id="",
                accessibility_features=["string"],
                address={
                    "city": "Berlin",
                    "country_code": "DE",
                    "county": "",
                    "line_1": "No 1 the Road",
                    "line_2": "The Place",
                    "line_3": "The Hill",
                    "postcode": "13359",
                    "state": "Brandenburg",
                },
                atm_type="",
                balance_inquiry_fee="",
                body_bank_id="gh.29.uk",
                branch_identification="",
                cash_withdrawal_international_fee="",
                cash_withdrawal_national_fee="",
                friday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                has_deposit_capability="false",
                is_accessible="false",
                located_at="",
                location={
                    "latitude": 11.45,
                    "longitude": 11.45,
                },
                location_categories=["string"],
                meta={
                    "license": {
                        "id": "ODbL-1.0",
                        "name": "Open Database License",
                    }
                },
                minimum_withdrawal="5",
                monday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                more_info="More information about this fee",
                name="Atm by the Lake",
                notes=["string"],
                phone="",
                saturday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                services=["string"],
                site_identification="",
                site_name="",
                sunday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                supported_currencies=["string"],
                supported_languages=["string"],
                thursday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                tuesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                wednesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        atm = await async_client.banks.atms.retrieve(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )
        assert atm.is_closed
        assert await atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        atm = await async_client.banks.atms.with_raw_response.retrieve(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await atm.json() == {"foo": "bar"}
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.banks.atms.with_streaming_response.retrieve(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.banks.atms.with_raw_response.retrieve(
                atm_id="ATM_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atm_id` but received ''"):
            await async_client.banks.atms.with_raw_response.retrieve(
                atm_id="",
                bank_id="BANK_ID",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        atm = await async_client.banks.atms.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )
        assert atm.is_closed
        assert await atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        atm = await async_client.banks.atms.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            id="atme-9a0f-4bfa-b30b-9003aa467f51",
            attributes=[
                {
                    "atm_attribute_id": "xxaf2a-9a0f-4bfa-b30b-9003aa467f51",
                    "atm_id": "atme-9a0f-4bfa-b30b-9003aa467f51",
                    "bank_id": "gh.29.uk",
                    "name": "ACCOUNT_MANAGEMENT_FEE",
                    "type": "",
                    "value": "5987953",
                    "is_active": False,
                }
            ],
        )
        assert atm.is_closed
        assert await atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        atm = await async_client.banks.atms.with_raw_response.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await atm.json() == {"foo": "bar"}
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/banks/BANK_ID/atms/ATM_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.banks.atms.with_streaming_response.update(
            atm_id="ATM_ID",
            path_bank_id="BANK_ID",
            accessibility_features=["string"],
            address={
                "city": "Berlin",
                "country_code": "DE",
                "county": "",
                "line_1": "No 1 the Road",
                "line_2": "The Place",
                "line_3": "The Hill",
                "postcode": "13359",
                "state": "Brandenburg",
            },
            atm_type="",
            balance_inquiry_fee="",
            body_bank_id="gh.29.uk",
            branch_identification="",
            cash_withdrawal_international_fee="",
            cash_withdrawal_national_fee="",
            friday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            has_deposit_capability="false",
            is_accessible="false",
            located_at="",
            location={
                "latitude": 11.45,
                "longitude": 11.45,
            },
            location_categories=["string"],
            meta={
                "license": {
                    "id": "ODbL-1.0",
                    "name": "Open Database License",
                }
            },
            minimum_withdrawal="5",
            monday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            more_info="More information about this fee",
            name="Atm by the Lake",
            notes=["string"],
            phone="",
            saturday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            services=["string"],
            site_identification="",
            site_name="",
            sunday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            supported_currencies=["string"],
            supported_languages=["string"],
            thursday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            tuesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
            wednesday={
                "closing_time": "18:00",
                "opening_time": "10:00",
            },
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_bank_id` but received ''"):
            await async_client.banks.atms.with_raw_response.update(
                atm_id="ATM_ID",
                path_bank_id="",
                accessibility_features=["string"],
                address={
                    "city": "Berlin",
                    "country_code": "DE",
                    "county": "",
                    "line_1": "No 1 the Road",
                    "line_2": "The Place",
                    "line_3": "The Hill",
                    "postcode": "13359",
                    "state": "Brandenburg",
                },
                atm_type="",
                balance_inquiry_fee="",
                body_bank_id="gh.29.uk",
                branch_identification="",
                cash_withdrawal_international_fee="",
                cash_withdrawal_national_fee="",
                friday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                has_deposit_capability="false",
                is_accessible="false",
                located_at="",
                location={
                    "latitude": 11.45,
                    "longitude": 11.45,
                },
                location_categories=["string"],
                meta={
                    "license": {
                        "id": "ODbL-1.0",
                        "name": "Open Database License",
                    }
                },
                minimum_withdrawal="5",
                monday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                more_info="More information about this fee",
                name="Atm by the Lake",
                notes=["string"],
                phone="",
                saturday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                services=["string"],
                site_identification="",
                site_name="",
                sunday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                supported_currencies=["string"],
                supported_languages=["string"],
                thursday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                tuesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                wednesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atm_id` but received ''"):
            await async_client.banks.atms.with_raw_response.update(
                atm_id="",
                path_bank_id="BANK_ID",
                accessibility_features=["string"],
                address={
                    "city": "Berlin",
                    "country_code": "DE",
                    "county": "",
                    "line_1": "No 1 the Road",
                    "line_2": "The Place",
                    "line_3": "The Hill",
                    "postcode": "13359",
                    "state": "Brandenburg",
                },
                atm_type="",
                balance_inquiry_fee="",
                body_bank_id="gh.29.uk",
                branch_identification="",
                cash_withdrawal_international_fee="",
                cash_withdrawal_national_fee="",
                friday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                has_deposit_capability="false",
                is_accessible="false",
                located_at="",
                location={
                    "latitude": 11.45,
                    "longitude": 11.45,
                },
                location_categories=["string"],
                meta={
                    "license": {
                        "id": "ODbL-1.0",
                        "name": "Open Database License",
                    }
                },
                minimum_withdrawal="5",
                monday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                more_info="More information about this fee",
                name="Atm by the Lake",
                notes=["string"],
                phone="",
                saturday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                services=["string"],
                site_identification="",
                site_name="",
                sunday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                supported_currencies=["string"],
                supported_languages=["string"],
                thursday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                tuesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
                wednesday={
                    "closing_time": "18:00",
                    "opening_time": "10:00",
                },
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        atm = await async_client.banks.atms.list(
            "BANK_ID",
        )
        assert atm.is_closed
        assert await atm.json() == {"foo": "bar"}
        assert cast(Any, atm.is_closed) is True
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        atm = await async_client.banks.atms.with_raw_response.list(
            "BANK_ID",
        )

        assert atm.is_closed is True
        assert atm.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await atm.json() == {"foo": "bar"}
        assert isinstance(atm, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/banks/BANK_ID/atms").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.banks.atms.with_streaming_response.list(
            "BANK_ID",
        ) as atm:
            assert not atm.is_closed
            assert atm.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await atm.json() == {"foo": "bar"}
            assert cast(Any, atm.is_closed) is True
            assert isinstance(atm, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, atm.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.banks.atms.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncObpAPI) -> None:
        atm = await async_client.banks.atms.delete(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )
        assert atm is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncObpAPI) -> None:
        response = await async_client.banks.atms.with_raw_response.delete(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        atm = await response.parse()
        assert atm is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncObpAPI) -> None:
        async with async_client.banks.atms.with_streaming_response.delete(
            atm_id="ATM_ID",
            bank_id="BANK_ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            atm = await response.parse()
            assert atm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.banks.atms.with_raw_response.delete(
                atm_id="ATM_ID",
                bank_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atm_id` but received ''"):
            await async_client.banks.atms.with_raw_response.delete(
                atm_id="",
                bank_id="BANK_ID",
            )
