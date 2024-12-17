# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WarehouseCreateParams", "Query", "QueryMatchAll"]


class WarehouseCreateParams(TypedDict, total=False):
    query: Required[Query]


class QueryMatchAll(TypedDict, total=False):
    none: str


class Query(TypedDict, total=False):
    match_all: Required[QueryMatchAll]
