# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .warehouse import (
    WarehouseResource,
    AsyncWarehouseResource,
    WarehouseResourceWithRawResponse,
    AsyncWarehouseResourceWithRawResponse,
    WarehouseResourceWithStreamingResponse,
    AsyncWarehouseResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .warehouse.warehouse import WarehouseResource, AsyncWarehouseResource

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def warehouse(self) -> WarehouseResource:
        return WarehouseResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self)


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def warehouse(self) -> AsyncWarehouseResource:
        return AsyncWarehouseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self)


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._search.metrics)

    @cached_property
    def warehouse(self) -> WarehouseResourceWithRawResponse:
        return WarehouseResourceWithRawResponse(self._search.warehouse)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._search.metrics)

    @cached_property
    def warehouse(self) -> AsyncWarehouseResourceWithRawResponse:
        return AsyncWarehouseResourceWithRawResponse(self._search.warehouse)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._search.metrics)

    @cached_property
    def warehouse(self) -> WarehouseResourceWithStreamingResponse:
        return WarehouseResourceWithStreamingResponse(self._search.warehouse)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._search.metrics)

    @cached_property
    def warehouse(self) -> AsyncWarehouseResourceWithStreamingResponse:
        return AsyncWarehouseResourceWithStreamingResponse(self._search.warehouse)
