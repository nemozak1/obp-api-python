# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ConsentRequestCreateParams",
    "FromAccount",
    "FromAccountAccountRouting",
    "FromAccountBankRouting",
    "FromAccountBranchRouting",
    "ToAccount",
    "ToAccountAccountRouting",
    "ToAccountBankRouting",
    "ToAccountBranchRouting",
    "ToAccountLimit",
]


class ConsentRequestCreateParams(TypedDict, total=False):
    from_account: Required[FromAccount]

    to_account: Required[ToAccount]

    email: str

    phone_number: str

    time_to_live: int

    valid_from: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class FromAccountAccountRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class FromAccountBankRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class FromAccountBranchRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class FromAccount(TypedDict, total=False):
    account_routing: Required[FromAccountAccountRouting]

    bank_routing: Required[FromAccountBankRouting]

    branch_routing: Required[FromAccountBranchRouting]


class ToAccountAccountRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class ToAccountBankRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class ToAccountBranchRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class ToAccountLimit(TypedDict, total=False):
    currency: Required[str]

    max_monthly_amount: Required[int]

    max_number_of_monthly_transactions: Required[int]

    max_number_of_yearly_transactions: Required[int]

    max_single_amount: Required[int]

    max_yearly_amount: Required[int]


class ToAccount(TypedDict, total=False):
    account_routing: Required[ToAccountAccountRouting]

    bank_routing: Required[ToAccountBankRouting]

    branch_routing: Required[ToAccountBranchRouting]

    limit: Required[ToAccountLimit]
