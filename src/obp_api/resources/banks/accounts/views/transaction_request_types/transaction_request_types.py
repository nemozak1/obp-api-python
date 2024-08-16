# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from .transaction_requests import (
    TransactionRequestsResource,
    AsyncTransactionRequestsResource,
    TransactionRequestsResourceWithRawResponse,
    AsyncTransactionRequestsResourceWithRawResponse,
    TransactionRequestsResourceWithStreamingResponse,
    AsyncTransactionRequestsResourceWithStreamingResponse,
)

__all__ = ["TransactionRequestTypesResource", "AsyncTransactionRequestTypesResource"]


class TransactionRequestTypesResource(SyncAPIResource):
    @cached_property
    def transaction_requests(self) -> TransactionRequestsResource:
        return TransactionRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionRequestTypesResourceWithRawResponse:
        return TransactionRequestTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionRequestTypesResourceWithStreamingResponse:
        return TransactionRequestTypesResourceWithStreamingResponse(self)


class AsyncTransactionRequestTypesResource(AsyncAPIResource):
    @cached_property
    def transaction_requests(self) -> AsyncTransactionRequestsResource:
        return AsyncTransactionRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionRequestTypesResourceWithRawResponse:
        return AsyncTransactionRequestTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionRequestTypesResourceWithStreamingResponse:
        return AsyncTransactionRequestTypesResourceWithStreamingResponse(self)


class TransactionRequestTypesResourceWithRawResponse:
    def __init__(self, transaction_request_types: TransactionRequestTypesResource) -> None:
        self._transaction_request_types = transaction_request_types

    @cached_property
    def transaction_requests(self) -> TransactionRequestsResourceWithRawResponse:
        return TransactionRequestsResourceWithRawResponse(self._transaction_request_types.transaction_requests)


class AsyncTransactionRequestTypesResourceWithRawResponse:
    def __init__(self, transaction_request_types: AsyncTransactionRequestTypesResource) -> None:
        self._transaction_request_types = transaction_request_types

    @cached_property
    def transaction_requests(self) -> AsyncTransactionRequestsResourceWithRawResponse:
        return AsyncTransactionRequestsResourceWithRawResponse(self._transaction_request_types.transaction_requests)


class TransactionRequestTypesResourceWithStreamingResponse:
    def __init__(self, transaction_request_types: TransactionRequestTypesResource) -> None:
        self._transaction_request_types = transaction_request_types

    @cached_property
    def transaction_requests(self) -> TransactionRequestsResourceWithStreamingResponse:
        return TransactionRequestsResourceWithStreamingResponse(self._transaction_request_types.transaction_requests)


class AsyncTransactionRequestTypesResourceWithStreamingResponse:
    def __init__(self, transaction_request_types: AsyncTransactionRequestTypesResource) -> None:
        self._transaction_request_types = transaction_request_types

    @cached_property
    def transaction_requests(self) -> AsyncTransactionRequestsResourceWithStreamingResponse:
        return AsyncTransactionRequestsResourceWithStreamingResponse(
            self._transaction_request_types.transaction_requests
        )
