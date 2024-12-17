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


class TestDynamicMessageDocs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = client.banks.dynamic_message_docs.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
        )
        assert dynamic_message_doc.is_closed
        assert dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = client.banks.dynamic_message_docs.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
            body_bank_id="gh.29.uk",
            dynamic_message_doc_id="",
        )
        assert dynamic_message_doc.is_closed
        assert dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_message_doc = client.banks.dynamic_message_docs.with_raw_response.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
        )

        assert dynamic_message_doc.is_closed is True
        assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_message_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_message_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.banks.dynamic_message_docs.with_streaming_response.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
        ) as dynamic_message_doc:
            assert not dynamic_message_doc.is_closed
            assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_message_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_message_doc.is_closed) is True
            assert isinstance(dynamic_message_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_message_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_bank_id` but received ''"):
            client.banks.dynamic_message_docs.with_raw_response.create(
                path_bank_id="",
                adapter_implementation="",
                description="This an optional field. Maximum length is 2000. It can be any characters here.",
                example_inbound_message={},
                example_outbound_message={},
                inbound_avro_schema="",
                inbound_topic="",
                message_format="",
                method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
                outbound_avro_schema="",
                outbound_topic="",
                process="obp.getBank",
                programming_lang="Scala",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = client.banks.dynamic_message_docs.retrieve(
            "BANK_ID",
        )
        assert dynamic_message_doc.is_closed
        assert dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_message_doc = client.banks.dynamic_message_docs.with_raw_response.retrieve(
            "BANK_ID",
        )

        assert dynamic_message_doc.is_closed is True
        assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_message_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_message_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.banks.dynamic_message_docs.with_streaming_response.retrieve(
            "BANK_ID",
        ) as dynamic_message_doc:
            assert not dynamic_message_doc.is_closed
            assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_message_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_message_doc.is_closed) is True
            assert isinstance(dynamic_message_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_message_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.banks.dynamic_message_docs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = client.banks.dynamic_message_docs.list(
            "BANK_ID",
        )
        assert dynamic_message_doc.is_closed
        assert dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_message_doc = client.banks.dynamic_message_docs.with_raw_response.list(
            "BANK_ID",
        )

        assert dynamic_message_doc.is_closed is True
        assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_message_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_message_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.banks.dynamic_message_docs.with_streaming_response.list(
            "BANK_ID",
        ) as dynamic_message_doc:
            assert not dynamic_message_doc.is_closed
            assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_message_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_message_doc.is_closed) is True
            assert isinstance(dynamic_message_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_message_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: ObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            client.banks.dynamic_message_docs.with_raw_response.list(
                "",
            )


class TestAsyncDynamicMessageDocs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = await async_client.banks.dynamic_message_docs.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
        )
        assert dynamic_message_doc.is_closed
        assert await dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = await async_client.banks.dynamic_message_docs.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
            body_bank_id="gh.29.uk",
            dynamic_message_doc_id="",
        )
        assert dynamic_message_doc.is_closed
        assert await dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_message_doc = await async_client.banks.dynamic_message_docs.with_raw_response.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
        )

        assert dynamic_message_doc.is_closed is True
        assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_message_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_message_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.banks.dynamic_message_docs.with_streaming_response.create(
            path_bank_id="BANK_ID",
            adapter_implementation="",
            description="This an optional field. Maximum length is 2000. It can be any characters here.",
            example_inbound_message={},
            example_outbound_message={},
            inbound_avro_schema="",
            inbound_topic="",
            message_format="",
            method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
            outbound_avro_schema="",
            outbound_topic="",
            process="obp.getBank",
            programming_lang="Scala",
        ) as dynamic_message_doc:
            assert not dynamic_message_doc.is_closed
            assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_message_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_message_doc.is_closed) is True
            assert isinstance(dynamic_message_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_message_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_bank_id` but received ''"):
            await async_client.banks.dynamic_message_docs.with_raw_response.create(
                path_bank_id="",
                adapter_implementation="",
                description="This an optional field. Maximum length is 2000. It can be any characters here.",
                example_inbound_message={},
                example_outbound_message={},
                inbound_avro_schema="",
                inbound_topic="",
                message_format="",
                method_body="%20%20%20%20%20%20Future.successful%28%0A%20%20%20%20%20%20%20%20Full%28%28BankCommons%28%0A%20%20%20%20%20%20%20%20%20%20BankId%28%22Hello%20bank%20id%22%29%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%221%22%2C%0A%20%20%20%20%20%20%20%20%20%20%228%22%0A%20%20%20%20%20%20%20%20%29%2C%20None%29%29%0A%20%20%20%20%20%20%29",
                outbound_avro_schema="",
                outbound_topic="",
                process="obp.getBank",
                programming_lang="Scala",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = await async_client.banks.dynamic_message_docs.retrieve(
            "BANK_ID",
        )
        assert dynamic_message_doc.is_closed
        assert await dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_message_doc = await async_client.banks.dynamic_message_docs.with_raw_response.retrieve(
            "BANK_ID",
        )

        assert dynamic_message_doc.is_closed is True
        assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_message_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_message_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.banks.dynamic_message_docs.with_streaming_response.retrieve(
            "BANK_ID",
        ) as dynamic_message_doc:
            assert not dynamic_message_doc.is_closed
            assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_message_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_message_doc.is_closed) is True
            assert isinstance(dynamic_message_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_message_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.banks.dynamic_message_docs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_message_doc = await async_client.banks.dynamic_message_docs.list(
            "BANK_ID",
        )
        assert dynamic_message_doc.is_closed
        assert await dynamic_message_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_message_doc.is_closed) is True
        assert isinstance(dynamic_message_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_message_doc = await async_client.banks.dynamic_message_docs.with_raw_response.list(
            "BANK_ID",
        )

        assert dynamic_message_doc.is_closed is True
        assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_message_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_message_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/banks/BANK_ID/dynamic-message-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.banks.dynamic_message_docs.with_streaming_response.list(
            "BANK_ID",
        ) as dynamic_message_doc:
            assert not dynamic_message_doc.is_closed
            assert dynamic_message_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_message_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_message_doc.is_closed) is True
            assert isinstance(dynamic_message_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_message_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncObpAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bank_id` but received ''"):
            await async_client.banks.dynamic_message_docs.with_raw_response.list(
                "",
            )
