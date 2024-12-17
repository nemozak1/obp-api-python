# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountAccountRoutingQueryParams", "AccountRouting"]


class AccountAccountRoutingQueryParams(TypedDict, total=False):
    account_routing: Required[AccountRouting]

    bank_id: str


class AccountRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]
