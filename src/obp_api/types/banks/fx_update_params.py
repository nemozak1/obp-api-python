# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FxUpdateParams"]


class FxUpdateParams(TypedDict, total=False):
    path_bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    body_bank_id: Required[Annotated[str, PropertyInfo(alias="bank_id")]]

    conversion_value: Required[float]

    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    from_currency_code: Required[str]

    inverse_conversion_value: Required[float]

    to_currency_code: Required[str]
