# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KYCDocumentUpdateParams"]


class KYCDocumentUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    customer_id: Required[Annotated[str, PropertyInfo(alias="CUSTOMER_ID")]]

    customer_number: Required[str]

    expiry_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    issue_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    issue_place: Required[str]

    number: Required[str]

    type: Required[str]
