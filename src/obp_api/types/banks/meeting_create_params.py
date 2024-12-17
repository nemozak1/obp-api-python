# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeetingCreateParams", "Creator", "Invitee", "InviteeContactDetails"]


class MeetingCreateParams(TypedDict, total=False):
    creator: Required[Creator]

    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    invitees: Required[Iterable[Invitee]]

    provider_id: Required[str]

    purpose_id: Required[str]


class Creator(TypedDict, total=False):
    email_address: Required[str]

    mobile_phone: Required[str]

    name: Required[str]


class InviteeContactDetails(TypedDict, total=False):
    email_address: Required[str]

    mobile_phone: Required[str]

    name: Required[str]


class Invitee(TypedDict, total=False):
    contact_details: Required[InviteeContactDetails]

    status: Required[str]
