# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardCreateParams", "PinReset", "Replacement"]


class CardCreateParams(TypedDict, total=False):
    account_id: Required[str]

    allows: Required[List[str]]

    brand: Required[str]

    card_number: Required[str]

    card_type: Required[str]

    customer_id: Required[str]

    enabled: Required[bool]

    expires_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    issue_number: Required[str]

    name_on_card: Required[str]

    networks: Required[List[str]]

    pin_reset: Required[Iterable[PinReset]]

    serial_number: Required[str]

    technology: Required[str]

    valid_from_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    collected: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    posted: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    replacement: Replacement


class PinReset(TypedDict, total=False):
    reason_requested: Required[str]

    requested_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]


class Replacement(TypedDict, total=False):
    reason_requested: Required[str]

    requested_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
