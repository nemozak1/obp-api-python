# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionRequestCreateParams", "Card", "To", "Value"]


class TransactionRequestCreateParams(TypedDict, total=False):
    card: Required[Card]

    description: Required[str]

    to: Required[To]

    value: Required[Value]


class Card(TypedDict, total=False):
    brand: Required[str]

    card_number: Required[str]

    card_type: Required[str]

    cvv: Required[str]

    expiry_month: Required[str]

    expiry_year: Required[str]

    name_on_card: Required[str]


class To(TypedDict, total=False):
    counterparty_id: Required[str]


class Value(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]
