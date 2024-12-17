# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConsentRequestCreateParams", "AccountAccess", "AccountAccessAccountRouting", "Entitlement"]


class ConsentRequestCreateParams(TypedDict, total=False):
    account_access: Required[Iterable[AccountAccess]]

    everything: Required[bool]

    bank_id: str

    consumer_id: str

    email: str

    entitlements: Iterable[Entitlement]

    phone_number: str

    time_to_live: int

    valid_from: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class AccountAccessAccountRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class AccountAccess(TypedDict, total=False):
    account_routing: Required[AccountAccessAccountRouting]

    view_id: Required[str]


class Entitlement(TypedDict, total=False):
    bank_id: Required[str]

    role_name: Required[str]
