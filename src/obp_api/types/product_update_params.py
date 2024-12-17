# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProductUpdateParams", "Meta", "MetaLicense"]


class ProductUpdateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    name: Required[str]

    parent_product_code: Required[str]

    description: str

    meta: Meta

    more_info_url: str

    terms_and_conditions_url: str


class MetaLicense(TypedDict, total=False):
    id: Required[str]

    name: Required[str]


class Meta(TypedDict, total=False):
    license: Required[MetaLicense]
