# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MethodRoutingCreateParams", "Parameter"]


class MethodRoutingCreateParams(TypedDict, total=False):
    connector_name: Required[str]

    is_bank_id_exact_match: Required[bool]

    method_name: Required[str]

    parameters: Required[Iterable[Parameter]]

    bank_id_pattern: str

    method_routing_id: str


class Parameter(TypedDict, total=False):
    key: Required[str]

    value: Required[str]
