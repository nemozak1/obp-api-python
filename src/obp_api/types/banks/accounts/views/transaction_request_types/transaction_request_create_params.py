# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["TransactionRequestCreateParams", "To", "Value"]


class TransactionRequestCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_id: Required[Annotated[str, PropertyInfo(alias="ACCOUNT_ID")]]

    charge_policy: Required[str]

    description: Required[str]

    to: Required[To]

    value: Required[Value]

    future_date: str


class To(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    other_account_routing_address: Required[str]

    other_account_routing_scheme: Required[str]

    other_account_secondary_routing_address: Required[str]

    other_account_secondary_routing_scheme: Required[str]

    other_bank_routing_address: Required[str]

    other_bank_routing_scheme: Required[str]

    other_branch_routing_address: Required[str]

    other_branch_routing_scheme: Required[str]


class Value(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]
