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
from ..._base_client import make_request_options
from ...types.customers import branch_update_params

__all__ = ["BranchResource", "AsyncBranchResource"]


class BranchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BranchResourceWithRawResponse:
        return BranchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BranchResourceWithStreamingResponse:
        return BranchResourceWithStreamingResponse(self)

    def update(
        self,
        customer_id: str,
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
        <p>Update the Branch of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/obp/v5.1.0/banks/{bank_id}/customers/{customer_id}/branch",
            body=maybe_transform(body, branch_update_params.BranchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncBranchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBranchResourceWithRawResponse:
        return AsyncBranchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBranchResourceWithStreamingResponse:
        return AsyncBranchResourceWithStreamingResponse(self)

    async def update(
        self,
        customer_id: str,
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
        <p>Update the Branch of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/obp/v5.1.0/banks/{bank_id}/customers/{customer_id}/branch",
            body=await async_maybe_transform(body, branch_update_params.BranchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class BranchResourceWithRawResponse:
    def __init__(self, branch: BranchResource) -> None:
        self._branch = branch

        self.update = to_custom_raw_response_wrapper(
            branch.update,
            BinaryAPIResponse,
        )


class AsyncBranchResourceWithRawResponse:
    def __init__(self, branch: AsyncBranchResource) -> None:
        self._branch = branch

        self.update = async_to_custom_raw_response_wrapper(
            branch.update,
            AsyncBinaryAPIResponse,
        )


class BranchResourceWithStreamingResponse:
    def __init__(self, branch: BranchResource) -> None:
        self._branch = branch

        self.update = to_custom_streamed_response_wrapper(
            branch.update,
            StreamedBinaryAPIResponse,
        )


class AsyncBranchResourceWithStreamingResponse:
    def __init__(self, branch: AsyncBranchResource) -> None:
        self._branch = branch

        self.update = async_to_custom_streamed_response_wrapper(
            branch.update,
            AsyncStreamedBinaryAPIResponse,
        )
