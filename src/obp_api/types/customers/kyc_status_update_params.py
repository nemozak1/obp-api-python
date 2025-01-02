# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KYCStatusUpdateParams"]


class KYCStatusUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    customer_number: Required[str]

    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    ok: Required[bool]
