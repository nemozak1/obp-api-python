# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DataUpdateParams", "FaceImage"]


class DataUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    dependants: Required[int]

    employment_status: Required[str]

    face_image: Required[FaceImage]

    highest_education_attained: Required[str]

    relationship_status: Required[str]


class FaceImage(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    url: Required[str]
