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

__all__ = ["CRMEventsResource", "AsyncCRMEventsResource"]


class CRMEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CRMEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nemozak1/obp-api-python#accessing-raw-response-data-eg-headers
        """
        return CRMEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CRMEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nemozak1/obp-api-python#with_streaming_response
        """
        return CRMEventsResourceWithStreamingResponse(self)

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
        <p>Authentication is Mandatory</p>

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
            f"/obp/v5.1.0/banks/{bank_id}/crm-events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncCRMEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCRMEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nemozak1/obp-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCRMEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCRMEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nemozak1/obp-api-python#with_streaming_response
        """
        return AsyncCRMEventsResourceWithStreamingResponse(self)

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
        <p>Authentication is Mandatory</p>

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
            f"/obp/v5.1.0/banks/{bank_id}/crm-events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class CRMEventsResourceWithRawResponse:
    def __init__(self, crm_events: CRMEventsResource) -> None:
        self._crm_events = crm_events

        self.list = to_custom_raw_response_wrapper(
            crm_events.list,
            BinaryAPIResponse,
        )


class AsyncCRMEventsResourceWithRawResponse:
    def __init__(self, crm_events: AsyncCRMEventsResource) -> None:
        self._crm_events = crm_events

        self.list = async_to_custom_raw_response_wrapper(
            crm_events.list,
            AsyncBinaryAPIResponse,
        )


class CRMEventsResourceWithStreamingResponse:
    def __init__(self, crm_events: CRMEventsResource) -> None:
        self._crm_events = crm_events

        self.list = to_custom_streamed_response_wrapper(
            crm_events.list,
            StreamedBinaryAPIResponse,
        )


class AsyncCRMEventsResourceWithStreamingResponse:
    def __init__(self, crm_events: AsyncCRMEventsResource) -> None:
        self._crm_events = crm_events

        self.list = async_to_custom_streamed_response_wrapper(
            crm_events.list,
            AsyncStreamedBinaryAPIResponse,
        )
