# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DynamicResourceDocUpdateParams", "ExampleRequestBody", "SuccessResponseBody"]


class DynamicResourceDocUpdateParams(TypedDict, total=False):
    description: Required[str]

    error_response_bodies: Required[str]

    method_body: Required[str]

    partial_function_name: Required[str]

    request_url: Required[str]

    request_verb: Required[str]

    roles: Required[str]

    summary: Required[str]

    tags: Required[str]

    bank_id: str

    dynamic_resource_doc_id: str

    example_request_body: ExampleRequestBody

    success_response_body: SuccessResponseBody


class ExampleRequestBody(TypedDict, total=False):
    _optional_fields: Required[Annotated[List[str], PropertyInfo(alias="_optional_fields_")]]

    age: Required[int]

    hobby: Required[List[str]]

    name: Required[str]


class SuccessResponseBody(TypedDict, total=False):
    _optional_fields: Required[Annotated[List[str], PropertyInfo(alias="_optional_fields_")]]

    age: Required[int]

    hobby: Required[List[str]]

    my_user_id: Required[str]

    name: Required[str]
