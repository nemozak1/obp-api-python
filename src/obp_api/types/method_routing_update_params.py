# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MethodRoutingUpdateParams", "Parameter"]


class MethodRoutingUpdateParams(TypedDict, total=False):
    path_method_routing_id: Required[Annotated[str, PropertyInfo(alias="METHOD_ROUTING_ID")]]

    connector_name: Required[str]

    is_bank_id_exact_match: Required[bool]

    method_name: Required[str]

    parameters: Required[Iterable[Parameter]]

    bank_id_pattern: str

    body_method_routing_id: Annotated[str, PropertyInfo(alias="method_routing_id")]


class Parameter(TypedDict, total=False):
    key: Required[str]

    value: Required[str]
