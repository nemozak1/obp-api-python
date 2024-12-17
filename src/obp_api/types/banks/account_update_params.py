# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountUpdateParams", "AccountRouting"]


class AccountUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_routings: Required[Iterable[AccountRouting]]

    branch_id: Required[str]

    label: Required[str]

    type: Required[str]


class AccountRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]
