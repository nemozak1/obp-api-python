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


class TestDynamicResourceDocs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = client.dynamic_resource_docs.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )
        assert dynamic_resource_doc.is_closed
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = client.dynamic_resource_docs.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
            bank_id="gh.29.uk",
            dynamic_resource_doc_id="vce035ca-9a0f-4bfa-b30b-9003aa467f51",
            example_request_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "name": "Jhon",
            },
            success_response_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "my_user_id": "some_id_value",
                "name": "Jhon",
            },
        )
        assert dynamic_resource_doc.is_closed
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = client.dynamic_resource_docs.with_raw_response.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.dynamic_resource_docs.with_streaming_response.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        ) as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = client.dynamic_resource_docs.retrieve()
        assert dynamic_resource_doc.is_closed
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = client.dynamic_resource_docs.with_raw_response.retrieve()

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.dynamic_resource_docs.with_streaming_response.retrieve() as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = client.dynamic_resource_docs.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )
        assert dynamic_resource_doc.is_closed
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = client.dynamic_resource_docs.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
            bank_id="gh.29.uk",
            dynamic_resource_doc_id="vce035ca-9a0f-4bfa-b30b-9003aa467f51",
            example_request_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "name": "Jhon",
            },
            success_response_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "my_user_id": "some_id_value",
                "name": "Jhon",
            },
        )
        assert dynamic_resource_doc.is_closed
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = client.dynamic_resource_docs.with_raw_response.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.dynamic_resource_docs.with_streaming_response.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        ) as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = client.dynamic_resource_docs.list()
        assert dynamic_resource_doc.is_closed
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = client.dynamic_resource_docs.with_raw_response.list()

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.dynamic_resource_docs.with_streaming_response.list() as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_delete(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.delete("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = client.dynamic_resource_docs.delete()
        assert dynamic_resource_doc.is_closed
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_delete(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.delete("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = client.dynamic_resource_docs.with_raw_response.delete()

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_delete(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.delete("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.dynamic_resource_docs.with_streaming_response.delete() as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, StreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True


class TestAsyncDynamicResourceDocs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = await async_client.dynamic_resource_docs.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )
        assert dynamic_resource_doc.is_closed
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = await async_client.dynamic_resource_docs.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
            bank_id="gh.29.uk",
            dynamic_resource_doc_id="vce035ca-9a0f-4bfa-b30b-9003aa467f51",
            example_request_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "name": "Jhon",
            },
            success_response_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "my_user_id": "some_id_value",
                "name": "Jhon",
            },
        )
        assert dynamic_resource_doc.is_closed
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = await async_client.dynamic_resource_docs.with_raw_response.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.dynamic_resource_docs.with_streaming_response.create(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        ) as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = await async_client.dynamic_resource_docs.retrieve()
        assert dynamic_resource_doc.is_closed
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = await async_client.dynamic_resource_docs.with_raw_response.retrieve()

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.dynamic_resource_docs.with_streaming_response.retrieve() as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = await async_client.dynamic_resource_docs.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )
        assert dynamic_resource_doc.is_closed
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = await async_client.dynamic_resource_docs.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
            bank_id="gh.29.uk",
            dynamic_resource_doc_id="vce035ca-9a0f-4bfa-b30b-9003aa467f51",
            example_request_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "name": "Jhon",
            },
            success_response_body={
                "_optional_fields": ["hobby"],
                "age": 12,
                "hobby": ["coding"],
                "my_user_id": "some_id_value",
                "name": "Jhon",
            },
        )
        assert dynamic_resource_doc.is_closed
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = await async_client.dynamic_resource_docs.with_raw_response.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        )

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.dynamic_resource_docs.with_streaming_response.update(
            description="Create one User",
            error_response_bodies="OBP-50000: Unknown Error.,OBP-20001: User not logged in. Authentication is required!,OBP-20006: User is missing one or more roles: ,OBP-10001: Incorrect json format.",
            method_body="%20%20%20%20val%20Some(resourceDoc)%20%3D%20callContext.resourceDocument%0A%20%20%20%20val%20hasRequestBody%20%3D%20request.body.isDefined%0A%0A%20%20%20%20%2F%2F%20get%20Path%20Parameters%2C%20example%3A%0A%20%20%20%20%2F%2F%20if%20the%20requestUrl%20of%20resourceDoc%20is%20%2Fhello%2Fbanks%2FBANK_ID%2Fworld%0A%20%20%20%20%2F%2F%20the%20request%20path%20is%20%2Fhello%2Fbanks%2Fbank_x%2Fworld%0A%20%20%20%20%2F%2FpathParams.get(%22BANK_ID%22)%20will%20get%20Option(%22bank_x%22)%20value%0A%0A%20%20%20%20val%20myUserId%20%3D%20pathParams(%22MY_USER_ID%22)%0A%0A%0A%20%20%20%20val%20requestEntity%20%3D%20request.json%20match%20%7B%0A%20%20%20%20%20%20case%20Full(zson)%20%3D%3E%0A%20%20%20%20%20%20%20%20try%20%7B%0A%20%20%20%20%20%20%20%20%20%20zson.extract%5BRequestRootJsonClass%5D%0A%20%20%20%20%20%20%20%20%7D%20catch%20%7B%0A%20%20%20%20%20%20%20%20%20%20case%20e%3A%20MappingException%20%3D%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidJsonFormat%20%24%7Be.msg%7D%22))%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20case%20_%3A%20EmptyBox%20%3D%3E%0A%20%20%20%20%20%20%20%20return%20Full(errorJsonResponse(s%22%24InvalidRequestPayload%20Current%20request%20has%20no%20payload%22))%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%2F%2F%20please%20add%20business%20logic%20here%0A%20%20%20%20val%20responseBody%3AResponseRootJsonClass%20%3D%20ResponseRootJsonClass(s%22%24%7BmyUserId%7D_from_path%22%2C%20requestEntity.name%2C%20requestEntity.age%2C%20requestEntity.hobby)%0A%20%20%20%20Future.successful%20%7B%0A%20%20%20%20%20%20(responseBody%2C%20HttpCode.%60200%60(callContext.callContext))%0A%20%20%20%20%7D",
            partial_function_name="createUser",
            request_url="/my_user/MY_USER_ID",
            request_verb="POST",
            roles="CanCreateMyUser",
            summary="Create My User",
            tags="Create-My-User",
        ) as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = await async_client.dynamic_resource_docs.list()
        assert dynamic_resource_doc.is_closed
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = await async_client.dynamic_resource_docs.with_raw_response.list()

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/management/dynamic-resource-docs").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.dynamic_resource_docs.with_streaming_response.list() as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_delete(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.delete("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dynamic_resource_doc = await async_client.dynamic_resource_docs.delete()
        assert dynamic_resource_doc.is_closed
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert cast(Any, dynamic_resource_doc.is_closed) is True
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_delete(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.delete("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dynamic_resource_doc = await async_client.dynamic_resource_docs.with_raw_response.delete()

        assert dynamic_resource_doc.is_closed is True
        assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dynamic_resource_doc.json() == {"foo": "bar"}
        assert isinstance(dynamic_resource_doc, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_delete(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.delete("/obp/v5.1.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.dynamic_resource_docs.with_streaming_response.delete() as dynamic_resource_doc:
            assert not dynamic_resource_doc.is_closed
            assert dynamic_resource_doc.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dynamic_resource_doc.json() == {"foo": "bar"}
            assert cast(Any, dynamic_resource_doc.is_closed) is True
            assert isinstance(dynamic_resource_doc, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dynamic_resource_doc.is_closed) is True
