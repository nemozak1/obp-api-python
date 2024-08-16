# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .account import (
    AccountResource,
    AsyncAccountResource,
    AccountResourceWithRawResponse,
    AsyncAccountResourceWithRawResponse,
    AccountResourceWithStreamingResponse,
    AsyncAccountResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PublicAccountsResource", "AsyncPublicAccountsResource"]


class PublicAccountsResource(SyncAPIResource):
    @cached_property
    def account(self) -> AccountResource:
        return AccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> PublicAccountsResourceWithRawResponse:
        return PublicAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicAccountsResourceWithStreamingResponse:
        return PublicAccountsResourceWithStreamingResponse(self)


class AsyncPublicAccountsResource(AsyncAPIResource):
    @cached_property
    def account(self) -> AsyncAccountResource:
        return AsyncAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPublicAccountsResourceWithRawResponse:
        return AsyncPublicAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicAccountsResourceWithStreamingResponse:
        return AsyncPublicAccountsResourceWithStreamingResponse(self)


class PublicAccountsResourceWithRawResponse:
    def __init__(self, public_accounts: PublicAccountsResource) -> None:
        self._public_accounts = public_accounts

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        return AccountResourceWithRawResponse(self._public_accounts.account)


class AsyncPublicAccountsResourceWithRawResponse:
    def __init__(self, public_accounts: AsyncPublicAccountsResource) -> None:
        self._public_accounts = public_accounts

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        return AsyncAccountResourceWithRawResponse(self._public_accounts.account)


class PublicAccountsResourceWithStreamingResponse:
    def __init__(self, public_accounts: PublicAccountsResource) -> None:
        self._public_accounts = public_accounts

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        return AccountResourceWithStreamingResponse(self._public_accounts.account)


class AsyncPublicAccountsResourceWithStreamingResponse:
    def __init__(self, public_accounts: AsyncPublicAccountsResource) -> None:
        self._public_accounts = public_accounts

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        return AsyncAccountResourceWithStreamingResponse(self._public_accounts.account)
