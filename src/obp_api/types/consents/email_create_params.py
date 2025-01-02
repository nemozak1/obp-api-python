# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailCreateParams", "Entitlement", "View"]


class EmailCreateParams(TypedDict, total=False):
    email: Required[str]

    entitlements: Required[Iterable[Entitlement]]

    everything: Required[bool]

    views: Required[Iterable[View]]

    consumer_id: str

    time_to_live: int

    valid_from: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class Entitlement(TypedDict, total=False):
    bank_id: Required[str]

    role_name: Required[str]


class View(TypedDict, total=False):
    account_id: Required[str]

    bank_id: Required[str]

    view_id: Required[str]
