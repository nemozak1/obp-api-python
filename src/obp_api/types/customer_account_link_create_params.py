# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerAccountLinkCreateParams"]


class CustomerAccountLinkCreateParams(TypedDict, total=False):
    path_bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_id: Required[str]

    body_bank_id: Required[Annotated[str, PropertyInfo(alias="bank_id")]]

    customer_id: Required[str]

    relationship_type: Required[str]
