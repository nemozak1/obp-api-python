# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionCreateParams", "Value"]


class TransactionCreateParams(TypedDict, total=False):
    charge_policy: Required[str]

    completed: Required[str]

    description: Required[str]

    from_account_id: Required[str]

    posted: Required[str]

    to_account_id: Required[str]

    type: Required[str]

    value: Required[Value]


class Value(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]
