# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .public import (
    PublicResource,
    AsyncPublicResource,
    PublicResourceWithRawResponse,
    AsyncPublicResourceWithRawResponse,
    PublicResourceWithStreamingResponse,
    AsyncPublicResourceWithStreamingResponse,
)
from .private import (
    PrivateResource,
    AsyncPrivateResource,
    PrivateResourceWithRawResponse,
    AsyncPrivateResourceWithRawResponse,
    PrivateResourceWithStreamingResponse,
    AsyncPrivateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .account_ids import (
    AccountIDsResource,
    AsyncAccountIDsResource,
    AccountIDsResourceWithRawResponse,
    AsyncAccountIDsResourceWithRawResponse,
    AccountIDsResourceWithStreamingResponse,
    AsyncAccountIDsResourceWithStreamingResponse,
)
from .account_ids.account_ids import AccountIDsResource, AsyncAccountIDsResource

__all__ = ["BankAccountsResource", "AsyncBankAccountsResource"]


class BankAccountsResource(SyncAPIResource):
    @cached_property
    def account_ids(self) -> AccountIDsResource:
        return AccountIDsResource(self._client)

    @cached_property
    def private(self) -> PrivateResource:
        return PrivateResource(self._client)

    @cached_property
    def public(self) -> PublicResource:
        return PublicResource(self._client)

    @cached_property
    def with_raw_response(self) -> BankAccountsResourceWithRawResponse:
        return BankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BankAccountsResourceWithStreamingResponse:
        return BankAccountsResourceWithStreamingResponse(self)


class AsyncBankAccountsResource(AsyncAPIResource):
    @cached_property
    def account_ids(self) -> AsyncAccountIDsResource:
        return AsyncAccountIDsResource(self._client)

    @cached_property
    def private(self) -> AsyncPrivateResource:
        return AsyncPrivateResource(self._client)

    @cached_property
    def public(self) -> AsyncPublicResource:
        return AsyncPublicResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBankAccountsResourceWithRawResponse:
        return AsyncBankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBankAccountsResourceWithStreamingResponse:
        return AsyncBankAccountsResourceWithStreamingResponse(self)


class BankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

    @cached_property
    def account_ids(self) -> AccountIDsResourceWithRawResponse:
        return AccountIDsResourceWithRawResponse(self._bank_accounts.account_ids)

    @cached_property
    def private(self) -> PrivateResourceWithRawResponse:
        return PrivateResourceWithRawResponse(self._bank_accounts.private)

    @cached_property
    def public(self) -> PublicResourceWithRawResponse:
        return PublicResourceWithRawResponse(self._bank_accounts.public)


class AsyncBankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

    @cached_property
    def account_ids(self) -> AsyncAccountIDsResourceWithRawResponse:
        return AsyncAccountIDsResourceWithRawResponse(self._bank_accounts.account_ids)

    @cached_property
    def private(self) -> AsyncPrivateResourceWithRawResponse:
        return AsyncPrivateResourceWithRawResponse(self._bank_accounts.private)

    @cached_property
    def public(self) -> AsyncPublicResourceWithRawResponse:
        return AsyncPublicResourceWithRawResponse(self._bank_accounts.public)


class BankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

    @cached_property
    def account_ids(self) -> AccountIDsResourceWithStreamingResponse:
        return AccountIDsResourceWithStreamingResponse(self._bank_accounts.account_ids)

    @cached_property
    def private(self) -> PrivateResourceWithStreamingResponse:
        return PrivateResourceWithStreamingResponse(self._bank_accounts.private)

    @cached_property
    def public(self) -> PublicResourceWithStreamingResponse:
        return PublicResourceWithStreamingResponse(self._bank_accounts.public)


class AsyncBankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

    @cached_property
    def account_ids(self) -> AsyncAccountIDsResourceWithStreamingResponse:
        return AsyncAccountIDsResourceWithStreamingResponse(self._bank_accounts.account_ids)

    @cached_property
    def private(self) -> AsyncPrivateResourceWithStreamingResponse:
        return AsyncPrivateResourceWithStreamingResponse(self._bank_accounts.private)

    @cached_property
    def public(self) -> AsyncPublicResourceWithStreamingResponse:
        return AsyncPublicResourceWithStreamingResponse(self._bank_accounts.public)
