# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["HistoricalResource", "AsyncHistoricalResource"]


class HistoricalResource(SyncAPIResource):
    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HistoricalResourceWithRawResponse:
        return HistoricalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoricalResourceWithStreamingResponse:
        return HistoricalResourceWithStreamingResponse(self)


class AsyncHistoricalResource(AsyncAPIResource):
    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHistoricalResourceWithRawResponse:
        return AsyncHistoricalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoricalResourceWithStreamingResponse:
        return AsyncHistoricalResourceWithStreamingResponse(self)


class HistoricalResourceWithRawResponse:
    def __init__(self, historical: HistoricalResource) -> None:
        self._historical = historical

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._historical.transactions)


class AsyncHistoricalResourceWithRawResponse:
    def __init__(self, historical: AsyncHistoricalResource) -> None:
        self._historical = historical

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._historical.transactions)


class HistoricalResourceWithStreamingResponse:
    def __init__(self, historical: HistoricalResource) -> None:
        self._historical = historical

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._historical.transactions)


class AsyncHistoricalResourceWithStreamingResponse:
    def __init__(self, historical: AsyncHistoricalResource) -> None:
        self._historical = historical

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._historical.transactions)
