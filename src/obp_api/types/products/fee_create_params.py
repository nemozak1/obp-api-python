# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FeeCreateParams", "Value"]


class FeeCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    is_active: Required[bool]

    more_info: Required[str]

    name: Required[str]

    value: Required[Value]

    product_fee_id: str


class Value(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]

    frequency: Required[str]

    type: Required[str]
