# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardUpdateParams", "PinReset", "Replacement"]


class CardUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_id: Required[str]

    allows: Required[List[str]]

    card_type: Required[str]

    collected: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    customer_id: Required[str]

    enabled: Required[bool]

    expires_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    issue_number: Required[str]

    name_on_card: Required[str]

    networks: Required[List[str]]

    pin_reset: Required[Iterable[PinReset]]

    posted: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    replacement: Required[Replacement]

    serial_number: Required[str]

    technology: Required[str]

    valid_from_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]


class PinReset(TypedDict, total=False):
    reason_requested: Required[str]

    requested_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]


class Replacement(TypedDict, total=False):
    reason_requested: Required[str]

    requested_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
