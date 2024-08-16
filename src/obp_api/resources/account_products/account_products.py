# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .attributes import (
    AttributesResource,
    AsyncAttributesResource,
    AttributesResourceWithRawResponse,
    AsyncAttributesResourceWithRawResponse,
    AttributesResourceWithStreamingResponse,
    AsyncAttributesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AccountProductsResource", "AsyncAccountProductsResource"]


class AccountProductsResource(SyncAPIResource):
    @cached_property
    def attributes(self) -> AttributesResource:
        return AttributesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountProductsResourceWithRawResponse:
        return AccountProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountProductsResourceWithStreamingResponse:
        return AccountProductsResourceWithStreamingResponse(self)


class AsyncAccountProductsResource(AsyncAPIResource):
    @cached_property
    def attributes(self) -> AsyncAttributesResource:
        return AsyncAttributesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountProductsResourceWithRawResponse:
        return AsyncAccountProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountProductsResourceWithStreamingResponse:
        return AsyncAccountProductsResourceWithStreamingResponse(self)


class AccountProductsResourceWithRawResponse:
    def __init__(self, account_products: AccountProductsResource) -> None:
        self._account_products = account_products

    @cached_property
    def attributes(self) -> AttributesResourceWithRawResponse:
        return AttributesResourceWithRawResponse(self._account_products.attributes)


class AsyncAccountProductsResourceWithRawResponse:
    def __init__(self, account_products: AsyncAccountProductsResource) -> None:
        self._account_products = account_products

    @cached_property
    def attributes(self) -> AsyncAttributesResourceWithRawResponse:
        return AsyncAttributesResourceWithRawResponse(self._account_products.attributes)


class AccountProductsResourceWithStreamingResponse:
    def __init__(self, account_products: AccountProductsResource) -> None:
        self._account_products = account_products

    @cached_property
    def attributes(self) -> AttributesResourceWithStreamingResponse:
        return AttributesResourceWithStreamingResponse(self._account_products.attributes)


class AsyncAccountProductsResourceWithStreamingResponse:
    def __init__(self, account_products: AsyncAccountProductsResource) -> None:
        self._account_products = account_products

    @cached_property
    def attributes(self) -> AsyncAttributesResourceWithStreamingResponse:
        return AsyncAttributesResourceWithStreamingResponse(self._account_products.attributes)
