# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditLimitUpdateParams", "CreditLimit"]


class CreditLimitUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    credit_limit: Required[CreditLimit]


class CreditLimit(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]
