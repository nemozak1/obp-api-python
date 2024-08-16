# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .private import (
    PrivateResource,
    AsyncPrivateResource,
    PrivateResourceWithRawResponse,
    AsyncPrivateResourceWithRawResponse,
    PrivateResourceWithStreamingResponse,
    AsyncPrivateResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AccountIDsResource", "AsyncAccountIDsResource"]


class AccountIDsResource(SyncAPIResource):
    @cached_property
    def private(self) -> PrivateResource:
        return PrivateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountIDsResourceWithRawResponse:
        return AccountIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountIDsResourceWithStreamingResponse:
        return AccountIDsResourceWithStreamingResponse(self)


class AsyncAccountIDsResource(AsyncAPIResource):
    @cached_property
    def private(self) -> AsyncPrivateResource:
        return AsyncPrivateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountIDsResourceWithRawResponse:
        return AsyncAccountIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountIDsResourceWithStreamingResponse:
        return AsyncAccountIDsResourceWithStreamingResponse(self)


class AccountIDsResourceWithRawResponse:
    def __init__(self, account_ids: AccountIDsResource) -> None:
        self._account_ids = account_ids

    @cached_property
    def private(self) -> PrivateResourceWithRawResponse:
        return PrivateResourceWithRawResponse(self._account_ids.private)


class AsyncAccountIDsResourceWithRawResponse:
    def __init__(self, account_ids: AsyncAccountIDsResource) -> None:
        self._account_ids = account_ids

    @cached_property
    def private(self) -> AsyncPrivateResourceWithRawResponse:
        return AsyncPrivateResourceWithRawResponse(self._account_ids.private)


class AccountIDsResourceWithStreamingResponse:
    def __init__(self, account_ids: AccountIDsResource) -> None:
        self._account_ids = account_ids

    @cached_property
    def private(self) -> PrivateResourceWithStreamingResponse:
        return PrivateResourceWithStreamingResponse(self._account_ids.private)


class AsyncAccountIDsResourceWithStreamingResponse:
    def __init__(self, account_ids: AsyncAccountIDsResource) -> None:
        self._account_ids = account_ids

    @cached_property
    def private(self) -> AsyncPrivateResourceWithStreamingResponse:
        return AsyncPrivateResourceWithStreamingResponse(self._account_ids.private)
