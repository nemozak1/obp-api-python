# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["AccountCreateParams", "AccountRouting", "Balance"]


class AccountCreateParams(TypedDict, total=False):
    account_routings: Required[Iterable[AccountRouting]]

    balance: Required[Balance]

    branch_id: Required[str]

    label: Required[str]

    product_code: Required[str]

    user_id: Required[str]


class AccountRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class Balance(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]
