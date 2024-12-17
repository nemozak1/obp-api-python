# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectorMethodCreateParams"]


class ConnectorMethodCreateParams(TypedDict, total=False):
    method_body: Required[str]

    method_name: Required[str]

    programming_lang: Required[str]

    connector_method_id: str
