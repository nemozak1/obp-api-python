# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntitlementRequestCreateParams"]


class EntitlementRequestCreateParams(TypedDict, total=False):
    bank_id: Required[str]

    role_name: Required[str]
