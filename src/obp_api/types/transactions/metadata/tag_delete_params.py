# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TagDeleteParams"]


class TagDeleteParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_id: Required[Annotated[str, PropertyInfo(alias="ACCOUNT_ID")]]

    view_id: Required[Annotated[str, PropertyInfo(alias="VIEW_ID")]]

    transaction_id: Required[Annotated[str, PropertyInfo(alias="TRANSACTION_ID")]]

    body: Required[object]
