# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SocialMediaHandleCreateParams"]


class SocialMediaHandleCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    customer_number: Required[str]

    date_activated: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    date_added: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    handle: Required[str]

    type: Required[str]
