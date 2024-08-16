# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["CurrenciesResource", "AsyncCurrenciesResource"]


class CurrenciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrenciesResourceWithRawResponse:
        return CurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrenciesResourceWithStreamingResponse:
        return CurrenciesResourceWithStreamingResponse(self)

    def list(
        self,
        bank_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        <p>Get Currencies specified by BANK_ID</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/obp/v5.1.0/banks/{bank_id}/currencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncCurrenciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrenciesResourceWithRawResponse:
        return AsyncCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrenciesResourceWithStreamingResponse:
        return AsyncCurrenciesResourceWithStreamingResponse(self)

    async def list(
        self,
        bank_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        <p>Get Currencies specified by BANK_ID</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/obp/v5.1.0/banks/{bank_id}/currencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class CurrenciesResourceWithRawResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.list = to_custom_raw_response_wrapper(
            currencies.list,
            BinaryAPIResponse,
        )


class AsyncCurrenciesResourceWithRawResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.list = async_to_custom_raw_response_wrapper(
            currencies.list,
            AsyncBinaryAPIResponse,
        )


class CurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.list = to_custom_streamed_response_wrapper(
            currencies.list,
            StreamedBinaryAPIResponse,
        )


class AsyncCurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.list = async_to_custom_streamed_response_wrapper(
            currencies.list,
            AsyncStreamedBinaryAPIResponse,
        )
