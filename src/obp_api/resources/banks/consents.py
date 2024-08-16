# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.banks import consent_update_params
from ..._base_client import make_request_options

__all__ = ["ConsentsResource", "AsyncConsentsResource"]


class ConsentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsentsResourceWithRawResponse:
        return ConsentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsentsResourceWithStreamingResponse:
        return ConsentsResourceWithStreamingResponse(self)

    def update(
        self,
        consent_id: str,
        *,
        bank_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        <p>This endpoint is used to update the Status of Consent.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not consent_id:
            raise ValueError(f"Expected a non-empty value for `consent_id` but received {consent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/obp/v5.1.0/banks/{bank_id}/consents/{consent_id}",
            body=maybe_transform(body, consent_update_params.ConsentUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncConsentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsentsResourceWithRawResponse:
        return AsyncConsentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsentsResourceWithStreamingResponse:
        return AsyncConsentsResourceWithStreamingResponse(self)

    async def update(
        self,
        consent_id: str,
        *,
        bank_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        <p>This endpoint is used to update the Status of Consent.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not consent_id:
            raise ValueError(f"Expected a non-empty value for `consent_id` but received {consent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/obp/v5.1.0/banks/{bank_id}/consents/{consent_id}",
            body=await async_maybe_transform(body, consent_update_params.ConsentUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ConsentsResourceWithRawResponse:
    def __init__(self, consents: ConsentsResource) -> None:
        self._consents = consents

        self.update = to_custom_raw_response_wrapper(
            consents.update,
            BinaryAPIResponse,
        )


class AsyncConsentsResourceWithRawResponse:
    def __init__(self, consents: AsyncConsentsResource) -> None:
        self._consents = consents

        self.update = async_to_custom_raw_response_wrapper(
            consents.update,
            AsyncBinaryAPIResponse,
        )


class ConsentsResourceWithStreamingResponse:
    def __init__(self, consents: ConsentsResource) -> None:
        self._consents = consents

        self.update = to_custom_streamed_response_wrapper(
            consents.update,
            StreamedBinaryAPIResponse,
        )


class AsyncConsentsResourceWithStreamingResponse:
    def __init__(self, consents: AsyncConsentsResource) -> None:
        self._consents = consents

        self.update = async_to_custom_streamed_response_wrapper(
            consents.update,
            AsyncStreamedBinaryAPIResponse,
        )
