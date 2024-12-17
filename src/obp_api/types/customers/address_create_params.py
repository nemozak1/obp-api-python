# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AddressCreateParams"]


class AddressCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    city: Required[str]

    country_code: Required[str]

    county: Required[str]

    line_1: Required[str]

    line_2: Required[str]

    line_3: Required[str]

    postcode: Required[str]

    state: Required[str]

    status: Required[str]

    tags: Required[List[str]]
