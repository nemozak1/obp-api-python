# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .message_docs import (
    MessageDocsResource,
    AsyncMessageDocsResource,
    MessageDocsResourceWithRawResponse,
    AsyncMessageDocsResourceWithRawResponse,
    MessageDocsResourceWithStreamingResponse,
    AsyncMessageDocsResourceWithStreamingResponse,
)
from .message_docs.message_docs import MessageDocsResource, AsyncMessageDocsResource

__all__ = ["DocumentationResource", "AsyncDocumentationResource"]


class DocumentationResource(SyncAPIResource):
    @cached_property
    def message_docs(self) -> MessageDocsResource:
        return MessageDocsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DocumentationResourceWithRawResponse:
        return DocumentationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentationResourceWithStreamingResponse:
        return DocumentationResourceWithStreamingResponse(self)


class AsyncDocumentationResource(AsyncAPIResource):
    @cached_property
    def message_docs(self) -> AsyncMessageDocsResource:
        return AsyncMessageDocsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocumentationResourceWithRawResponse:
        return AsyncDocumentationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentationResourceWithStreamingResponse:
        return AsyncDocumentationResourceWithStreamingResponse(self)


class DocumentationResourceWithRawResponse:
    def __init__(self, documentation: DocumentationResource) -> None:
        self._documentation = documentation

    @cached_property
    def message_docs(self) -> MessageDocsResourceWithRawResponse:
        return MessageDocsResourceWithRawResponse(self._documentation.message_docs)


class AsyncDocumentationResourceWithRawResponse:
    def __init__(self, documentation: AsyncDocumentationResource) -> None:
        self._documentation = documentation

    @cached_property
    def message_docs(self) -> AsyncMessageDocsResourceWithRawResponse:
        return AsyncMessageDocsResourceWithRawResponse(self._documentation.message_docs)


class DocumentationResourceWithStreamingResponse:
    def __init__(self, documentation: DocumentationResource) -> None:
        self._documentation = documentation

    @cached_property
    def message_docs(self) -> MessageDocsResourceWithStreamingResponse:
        return MessageDocsResourceWithStreamingResponse(self._documentation.message_docs)


class AsyncDocumentationResourceWithStreamingResponse:
    def __init__(self, documentation: AsyncDocumentationResource) -> None:
        self._documentation = documentation

    @cached_property
    def message_docs(self) -> AsyncMessageDocsResourceWithStreamingResponse:
        return AsyncMessageDocsResourceWithStreamingResponse(self._documentation.message_docs)
