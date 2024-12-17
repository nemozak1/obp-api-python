# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BankCreateParams", "BankRouting"]


class BankCreateParams(TypedDict, total=False):
    bank_code: Required[str]

    id: str

    bank_routings: Iterable[BankRouting]

    full_name: str

    logo: str

    website: str


class BankRouting(TypedDict, total=False):
    address: Required[str]

    scheme: Required[str]
