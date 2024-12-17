# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountWebHookCreateParams"]


class AccountWebHookCreateParams(TypedDict, total=False):
    account_id: Required[str]

    http_method: Required[str]

    http_protocol: Required[str]

    is_active: Required[str]

    trigger_name: Required[str]

    url: Required[str]
