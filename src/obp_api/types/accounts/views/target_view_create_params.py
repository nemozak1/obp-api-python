# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TargetViewCreateParams"]


class TargetViewCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_id: Required[Annotated[str, PropertyInfo(alias="ACCOUNT_ID")]]

    allowed_permissions: Required[List[str]]

    description: Required[str]

    hide_metadata_if_alias_used: Required[bool]

    is_public: Required[bool]

    metadata_view: Required[str]

    name: Required[str]

    which_alias_to_use: Required[str]
