# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RegulatedEntityCreateParams", "Service"]


class RegulatedEntityCreateParams(TypedDict, total=False):
    certificate_authority_ca_owner_id: Required[str]

    entity_address: Required[str]

    entity_certificate_public_key: Required[str]

    entity_code: Required[str]

    entity_country: Required[str]

    entity_name: Required[str]

    entity_post_code: Required[str]

    entity_town_city: Required[str]

    entity_type: Required[str]

    entity_web_site: Required[str]

    services: Required[Iterable[Service]]


class Service(TypedDict, total=False):
    cy: Required[Annotated[List[str], PropertyInfo(alias="CY")]]
