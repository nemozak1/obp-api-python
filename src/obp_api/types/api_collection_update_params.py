# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["APICollectionUpdateParams"]


class APICollectionUpdateParams(TypedDict, total=False):
    api_collection_name: Required[str]

    is_sharable: Required[bool]

    description: str
