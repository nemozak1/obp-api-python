# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountUpdateParams", "AccountRouting", "Balance"]


class AccountUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    label: Required[str]

    product_code: Required[str]

    account_routings: Iterable[AccountRouting]

    balance: Balance

    branch_id: str

    user_id: str


class AccountRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class Balance(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]
