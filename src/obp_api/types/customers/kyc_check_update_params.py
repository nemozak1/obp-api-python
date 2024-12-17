# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KYCCheckUpdateParams"]


class KYCCheckUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    customer_id: Required[Annotated[str, PropertyInfo(alias="CUSTOMER_ID")]]

    comments: Required[str]

    customer_number: Required[str]

    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    how: Required[str]

    satisfied: Required[bool]

    staff_name: Required[str]

    staff_user_id: Required[str]
