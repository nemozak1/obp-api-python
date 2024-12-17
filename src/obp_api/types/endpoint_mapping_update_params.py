# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EndpointMappingUpdateParams", "ResponseMapping", "ResponseMappingBalance", "ResponseMappingName"]


class EndpointMappingUpdateParams(TypedDict, total=False):
    operation_id: Required[str]

    request_mapping: Required[object]

    response_mapping: Required[ResponseMapping]


class ResponseMappingBalance(TypedDict, total=False):
    entity: Required[str]

    field: Required[str]

    query: Required[str]


class ResponseMappingName(TypedDict, total=False):
    entity: Required[str]

    field: Required[str]

    query: Required[str]


class ResponseMapping(TypedDict, total=False):
    balance: Required[ResponseMappingBalance]

    name: Required[ResponseMappingName]
