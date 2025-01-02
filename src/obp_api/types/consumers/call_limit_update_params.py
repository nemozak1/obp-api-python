# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CallLimitUpdateParams"]


class CallLimitUpdateParams(TypedDict, total=False):
    from_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    per_day_call_limit: Required[str]

    per_hour_call_limit: Required[str]

    per_minute_call_limit: Required[str]

    per_month_call_limit: Required[str]

    per_second_call_limit: Required[str]

    per_week_call_limit: Required[str]

    to_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    api_name: str

    api_version: str

    bank_id: str
