# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StandingOrderCreateParams", "Amount", "When"]


class StandingOrderCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    amount: Required[Amount]

    counterparty_id: Required[str]

    customer_id: Required[str]

    date_starts: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    user_id: Required[str]

    when: Required[When]

    date_expires: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    date_signed: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class Amount(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]


class When(TypedDict, total=False):
    detail: Required[str]

    frequency: Required[str]
