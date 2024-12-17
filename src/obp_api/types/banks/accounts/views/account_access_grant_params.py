# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccountAccessGrantParams"]


class AccountAccessGrantParams(TypedDict, total=False):
    path_view_id: Required[Annotated[str, PropertyInfo(alias="VIEW_ID")]]

    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    user_id: Required[str]

    body_view_id: Required[Annotated[str, PropertyInfo(alias="view_id")]]
