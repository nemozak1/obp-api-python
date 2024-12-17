# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DynamicEntityUpdateParams", "FooBar", "FooBarProperties", "FooBarPropertiesName", "FooBarPropertiesNumber"]


class DynamicEntityUpdateParams(TypedDict, total=False):
    path_dynamic_entity_id: Required[Annotated[str, PropertyInfo(alias="DYNAMIC_ENTITY_ID")]]

    foo_bar: Required[Annotated[FooBar, PropertyInfo(alias="FooBar")]]

    has_personal_entity: Required[Annotated[bool, PropertyInfo(alias="hasPersonalEntity")]]

    bank_id: Annotated[str, PropertyInfo(alias="bankId")]

    body_dynamic_entity_id: Annotated[str, PropertyInfo(alias="dynamicEntityId")]

    user_id: Annotated[str, PropertyInfo(alias="userId")]


class FooBarPropertiesName(TypedDict, total=False):
    description: Required[str]

    example: Required[str]

    max_length: Required[Annotated[int, PropertyInfo(alias="maxLength")]]

    min_length: Required[Annotated[int, PropertyInfo(alias="minLength")]]

    type: Required[Literal["number", "integer", "boolean", "string", "DATE_WITH_DAY"]]


class FooBarPropertiesNumber(TypedDict, total=False):
    description: Required[str]

    example: Required[int]

    type: Required[Literal["number", "integer", "boolean", "string", "DATE_WITH_DAY"]]


class FooBarProperties(TypedDict, total=False):
    name: Required[FooBarPropertiesName]

    number: Required[FooBarPropertiesNumber]


class FooBar(TypedDict, total=False):
    description: Required[str]

    properties: Required[FooBarProperties]

    required: Required[List[str]]
