# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AtmUpdateParams",
    "Address",
    "Friday",
    "Location",
    "Meta",
    "MetaLicense",
    "Monday",
    "Saturday",
    "Sunday",
    "Thursday",
    "Tuesday",
    "Wednesday",
    "Attribute",
]


class AtmUpdateParams(TypedDict, total=False):
    path_bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    accessibility_features: Required[List[str]]

    address: Required[Address]

    atm_type: Required[str]

    balance_inquiry_fee: Required[str]

    body_bank_id: Required[Annotated[str, PropertyInfo(alias="bank_id")]]

    branch_identification: Required[str]

    cash_withdrawal_international_fee: Required[str]

    cash_withdrawal_national_fee: Required[str]

    friday: Required[Friday]

    has_deposit_capability: Required[str]

    is_accessible: Required[str]

    located_at: Required[str]

    location: Required[Location]

    location_categories: Required[List[str]]

    meta: Required[Meta]

    minimum_withdrawal: Required[str]

    monday: Required[Monday]

    more_info: Required[str]

    name: Required[str]

    notes: Required[List[str]]

    phone: Required[str]

    saturday: Required[Saturday]

    services: Required[List[str]]

    site_identification: Required[str]

    site_name: Required[str]

    sunday: Required[Sunday]

    supported_currencies: Required[List[str]]

    supported_languages: Required[List[str]]

    thursday: Required[Thursday]

    tuesday: Required[Tuesday]

    wednesday: Required[Wednesday]

    id: str

    attributes: Iterable[Attribute]


class Address(TypedDict, total=False):
    city: Required[str]

    country_code: Required[str]

    county: Required[str]

    line_1: Required[str]

    line_2: Required[str]

    line_3: Required[str]

    postcode: Required[str]

    state: Required[str]


class Friday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Location(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]


class MetaLicense(TypedDict, total=False):
    id: Required[str]

    name: Required[str]


class Meta(TypedDict, total=False):
    license: Required[MetaLicense]


class Monday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Saturday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Sunday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Thursday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Tuesday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Wednesday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Attribute(TypedDict, total=False):
    atm_attribute_id: Required[str]

    atm_id: Required[str]

    bank_id: Required[str]

    name: Required[str]

    type: Required[str]

    value: Required[str]

    is_active: bool
