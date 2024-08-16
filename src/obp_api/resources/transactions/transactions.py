# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transaction import (
    TransactionResource,
    AsyncTransactionResource,
    TransactionResourceWithRawResponse,
    AsyncTransactionResourceWithRawResponse,
    TransactionResourceWithStreamingResponse,
    AsyncTransactionResourceWithStreamingResponse,
)
from .other_account import (
    OtherAccountResource,
    AsyncOtherAccountResource,
    OtherAccountResourceWithRawResponse,
    AsyncOtherAccountResourceWithRawResponse,
    OtherAccountResourceWithStreamingResponse,
    AsyncOtherAccountResourceWithStreamingResponse,
)
from .metadata.metadata import MetadataResource, AsyncMetadataResource
from .balancing_transaction import (
    BalancingTransactionResource,
    AsyncBalancingTransactionResource,
    BalancingTransactionResourceWithRawResponse,
    AsyncBalancingTransactionResourceWithRawResponse,
    BalancingTransactionResourceWithStreamingResponse,
    AsyncBalancingTransactionResourceWithStreamingResponse,
)
from .transaction_attributes import (
    TransactionAttributesResource,
    AsyncTransactionAttributesResource,
    TransactionAttributesResourceWithRawResponse,
    AsyncTransactionAttributesResourceWithRawResponse,
    TransactionAttributesResourceWithStreamingResponse,
    AsyncTransactionAttributesResourceWithStreamingResponse,
)

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def other_account(self) -> OtherAccountResource:
        return OtherAccountResource(self._client)

    @cached_property
    def transaction(self) -> TransactionResource:
        return TransactionResource(self._client)

    @cached_property
    def transaction_attributes(self) -> TransactionAttributesResource:
        return TransactionAttributesResource(self._client)

    @cached_property
    def balancing_transaction(self) -> BalancingTransactionResource:
        return BalancingTransactionResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self)


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def other_account(self) -> AsyncOtherAccountResource:
        return AsyncOtherAccountResource(self._client)

    @cached_property
    def transaction(self) -> AsyncTransactionResource:
        return AsyncTransactionResource(self._client)

    @cached_property
    def transaction_attributes(self) -> AsyncTransactionAttributesResource:
        return AsyncTransactionAttributesResource(self._client)

    @cached_property
    def balancing_transaction(self) -> AsyncBalancingTransactionResource:
        return AsyncBalancingTransactionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self)


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._transactions.metadata)

    @cached_property
    def other_account(self) -> OtherAccountResourceWithRawResponse:
        return OtherAccountResourceWithRawResponse(self._transactions.other_account)

    @cached_property
    def transaction(self) -> TransactionResourceWithRawResponse:
        return TransactionResourceWithRawResponse(self._transactions.transaction)

    @cached_property
    def transaction_attributes(self) -> TransactionAttributesResourceWithRawResponse:
        return TransactionAttributesResourceWithRawResponse(self._transactions.transaction_attributes)

    @cached_property
    def balancing_transaction(self) -> BalancingTransactionResourceWithRawResponse:
        return BalancingTransactionResourceWithRawResponse(self._transactions.balancing_transaction)


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._transactions.metadata)

    @cached_property
    def other_account(self) -> AsyncOtherAccountResourceWithRawResponse:
        return AsyncOtherAccountResourceWithRawResponse(self._transactions.other_account)

    @cached_property
    def transaction(self) -> AsyncTransactionResourceWithRawResponse:
        return AsyncTransactionResourceWithRawResponse(self._transactions.transaction)

    @cached_property
    def transaction_attributes(self) -> AsyncTransactionAttributesResourceWithRawResponse:
        return AsyncTransactionAttributesResourceWithRawResponse(self._transactions.transaction_attributes)

    @cached_property
    def balancing_transaction(self) -> AsyncBalancingTransactionResourceWithRawResponse:
        return AsyncBalancingTransactionResourceWithRawResponse(self._transactions.balancing_transaction)


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._transactions.metadata)

    @cached_property
    def other_account(self) -> OtherAccountResourceWithStreamingResponse:
        return OtherAccountResourceWithStreamingResponse(self._transactions.other_account)

    @cached_property
    def transaction(self) -> TransactionResourceWithStreamingResponse:
        return TransactionResourceWithStreamingResponse(self._transactions.transaction)

    @cached_property
    def transaction_attributes(self) -> TransactionAttributesResourceWithStreamingResponse:
        return TransactionAttributesResourceWithStreamingResponse(self._transactions.transaction_attributes)

    @cached_property
    def balancing_transaction(self) -> BalancingTransactionResourceWithStreamingResponse:
        return BalancingTransactionResourceWithStreamingResponse(self._transactions.balancing_transaction)


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._transactions.metadata)

    @cached_property
    def other_account(self) -> AsyncOtherAccountResourceWithStreamingResponse:
        return AsyncOtherAccountResourceWithStreamingResponse(self._transactions.other_account)

    @cached_property
    def transaction(self) -> AsyncTransactionResourceWithStreamingResponse:
        return AsyncTransactionResourceWithStreamingResponse(self._transactions.transaction)

    @cached_property
    def transaction_attributes(self) -> AsyncTransactionAttributesResourceWithStreamingResponse:
        return AsyncTransactionAttributesResourceWithStreamingResponse(self._transactions.transaction_attributes)

    @cached_property
    def balancing_transaction(self) -> AsyncBalancingTransactionResourceWithStreamingResponse:
        return AsyncBalancingTransactionResourceWithStreamingResponse(self._transactions.balancing_transaction)
