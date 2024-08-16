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
from ...types.user import attribute_create_params, attribute_update_params
from ..._base_client import make_request_options

__all__ = ["AttributesResource", "AsyncAttributesResource"]


class AttributesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttributesResourceWithRawResponse:
        return AttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttributesResourceWithStreamingResponse:
        return AttributesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        <p>Create My Personal User Attribute</p><p>The <code>type</code> field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/obp/v5.1.0/my/user/attributes",
            body=maybe_transform(body, attribute_create_params.AttributeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        <p>Update My Personal User Attribute for current user by USER_ATTRIBUTE_ID</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/obp/v5.1.0/my/user/attributes/USER_ATTRIBUTE_ID",
            body=maybe_transform(body, attribute_update_params.AttributeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """<p>Get My Personal User Attributes.</p><p>Authentication is Mandatory</p>"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/obp/v5.1.0/my/user/attributes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncAttributesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttributesResourceWithRawResponse:
        return AsyncAttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttributesResourceWithStreamingResponse:
        return AsyncAttributesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        <p>Create My Personal User Attribute</p><p>The <code>type</code> field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/obp/v5.1.0/my/user/attributes",
            body=await async_maybe_transform(body, attribute_create_params.AttributeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        <p>Update My Personal User Attribute for current user by USER_ATTRIBUTE_ID</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/obp/v5.1.0/my/user/attributes/USER_ATTRIBUTE_ID",
            body=await async_maybe_transform(body, attribute_update_params.AttributeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """<p>Get My Personal User Attributes.</p><p>Authentication is Mandatory</p>"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/obp/v5.1.0/my/user/attributes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class AttributesResourceWithRawResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_custom_raw_response_wrapper(
            attributes.create,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            attributes.update,
            BinaryAPIResponse,
        )
        self.list = to_custom_raw_response_wrapper(
            attributes.list,
            BinaryAPIResponse,
        )


class AsyncAttributesResourceWithRawResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_custom_raw_response_wrapper(
            attributes.create,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            attributes.update,
            AsyncBinaryAPIResponse,
        )
        self.list = async_to_custom_raw_response_wrapper(
            attributes.list,
            AsyncBinaryAPIResponse,
        )


class AttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_custom_streamed_response_wrapper(
            attributes.create,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            attributes.update,
            StreamedBinaryAPIResponse,
        )
        self.list = to_custom_streamed_response_wrapper(
            attributes.list,
            StreamedBinaryAPIResponse,
        )


class AsyncAttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_custom_streamed_response_wrapper(
            attributes.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            attributes.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list = async_to_custom_streamed_response_wrapper(
            attributes.list,
            AsyncStreamedBinaryAPIResponse,
        )
