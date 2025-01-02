# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DynamicMessageDocCreateParams"]


class DynamicMessageDocCreateParams(TypedDict, total=False):
    path_bank_id: Required[Annotated[str, PropertyInfo(alias="BANK_ID")]]

    adapter_implementation: Required[str]

    description: Required[str]

    example_inbound_message: Required[object]

    example_outbound_message: Required[object]

    inbound_avro_schema: Required[str]

    inbound_topic: Required[str]

    message_format: Required[str]

    method_body: Required[str]

    outbound_avro_schema: Required[str]

    outbound_topic: Required[str]

    process: Required[str]

    programming_lang: Required[str]

    body_bank_id: Annotated[str, PropertyInfo(alias="bank_id")]

    dynamic_message_doc_id: str
