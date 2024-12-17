# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UserEntitlementCreateParams", "Role"]


class UserEntitlementCreateParams(TypedDict, total=False):
    provider: Required[str]

    roles: Required[Iterable[Role]]

    username: Required[str]


class Role(TypedDict, total=False):
    bank_id: Required[str]

    role_name: Required[str]
