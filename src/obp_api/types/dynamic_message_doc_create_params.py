# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DynamicMessageDocCreateParams"]


class DynamicMessageDocCreateParams(TypedDict, total=False):
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

    bank_id: str

    dynamic_message_doc_id: str
