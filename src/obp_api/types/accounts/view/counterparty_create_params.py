# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CounterpartyCreateParams", "Bespoke"]


class CounterpartyCreateParams(TypedDict, total=False):
    bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    account_id: Required[Annotated[str, PropertyInfo(alias="ACCOUNT_ID")]]

    bespoke: Required[Iterable[Bespoke]]

    currency: Required[str]

    description: Required[str]

    is_beneficiary: Required[bool]

    name: Required[str]

    other_account_routing_address: Required[str]

    other_account_routing_scheme: Required[str]

    other_account_secondary_routing_address: Required[str]

    other_account_secondary_routing_scheme: Required[str]

    other_bank_routing_address: Required[str]

    other_bank_routing_scheme: Required[str]

    other_branch_routing_address: Required[str]

    other_branch_routing_scheme: Required[str]


class Bespoke(TypedDict, total=False):
    key: Required[str]

    value: Required[str]
