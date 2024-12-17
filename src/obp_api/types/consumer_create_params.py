# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConsumerCreateParams"]


class ConsumerCreateParams(TypedDict, total=False):
    app_name: Required[str]

    app_type: Required[str]

    client_certificate: Required[Annotated[str, PropertyInfo(alias="clientCertificate")]]

    created: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    created_by_user_id: Required[str]

    description: Required[str]

    developer_email: Required[str]

    enabled: Required[bool]

    redirect_url: Required[str]
