# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountApplicationCreateParams"]


class AccountApplicationCreateParams(TypedDict, total=False):
    product_code: Required[str]

    customer_id: str

    user_id: str
