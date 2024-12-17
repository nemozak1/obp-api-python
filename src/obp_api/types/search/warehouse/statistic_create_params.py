# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StatisticCreateParams", "Query", "QueryMatchAll"]


class StatisticCreateParams(TypedDict, total=False):
    index: Required[Annotated[str, PropertyInfo(alias="INDEX")]]

    query: Required[Query]


class QueryMatchAll(TypedDict, total=False):
    none: str


class Query(TypedDict, total=False):
    match_all: Required[QueryMatchAll]
