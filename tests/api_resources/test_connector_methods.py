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


class TestConnectorMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = client.connector_methods.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
        )
        assert connector_method.is_closed
        assert connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = client.connector_methods.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
            connector_method_id="ace0352a-9a0f-4bfa-b30b-9003aa467f51",
        )
        assert connector_method.is_closed
        assert connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = client.connector_methods.with_raw_response.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
        )

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.connector_methods.with_streaming_response.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
        ) as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, StreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = client.connector_methods.retrieve()
        assert connector_method.is_closed
        assert connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = client.connector_methods.with_raw_response.retrieve()

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.connector_methods.with_streaming_response.retrieve() as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, StreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = client.connector_methods.update(
            method_body="%7B%0A%20%20%20%20const%20%5BbankId%5D%20%3D%20args%3B%0A%20%20%20%20%2F%2F%20call%20java%20or%20scala%20type%20in%20this%20way%0A%20%20%20%20const%20BigDecimal%20%3D%20Java.type(%27java.math.BigDecimal%27)%3B%0A%20%20%20%20%2F%2F%20define%20a%20class%0A%20%20%20%20class%20SwiftBic%7B%0A%20%20%20%20%20%20%20%20constructor(name%2C%20value)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.name%20%3D%20name%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.value%20%3D%20value%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20define%20async%20function%0A%20%20%20%20const%20someAsyncFn%20%3D%20async%20()%20%3D%3E%20new%20BigDecimal(%27123.456%27)%0A%20%20%20%20%2F%2F%20call%20other%20async%20methods%0A%20%20%20%20const%20data%20%3D%20await%20someAsyncFn()%3B%0A%0A%20%20%20%20const%20bank%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%22bankId%22%3A%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22value%22%3A%22HelloJsBank%3A%22%2B%20bankId%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22shortName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%20%2Bdata.toString()%2C%0A%20%20%20%20%20%20%20%20%22fullName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%22logoUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%22websiteUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingScheme%22%3A%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingAddress%22%3A%22Js%22%2C%0A%20%20%20%20%20%20%20%20%22swiftBic%22%3A%20new%20SwiftBic(%22Mock%20Swift%22%2C%2010).name%2C%0A%20%20%20%20%20%20%20%20%22nationalIdentifier%22%3A%22Js%22%2C%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20bank%3B%0A%7D",
            programming_lang="Js",
        )
        assert connector_method.is_closed
        assert connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = client.connector_methods.with_raw_response.update(
            method_body="%7B%0A%20%20%20%20const%20%5BbankId%5D%20%3D%20args%3B%0A%20%20%20%20%2F%2F%20call%20java%20or%20scala%20type%20in%20this%20way%0A%20%20%20%20const%20BigDecimal%20%3D%20Java.type(%27java.math.BigDecimal%27)%3B%0A%20%20%20%20%2F%2F%20define%20a%20class%0A%20%20%20%20class%20SwiftBic%7B%0A%20%20%20%20%20%20%20%20constructor(name%2C%20value)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.name%20%3D%20name%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.value%20%3D%20value%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20define%20async%20function%0A%20%20%20%20const%20someAsyncFn%20%3D%20async%20()%20%3D%3E%20new%20BigDecimal(%27123.456%27)%0A%20%20%20%20%2F%2F%20call%20other%20async%20methods%0A%20%20%20%20const%20data%20%3D%20await%20someAsyncFn()%3B%0A%0A%20%20%20%20const%20bank%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%22bankId%22%3A%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22value%22%3A%22HelloJsBank%3A%22%2B%20bankId%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22shortName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%20%2Bdata.toString()%2C%0A%20%20%20%20%20%20%20%20%22fullName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%22logoUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%22websiteUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingScheme%22%3A%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingAddress%22%3A%22Js%22%2C%0A%20%20%20%20%20%20%20%20%22swiftBic%22%3A%20new%20SwiftBic(%22Mock%20Swift%22%2C%2010).name%2C%0A%20%20%20%20%20%20%20%20%22nationalIdentifier%22%3A%22Js%22%2C%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20bank%3B%0A%7D",
            programming_lang="Js",
        )

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.connector_methods.with_streaming_response.update(
            method_body="%7B%0A%20%20%20%20const%20%5BbankId%5D%20%3D%20args%3B%0A%20%20%20%20%2F%2F%20call%20java%20or%20scala%20type%20in%20this%20way%0A%20%20%20%20const%20BigDecimal%20%3D%20Java.type(%27java.math.BigDecimal%27)%3B%0A%20%20%20%20%2F%2F%20define%20a%20class%0A%20%20%20%20class%20SwiftBic%7B%0A%20%20%20%20%20%20%20%20constructor(name%2C%20value)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.name%20%3D%20name%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.value%20%3D%20value%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20define%20async%20function%0A%20%20%20%20const%20someAsyncFn%20%3D%20async%20()%20%3D%3E%20new%20BigDecimal(%27123.456%27)%0A%20%20%20%20%2F%2F%20call%20other%20async%20methods%0A%20%20%20%20const%20data%20%3D%20await%20someAsyncFn()%3B%0A%0A%20%20%20%20const%20bank%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%22bankId%22%3A%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22value%22%3A%22HelloJsBank%3A%22%2B%20bankId%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22shortName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%20%2Bdata.toString()%2C%0A%20%20%20%20%20%20%20%20%22fullName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%22logoUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%22websiteUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingScheme%22%3A%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingAddress%22%3A%22Js%22%2C%0A%20%20%20%20%20%20%20%20%22swiftBic%22%3A%20new%20SwiftBic(%22Mock%20Swift%22%2C%2010).name%2C%0A%20%20%20%20%20%20%20%20%22nationalIdentifier%22%3A%22Js%22%2C%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20bank%3B%0A%7D",
            programming_lang="Js",
        ) as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, StreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = client.connector_methods.list()
        assert connector_method.is_closed
        assert connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = client.connector_methods.with_raw_response.list()

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.connector_methods.with_streaming_response.list() as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, StreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True


