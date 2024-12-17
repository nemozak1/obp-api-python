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


class TestSandbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_data_import(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/sandbox/data-import").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        sandbox = client.sandbox.data_import(
            accounts=[
                {
                    "id": "account1",
                    "balance": {
                        "amount": "1000.00",
                        "currency": "EUR",
                    },
                    "bank": "bank2",
                    "generate_accountants_view": True,
                    "generate_auditors_view": True,
                    "generate_public_view": False,
                    "iban": "21234567890",
                    "label": "Account 1 at Bank 2",
                    "number": "22",
                    "owners": ["string"],
                    "type": "savings",
                }
            ],
            atms=[
                {
                    "id": "atm1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Ashbourne Atm 1",
                }
            ],
            banks=[
                {
                    "id": "bank2",
                    "full_name": "Bank 2 Inc.",
                    "logo": "http://example.com/logo2",
                    "short_name": "bank 2",
                    "website": "http://example.com/2",
                }
            ],
            branches=[
                {
                    "id": "branch1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Genel Müdürlük",
                }
            ],
            crm_events=[
                {
                    "id": "KIFJA76876AS",
                    "actual_date": "1100-01-01T01:01:01.000Z",
                    "bank_id": "bank1",
                    "category": "Call",
                    "channel": "Phone",
                    "customer": {
                        "name": "James Brown",
                        "number": "698761728934",
                    },
                    "detail": "Check mortgage",
                }
            ],
            products=[
                {
                    "bank_id": "bank1",
                    "category": "cat1",
                    "code": "prd1",
                    "family": "fam1",
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "more_info_url": "www.example.com/index1",
                    "name": "product 1",
                    "super_family": "sup fam 1",
                }
            ],
            transactions=[
                {
                    "id": "blankCounterpartNameTransaction",
                    "details": {
                        "completed": "2012-04-07T00:00:00.001Z",
                        "description": "some description",
                        "new_balance": "1244.00",
                        "posted": "2012-03-07T00:00:00.001Z",
                        "type": "SEPA",
                        "value": "-135.33",
                    },
                    "this_account": {
                        "id": "account1",
                        "bank": "bank1",
                    },
                }
            ],
            users=[
                {
                    "email": "user1@example.com",
                    "password": "TESOBE520berlin123!",
                    "user_name": "User 1",
                }
            ],
        )
        assert sandbox.is_closed
        assert sandbox.json() == {"foo": "bar"}
        assert cast(Any, sandbox.is_closed) is True
        assert isinstance(sandbox, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_data_import(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/sandbox/data-import").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        sandbox = client.sandbox.with_raw_response.data_import(
            accounts=[
                {
                    "id": "account1",
                    "balance": {
                        "amount": "1000.00",
                        "currency": "EUR",
                    },
                    "bank": "bank2",
                    "generate_accountants_view": True,
                    "generate_auditors_view": True,
                    "generate_public_view": False,
                    "iban": "21234567890",
                    "label": "Account 1 at Bank 2",
                    "number": "22",
                    "owners": ["string"],
                    "type": "savings",
                }
            ],
            atms=[
                {
                    "id": "atm1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Ashbourne Atm 1",
                }
            ],
            banks=[
                {
                    "id": "bank2",
                    "full_name": "Bank 2 Inc.",
                    "logo": "http://example.com/logo2",
                    "short_name": "bank 2",
                    "website": "http://example.com/2",
                }
            ],
            branches=[
                {
                    "id": "branch1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Genel Müdürlük",
                }
            ],
            crm_events=[
                {
                    "id": "KIFJA76876AS",
                    "actual_date": "1100-01-01T01:01:01.000Z",
                    "bank_id": "bank1",
                    "category": "Call",
                    "channel": "Phone",
                    "customer": {
                        "name": "James Brown",
                        "number": "698761728934",
                    },
                    "detail": "Check mortgage",
                }
            ],
            products=[
                {
                    "bank_id": "bank1",
                    "category": "cat1",
                    "code": "prd1",
                    "family": "fam1",
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "more_info_url": "www.example.com/index1",
                    "name": "product 1",
                    "super_family": "sup fam 1",
                }
            ],
            transactions=[
                {
                    "id": "blankCounterpartNameTransaction",
                    "details": {
                        "completed": "2012-04-07T00:00:00.001Z",
                        "description": "some description",
                        "new_balance": "1244.00",
                        "posted": "2012-03-07T00:00:00.001Z",
                        "type": "SEPA",
                        "value": "-135.33",
                    },
                    "this_account": {
                        "id": "account1",
                        "bank": "bank1",
                    },
                }
            ],
            users=[
                {
                    "email": "user1@example.com",
                    "password": "TESOBE520berlin123!",
                    "user_name": "User 1",
                }
            ],
        )

        assert sandbox.is_closed is True
        assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"
        assert sandbox.json() == {"foo": "bar"}
        assert isinstance(sandbox, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_data_import(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/sandbox/data-import").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.sandbox.with_streaming_response.data_import(
            accounts=[
                {
                    "id": "account1",
                    "balance": {
                        "amount": "1000.00",
                        "currency": "EUR",
                    },
                    "bank": "bank2",
                    "generate_accountants_view": True,
                    "generate_auditors_view": True,
                    "generate_public_view": False,
                    "iban": "21234567890",
                    "label": "Account 1 at Bank 2",
                    "number": "22",
                    "owners": ["string"],
                    "type": "savings",
                }
            ],
            atms=[
                {
                    "id": "atm1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Ashbourne Atm 1",
                }
            ],
            banks=[
                {
                    "id": "bank2",
                    "full_name": "Bank 2 Inc.",
                    "logo": "http://example.com/logo2",
                    "short_name": "bank 2",
                    "website": "http://example.com/2",
                }
            ],
            branches=[
                {
                    "id": "branch1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Genel Müdürlük",
                }
            ],
            crm_events=[
                {
                    "id": "KIFJA76876AS",
                    "actual_date": "1100-01-01T01:01:01.000Z",
                    "bank_id": "bank1",
                    "category": "Call",
                    "channel": "Phone",
                    "customer": {
                        "name": "James Brown",
                        "number": "698761728934",
                    },
                    "detail": "Check mortgage",
                }
            ],
            products=[
                {
                    "bank_id": "bank1",
                    "category": "cat1",
                    "code": "prd1",
                    "family": "fam1",
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "more_info_url": "www.example.com/index1",
                    "name": "product 1",
                    "super_family": "sup fam 1",
                }
            ],
            transactions=[
                {
                    "id": "blankCounterpartNameTransaction",
                    "details": {
                        "completed": "2012-04-07T00:00:00.001Z",
                        "description": "some description",
                        "new_balance": "1244.00",
                        "posted": "2012-03-07T00:00:00.001Z",
                        "type": "SEPA",
                        "value": "-135.33",
                    },
                    "this_account": {
                        "id": "account1",
                        "bank": "bank1",
                    },
                }
            ],
            users=[
                {
                    "email": "user1@example.com",
                    "password": "TESOBE520berlin123!",
                    "user_name": "User 1",
                }
            ],
        ) as sandbox:
            assert not sandbox.is_closed
            assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"

            assert sandbox.json() == {"foo": "bar"}
            assert cast(Any, sandbox.is_closed) is True
            assert isinstance(sandbox, StreamedBinaryAPIResponse)

        assert cast(Any, sandbox.is_closed) is True


class TestAsyncSandbox:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_data_import(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/sandbox/data-import").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        sandbox = await async_client.sandbox.data_import(
            accounts=[
                {
                    "id": "account1",
                    "balance": {
                        "amount": "1000.00",
                        "currency": "EUR",
                    },
                    "bank": "bank2",
                    "generate_accountants_view": True,
                    "generate_auditors_view": True,
                    "generate_public_view": False,
                    "iban": "21234567890",
                    "label": "Account 1 at Bank 2",
                    "number": "22",
                    "owners": ["string"],
                    "type": "savings",
                }
            ],
            atms=[
                {
                    "id": "atm1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Ashbourne Atm 1",
                }
            ],
            banks=[
                {
                    "id": "bank2",
                    "full_name": "Bank 2 Inc.",
                    "logo": "http://example.com/logo2",
                    "short_name": "bank 2",
                    "website": "http://example.com/2",
                }
            ],
            branches=[
                {
                    "id": "branch1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Genel Müdürlük",
                }
            ],
            crm_events=[
                {
                    "id": "KIFJA76876AS",
                    "actual_date": "1100-01-01T01:01:01.000Z",
                    "bank_id": "bank1",
                    "category": "Call",
                    "channel": "Phone",
                    "customer": {
                        "name": "James Brown",
                        "number": "698761728934",
                    },
                    "detail": "Check mortgage",
                }
            ],
            products=[
                {
                    "bank_id": "bank1",
                    "category": "cat1",
                    "code": "prd1",
                    "family": "fam1",
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "more_info_url": "www.example.com/index1",
                    "name": "product 1",
                    "super_family": "sup fam 1",
                }
            ],
            transactions=[
                {
                    "id": "blankCounterpartNameTransaction",
                    "details": {
                        "completed": "2012-04-07T00:00:00.001Z",
                        "description": "some description",
                        "new_balance": "1244.00",
                        "posted": "2012-03-07T00:00:00.001Z",
                        "type": "SEPA",
                        "value": "-135.33",
                    },
                    "this_account": {
                        "id": "account1",
                        "bank": "bank1",
                    },
                }
            ],
            users=[
                {
                    "email": "user1@example.com",
                    "password": "TESOBE520berlin123!",
                    "user_name": "User 1",
                }
            ],
        )
        assert sandbox.is_closed
        assert await sandbox.json() == {"foo": "bar"}
        assert cast(Any, sandbox.is_closed) is True
        assert isinstance(sandbox, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_data_import(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/sandbox/data-import").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        sandbox = await async_client.sandbox.with_raw_response.data_import(
            accounts=[
                {
                    "id": "account1",
                    "balance": {
                        "amount": "1000.00",
                        "currency": "EUR",
                    },
                    "bank": "bank2",
                    "generate_accountants_view": True,
                    "generate_auditors_view": True,
                    "generate_public_view": False,
                    "iban": "21234567890",
                    "label": "Account 1 at Bank 2",
                    "number": "22",
                    "owners": ["string"],
                    "type": "savings",
                }
            ],
            atms=[
                {
                    "id": "atm1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Ashbourne Atm 1",
                }
            ],
            banks=[
                {
                    "id": "bank2",
                    "full_name": "Bank 2 Inc.",
                    "logo": "http://example.com/logo2",
                    "short_name": "bank 2",
                    "website": "http://example.com/2",
                }
            ],
            branches=[
                {
                    "id": "branch1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Genel Müdürlük",
                }
            ],
            crm_events=[
                {
                    "id": "KIFJA76876AS",
                    "actual_date": "1100-01-01T01:01:01.000Z",
                    "bank_id": "bank1",
                    "category": "Call",
                    "channel": "Phone",
                    "customer": {
                        "name": "James Brown",
                        "number": "698761728934",
                    },
                    "detail": "Check mortgage",
                }
            ],
            products=[
                {
                    "bank_id": "bank1",
                    "category": "cat1",
                    "code": "prd1",
                    "family": "fam1",
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "more_info_url": "www.example.com/index1",
                    "name": "product 1",
                    "super_family": "sup fam 1",
                }
            ],
            transactions=[
                {
                    "id": "blankCounterpartNameTransaction",
                    "details": {
                        "completed": "2012-04-07T00:00:00.001Z",
                        "description": "some description",
                        "new_balance": "1244.00",
                        "posted": "2012-03-07T00:00:00.001Z",
                        "type": "SEPA",
                        "value": "-135.33",
                    },
                    "this_account": {
                        "id": "account1",
                        "bank": "bank1",
                    },
                }
            ],
            users=[
                {
                    "email": "user1@example.com",
                    "password": "TESOBE520berlin123!",
                    "user_name": "User 1",
                }
            ],
        )

        assert sandbox.is_closed is True
        assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await sandbox.json() == {"foo": "bar"}
        assert isinstance(sandbox, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_data_import(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/sandbox/data-import").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.sandbox.with_streaming_response.data_import(
            accounts=[
                {
                    "id": "account1",
                    "balance": {
                        "amount": "1000.00",
                        "currency": "EUR",
                    },
                    "bank": "bank2",
                    "generate_accountants_view": True,
                    "generate_auditors_view": True,
                    "generate_public_view": False,
                    "iban": "21234567890",
                    "label": "Account 1 at Bank 2",
                    "number": "22",
                    "owners": ["string"],
                    "type": "savings",
                }
            ],
            atms=[
                {
                    "id": "atm1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Ashbourne Atm 1",
                }
            ],
            banks=[
                {
                    "id": "bank2",
                    "full_name": "Bank 2 Inc.",
                    "logo": "http://example.com/logo2",
                    "short_name": "bank 2",
                    "website": "http://example.com/2",
                }
            ],
            branches=[
                {
                    "id": "branch1",
                    "address": {
                        "city": "Ashbourne",
                        "country_code": "UK",
                        "county": "Derbyshire",
                        "line_1": "5 Some Street",
                        "line_2": "Rosy Place",
                        "line_3": "Sunny Village",
                        "post_code": "WHY RU4",
                        "state": "",
                    },
                    "bank_id": "bank1",
                    "location": {
                        "latitude": 52.556198,
                        "longitude": 13.384099,
                    },
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "name": "Genel Müdürlük",
                }
            ],
            crm_events=[
                {
                    "id": "KIFJA76876AS",
                    "actual_date": "1100-01-01T01:01:01.000Z",
                    "bank_id": "bank1",
                    "category": "Call",
                    "channel": "Phone",
                    "customer": {
                        "name": "James Brown",
                        "number": "698761728934",
                    },
                    "detail": "Check mortgage",
                }
            ],
            products=[
                {
                    "bank_id": "bank1",
                    "category": "cat1",
                    "code": "prd1",
                    "family": "fam1",
                    "meta": {
                        "license": {
                            "id": "pddl",
                            "name": "Open Data Commons Public Domain Dedication and License (PDDL)",
                        }
                    },
                    "more_info_url": "www.example.com/index1",
                    "name": "product 1",
                    "super_family": "sup fam 1",
                }
            ],
            transactions=[
                {
                    "id": "blankCounterpartNameTransaction",
                    "details": {
                        "completed": "2012-04-07T00:00:00.001Z",
                        "description": "some description",
                        "new_balance": "1244.00",
                        "posted": "2012-03-07T00:00:00.001Z",
                        "type": "SEPA",
                        "value": "-135.33",
                    },
                    "this_account": {
                        "id": "account1",
                        "bank": "bank1",
                    },
                }
            ],
            users=[
                {
                    "email": "user1@example.com",
                    "password": "TESOBE520berlin123!",
                    "user_name": "User 1",
                }
            ],
        ) as sandbox:
            assert not sandbox.is_closed
            assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await sandbox.json() == {"foo": "bar"}
            assert cast(Any, sandbox.is_closed) is True
            assert isinstance(sandbox, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, sandbox.is_closed) is True
