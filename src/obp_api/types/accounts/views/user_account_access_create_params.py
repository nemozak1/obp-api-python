# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserAccountAccessCreateParams", "View"]


class UserAccountAccessCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_id: Required[Annotated[str, PropertyInfo(alias="ACCOUNT_ID")]]

    provider: Required[str]

    username: Required[str]

    views: Required[Iterable[View]]


class View(TypedDict, total=False):
    is_system: Required[bool]

    view_id: Required[str]
