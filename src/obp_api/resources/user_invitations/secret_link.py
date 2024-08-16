# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..._base_client import make_request_options

__all__ = ["SecretLinkResource", "AsyncSecretLinkResource"]


class SecretLinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretLinkResourceWithRawResponse:
        return SecretLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretLinkResourceWithStreamingResponse:
        return SecretLinkResourceWithStreamingResponse(self)

    def retrieve(
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
        <p>Get User Invitation</p><p>Authentication is Mandatory</p>

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
            f"/obp/v5.1.0/banks/{bank_id}/user-invitations/SECRET_LINK",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSecretLinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretLinkResourceWithRawResponse:
        return AsyncSecretLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretLinkResourceWithStreamingResponse:
        return AsyncSecretLinkResourceWithStreamingResponse(self)

    async def retrieve(
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
        <p>Get User Invitation</p><p>Authentication is Mandatory</p>

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
            f"/obp/v5.1.0/banks/{bank_id}/user-invitations/SECRET_LINK",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SecretLinkResourceWithRawResponse:
    def __init__(self, secret_link: SecretLinkResource) -> None:
        self._secret_link = secret_link

        self.retrieve = to_custom_raw_response_wrapper(
            secret_link.retrieve,
            BinaryAPIResponse,
        )


class AsyncSecretLinkResourceWithRawResponse:
    def __init__(self, secret_link: AsyncSecretLinkResource) -> None:
        self._secret_link = secret_link

        self.retrieve = async_to_custom_raw_response_wrapper(
            secret_link.retrieve,
            AsyncBinaryAPIResponse,
        )


class SecretLinkResourceWithStreamingResponse:
    def __init__(self, secret_link: SecretLinkResource) -> None:
        self._secret_link = secret_link

        self.retrieve = to_custom_streamed_response_wrapper(
            secret_link.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncSecretLinkResourceWithStreamingResponse:
    def __init__(self, secret_link: AsyncSecretLinkResource) -> None:
        self._secret_link = secret_link

        self.retrieve = async_to_custom_streamed_response_wrapper(
            secret_link.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
