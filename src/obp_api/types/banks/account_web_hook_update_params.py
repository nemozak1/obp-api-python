# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountWebHookUpdateParams"]


class AccountWebHookUpdateParams(TypedDict, total=False):
    account_webhook_id: Required[str]

    is_active: Required[str]
