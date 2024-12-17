# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SystemViewCreateParams"]


class SystemViewCreateParams(TypedDict, total=False):
    allowed_actions: Required[List[str]]

    description: Required[str]

    hide_metadata_if_alias_used: Required[bool]

    is_public: Required[bool]

    metadata_view: Required[str]

    name: Required[str]

    which_alias_to_use: Required[str]

    can_grant_access_to_views: List[str]

    can_revoke_access_to_views: List[str]