class TestAsyncConnectorMethods:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = await async_client.connector_methods.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
        )
        assert connector_method.is_closed
        assert await connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = await async_client.connector_methods.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
            connector_method_id="ace0352a-9a0f-4bfa-b30b-9003aa467f51",
        )
        assert connector_method.is_closed
        assert await connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = await async_client.connector_methods.with_raw_response.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
        )

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.connector_methods.with_streaming_response.create(
            method_body="package%20code.bankconnectors%3B%0A%0Aimport%20com.openbankproject.commons.model.*%3B%0Aimport%20java.util.function.Function%3B%0Aimport%20java.util.function.Supplier%3B%0A%0A%2F**%0A%20*%20This%20is%20a%20java%20dynamic%20function%20template.%0A%20*%20Must%20copy%20the%20whole%20content%20of%20the%20file%20as%20%22dynamic%20method%20body%22.%0A%20*%20Currently%2C%20support%20Java%201.8%20version%20language%20features%0A%20*%2F%0Apublic%20class%20DynamicJavaConnector%20implements%20Supplier%3CFunction%3CObject%5B%5D%2C%20Object%3E%3E%20%7B%0A%20%20%20%20private%20Object%20apply(Object%5B%5D%20args)%20%7B%0A%20%20%20%20%20%20%20BankId%20bankId%20%3D%20(BankId)%20args%5B0%5D%3B%0A%0A%20%20%20%20%20%20%20Bank%20bank%20%3D%20new%20BankCommons(bankId%2C%20%22The%20Java%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22The%20Royal%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Swift%20bic%20value%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Java%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%3B%0A%20%20%20%20%20%20%20return%20bank%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%40Override%0A%20%20%20%20public%20Function%3CObject%5B%5D%2C%20Object%3E%20get()%20%7B%0A%20%20%20%20%20%20%20%20return%20this%3A%3Aapply%3B%0A%20%20%20%20%7D%0A%7D%0A",
            method_name="getBank",
            programming_lang="Java",
        ) as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = await async_client.connector_methods.retrieve()
        assert connector_method.is_closed
        assert await connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = await async_client.connector_methods.with_raw_response.retrieve()

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.connector_methods.with_streaming_response.retrieve() as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = await async_client.connector_methods.update(
            method_body="%7B%0A%20%20%20%20const%20%5BbankId%5D%20%3D%20args%3B%0A%20%20%20%20%2F%2F%20call%20java%20or%20scala%20type%20in%20this%20way%0A%20%20%20%20const%20BigDecimal%20%3D%20Java.type(%27java.math.BigDecimal%27)%3B%0A%20%20%20%20%2F%2F%20define%20a%20class%0A%20%20%20%20class%20SwiftBic%7B%0A%20%20%20%20%20%20%20%20constructor(name%2C%20value)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.name%20%3D%20name%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.value%20%3D%20value%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20define%20async%20function%0A%20%20%20%20const%20someAsyncFn%20%3D%20async%20()%20%3D%3E%20new%20BigDecimal(%27123.456%27)%0A%20%20%20%20%2F%2F%20call%20other%20async%20methods%0A%20%20%20%20const%20data%20%3D%20await%20someAsyncFn()%3B%0A%0A%20%20%20%20const%20bank%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%22bankId%22%3A%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22value%22%3A%22HelloJsBank%3A%22%2B%20bankId%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22shortName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%20%2Bdata.toString()%2C%0A%20%20%20%20%20%20%20%20%22fullName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%22logoUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%22websiteUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingScheme%22%3A%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingAddress%22%3A%22Js%22%2C%0A%20%20%20%20%20%20%20%20%22swiftBic%22%3A%20new%20SwiftBic(%22Mock%20Swift%22%2C%2010).name%2C%0A%20%20%20%20%20%20%20%20%22nationalIdentifier%22%3A%22Js%22%2C%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20bank%3B%0A%7D",
            programming_lang="Js",
        )
        assert connector_method.is_closed
        assert await connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = await async_client.connector_methods.with_raw_response.update(
            method_body="%7B%0A%20%20%20%20const%20%5BbankId%5D%20%3D%20args%3B%0A%20%20%20%20%2F%2F%20call%20java%20or%20scala%20type%20in%20this%20way%0A%20%20%20%20const%20BigDecimal%20%3D%20Java.type(%27java.math.BigDecimal%27)%3B%0A%20%20%20%20%2F%2F%20define%20a%20class%0A%20%20%20%20class%20SwiftBic%7B%0A%20%20%20%20%20%20%20%20constructor(name%2C%20value)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.name%20%3D%20name%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.value%20%3D%20value%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20define%20async%20function%0A%20%20%20%20const%20someAsyncFn%20%3D%20async%20()%20%3D%3E%20new%20BigDecimal(%27123.456%27)%0A%20%20%20%20%2F%2F%20call%20other%20async%20methods%0A%20%20%20%20const%20data%20%3D%20await%20someAsyncFn()%3B%0A%0A%20%20%20%20const%20bank%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%22bankId%22%3A%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22value%22%3A%22HelloJsBank%3A%22%2B%20bankId%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22shortName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%20%2Bdata.toString()%2C%0A%20%20%20%20%20%20%20%20%22fullName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%22logoUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%22websiteUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingScheme%22%3A%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingAddress%22%3A%22Js%22%2C%0A%20%20%20%20%20%20%20%20%22swiftBic%22%3A%20new%20SwiftBic(%22Mock%20Swift%22%2C%2010).name%2C%0A%20%20%20%20%20%20%20%20%22nationalIdentifier%22%3A%22Js%22%2C%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20bank%3B%0A%7D",
            programming_lang="Js",
        )

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/connector-methods/CONNECTOR_METHOD_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.connector_methods.with_streaming_response.update(
            method_body="%7B%0A%20%20%20%20const%20%5BbankId%5D%20%3D%20args%3B%0A%20%20%20%20%2F%2F%20call%20java%20or%20scala%20type%20in%20this%20way%0A%20%20%20%20const%20BigDecimal%20%3D%20Java.type(%27java.math.BigDecimal%27)%3B%0A%20%20%20%20%2F%2F%20define%20a%20class%0A%20%20%20%20class%20SwiftBic%7B%0A%20%20%20%20%20%20%20%20constructor(name%2C%20value)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.name%20%3D%20name%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20this.value%20%3D%20value%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20define%20async%20function%0A%20%20%20%20const%20someAsyncFn%20%3D%20async%20()%20%3D%3E%20new%20BigDecimal(%27123.456%27)%0A%20%20%20%20%2F%2F%20call%20other%20async%20methods%0A%20%20%20%20const%20data%20%3D%20await%20someAsyncFn()%3B%0A%0A%20%20%20%20const%20bank%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%22bankId%22%3A%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22value%22%3A%22HelloJsBank%3A%22%2B%20bankId%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22shortName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%20%2Bdata.toString()%2C%0A%20%20%20%20%20%20%20%20%22fullName%22%3A%22The%20Js%20Bank%20of%20Scotland%22%2C%0A%20%20%20%20%20%20%20%20%22logoUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%2Flogo.gif%22%2C%0A%20%20%20%20%20%20%20%20%22websiteUrl%22%3A%22http%3A%2F%2Fwww.red-bank-shoreditch.com%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingScheme%22%3A%22OBP%22%2C%0A%20%20%20%20%20%20%20%20%22bankRoutingAddress%22%3A%22Js%22%2C%0A%20%20%20%20%20%20%20%20%22swiftBic%22%3A%20new%20SwiftBic(%22Mock%20Swift%22%2C%2010).name%2C%0A%20%20%20%20%20%20%20%20%22nationalIdentifier%22%3A%22Js%22%2C%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20bank%3B%0A%7D",
            programming_lang="Js",
        ) as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        connector_method = await async_client.connector_methods.list()
        assert connector_method.is_closed
        assert await connector_method.json() == {"foo": "bar"}
        assert cast(Any, connector_method.is_closed) is True
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        connector_method = await async_client.connector_methods.with_raw_response.list()

        assert connector_method.is_closed is True
        assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await connector_method.json() == {"foo": "bar"}
        assert isinstance(connector_method, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/connector-methods").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.connector_methods.with_streaming_response.list() as connector_method:
            assert not connector_method.is_closed
            assert connector_method.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await connector_method.json() == {"foo": "bar"}
            assert cast(Any, connector_method.is_closed) is True
            assert isinstance(connector_method, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, connector_method.is_closed) is True
