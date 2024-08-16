# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .consent_requests import (
    ConsentRequestsResource,
    AsyncConsentRequestsResource,
    ConsentRequestsResourceWithRawResponse,
    AsyncConsentRequestsResourceWithRawResponse,
    ConsentRequestsResourceWithStreamingResponse,
    AsyncConsentRequestsResourceWithStreamingResponse,
)
from .consent_requests.consent_requests import ConsentRequestsResource, AsyncConsentRequestsResource

__all__ = ["ConsumerResource", "AsyncConsumerResource"]


class ConsumerResource(SyncAPIResource):
    @cached_property
    def consent_requests(self) -> ConsentRequestsResource:
        return ConsentRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConsumerResourceWithRawResponse:
        return ConsumerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumerResourceWithStreamingResponse:
        return ConsumerResourceWithStreamingResponse(self)


class AsyncConsumerResource(AsyncAPIResource):
    @cached_property
    def consent_requests(self) -> AsyncConsentRequestsResource:
        return AsyncConsentRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConsumerResourceWithRawResponse:
        return AsyncConsumerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumerResourceWithStreamingResponse:
        return AsyncConsumerResourceWithStreamingResponse(self)


class ConsumerResourceWithRawResponse:
    def __init__(self, consumer: ConsumerResource) -> None:
        self._consumer = consumer

    @cached_property
    def consent_requests(self) -> ConsentRequestsResourceWithRawResponse:
        return ConsentRequestsResourceWithRawResponse(self._consumer.consent_requests)


class AsyncConsumerResourceWithRawResponse:
    def __init__(self, consumer: AsyncConsumerResource) -> None:
        self._consumer = consumer

    @cached_property
    def consent_requests(self) -> AsyncConsentRequestsResourceWithRawResponse:
        return AsyncConsentRequestsResourceWithRawResponse(self._consumer.consent_requests)


class ConsumerResourceWithStreamingResponse:
    def __init__(self, consumer: ConsumerResource) -> None:
        self._consumer = consumer

    @cached_property
    def consent_requests(self) -> ConsentRequestsResourceWithStreamingResponse:
        return ConsentRequestsResourceWithStreamingResponse(self._consumer.consent_requests)


class AsyncConsumerResourceWithStreamingResponse:
    def __init__(self, consumer: AsyncConsumerResource) -> None:
        self._consumer = consumer

    @cached_property
    def consent_requests(self) -> AsyncConsentRequestsResourceWithStreamingResponse:
        return AsyncConsentRequestsResourceWithStreamingResponse(self._consumer.consent_requests)
