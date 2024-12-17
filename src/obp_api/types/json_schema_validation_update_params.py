# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["JsonSchemaValidationUpdateParams", "Properties", "PropertiesXxxID"]


class JsonSchemaValidationUpdateParams(TypedDict, total=False):
    schema: Required[Annotated[str, PropertyInfo(alias="$schema")]]

    additional_properties: Required[Annotated[bool, PropertyInfo(alias="additionalProperties")]]

    description: Required[str]

    properties: Required[Properties]

    required: Required[List[str]]

    title: Required[str]

    type: Required[str]


class PropertiesXxxID(TypedDict, total=False):
    examples: Required[List[str]]

    max_length: Required[Annotated[int, PropertyInfo(alias="maxLength")]]

    min_length: Required[Annotated[int, PropertyInfo(alias="minLength")]]

    type: Required[str]


class Properties(TypedDict, total=False):
    xxx_id: Required[PropertiesXxxID]
