# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ProductUpdateParams"]


class ProductUpdateParams(TypedDict, total=False):
    alias: Required[str]

    can_be_seen_on_views: Required[List[str]]

    category: Required[str]

    description: Required[str]

    is_active: Required[bool]

    name: Required[str]

    type: Required[str]
