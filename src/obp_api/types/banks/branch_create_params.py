# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "BranchCreateParams",
    "Address",
    "BranchRouting",
    "DriveUp",
    "DriveUpFriday",
    "DriveUpMonday",
    "DriveUpSaturday",
    "DriveUpSunday",
    "DriveUpThursday",
    "DriveUpTuesday",
    "DriveUpWednesday",
    "Lobby",
    "LobbyFriday",
    "LobbyMonday",
    "LobbySaturday",
    "LobbySunday",
    "LobbyThursday",
    "LobbyTuesday",
    "LobbyWednesday",
    "Location",
    "Meta",
    "MetaLicense",
]


class BranchCreateParams(TypedDict, total=False):
    path_bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    id: Required[str]

    accessible_features: Required[Annotated[str, PropertyInfo(alias="accessibleFeatures")]]

    address: Required[Address]

    body_bank_id: Required[Annotated[str, PropertyInfo(alias="bank_id")]]

    branch_routing: Required[BranchRouting]

    branch_type: Required[str]

    drive_up: Required[DriveUp]

    is_accessible: Required[str]

    lobby: Required[Lobby]

    location: Required[Location]

    meta: Required[Meta]

    more_info: Required[str]

    name: Required[str]

    phone_number: Required[str]


class Address(TypedDict, total=False):
    city: Required[str]

    country_code: Required[str]

    county: Required[str]

    line_1: Required[str]

    line_2: Required[str]

    line_3: Required[str]

    postcode: Required[str]

    state: Required[str]


class BranchRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]


class DriveUpFriday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class DriveUpMonday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class DriveUpSaturday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class DriveUpSunday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class DriveUpThursday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class DriveUpTuesday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class DriveUpWednesday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class DriveUp(TypedDict, total=False):
    friday: Required[DriveUpFriday]

    monday: Required[DriveUpMonday]

    saturday: Required[DriveUpSaturday]

    sunday: Required[DriveUpSunday]

    thursday: Required[DriveUpThursday]

    tuesday: Required[DriveUpTuesday]

    wednesday: Required[DriveUpWednesday]


class LobbyFriday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class LobbyMonday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class LobbySaturday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class LobbySunday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class LobbyThursday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class LobbyTuesday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class LobbyWednesday(TypedDict, total=False):
    closing_time: Required[str]

    opening_time: Required[str]


class Lobby(TypedDict, total=False):
    friday: Required[Iterable[LobbyFriday]]

    monday: Required[Iterable[LobbyMonday]]

    saturday: Required[Iterable[LobbySaturday]]

    sunday: Required[Iterable[LobbySunday]]

    thursday: Required[Iterable[LobbyThursday]]

    tuesday: Required[Iterable[LobbyTuesday]]

    wednesday: Required[Iterable[LobbyWednesday]]


class Location(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]


class MetaLicense(TypedDict, total=False):
    id: Required[str]

    name: Required[str]


class Meta(TypedDict, total=False):
    license: Required[MetaLicense]
