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

__all__ = ["AdapterResource", "AsyncAdapterResource"]


class AdapterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdapterResourceWithRawResponse:
        return AdapterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdapterResourceWithStreamingResponse:
        return AdapterResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        <p>Get basic information about the Adapter.</p><p>Authentication is Optional</p><p>Authentication is Mandatory</p>
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/obp/v5.1.0/adapter",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncAdapterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdapterResourceWithRawResponse:
        return AsyncAdapterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdapterResourceWithStreamingResponse:
        return AsyncAdapterResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        <p>Get basic information about the Adapter.</p><p>Authentication is Optional</p><p>Authentication is Mandatory</p>
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/obp/v5.1.0/adapter",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class AdapterResourceWithRawResponse:
    def __init__(self, adapter: AdapterResource) -> None:
        self._adapter = adapter

        self.retrieve = to_custom_raw_response_wrapper(
            adapter.retrieve,
            BinaryAPIResponse,
        )


class AsyncAdapterResourceWithRawResponse:
    def __init__(self, adapter: AsyncAdapterResource) -> None:
        self._adapter = adapter

        self.retrieve = async_to_custom_raw_response_wrapper(
            adapter.retrieve,
            AsyncBinaryAPIResponse,
        )


class AdapterResourceWithStreamingResponse:
    def __init__(self, adapter: AdapterResource) -> None:
        self._adapter = adapter

        self.retrieve = to_custom_streamed_response_wrapper(
            adapter.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncAdapterResourceWithStreamingResponse:
    def __init__(self, adapter: AsyncAdapterResource) -> None:
        self._adapter = adapter

        self.retrieve = async_to_custom_streamed_response_wrapper(
            adapter.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
