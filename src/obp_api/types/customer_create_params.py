# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Union
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerCreateParams", "CreditLimit", "CreditRating", "FaceImage"]


class CustomerCreateParams(TypedDict, total=False):
    legal_name: Required[str]

    mobile_phone_number: Required[str]

    branch_id: str

    credit_limit: CreditLimit

    credit_rating: CreditRating

    customer_number: str

    date_of_birth: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]

    dependants: int

    dob_of_dependants: Annotated[List[Union[str, datetime.date]], PropertyInfo(format="iso8601")]

    email: str

    employment_status: str

    face_image: FaceImage

    highest_education_attained: str

    kyc_status: bool

    last_ok_date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]

    name_suffix: str

    relationship_status: str

    title: str


class CreditLimit(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]


class CreditRating(TypedDict, total=False):
    rating: Required[str]

    source: Required[str]


class FaceImage(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    url: Required[str]
