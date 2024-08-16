# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .where import (
    WhereResource,
    AsyncWhereResource,
    WhereResourceWithRawResponse,
    AsyncWhereResourceWithRawResponse,
    WhereResourceWithStreamingResponse,
    AsyncWhereResourceWithStreamingResponse,
)
from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from .narrative import (
    NarrativeResource,
    AsyncNarrativeResource,
    NarrativeResourceWithRawResponse,
    AsyncNarrativeResourceWithRawResponse,
    NarrativeResourceWithStreamingResponse,
    AsyncNarrativeResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def narrative(self) -> NarrativeResource:
        return NarrativeResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def where(self) -> WhereResource:
        return WhereResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self)


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def narrative(self) -> AsyncNarrativeResource:
        return AsyncNarrativeResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def where(self) -> AsyncWhereResource:
        return AsyncWhereResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self)


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._metadata.comments)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._metadata.images)

    @cached_property
    def narrative(self) -> NarrativeResourceWithRawResponse:
        return NarrativeResourceWithRawResponse(self._metadata.narrative)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._metadata.tags)

    @cached_property
    def where(self) -> WhereResourceWithRawResponse:
        return WhereResourceWithRawResponse(self._metadata.where)


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._metadata.comments)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._metadata.images)

    @cached_property
    def narrative(self) -> AsyncNarrativeResourceWithRawResponse:
        return AsyncNarrativeResourceWithRawResponse(self._metadata.narrative)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._metadata.tags)

    @cached_property
    def where(self) -> AsyncWhereResourceWithRawResponse:
        return AsyncWhereResourceWithRawResponse(self._metadata.where)


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._metadata.comments)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._metadata.images)

    @cached_property
    def narrative(self) -> NarrativeResourceWithStreamingResponse:
        return NarrativeResourceWithStreamingResponse(self._metadata.narrative)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._metadata.tags)

    @cached_property
    def where(self) -> WhereResourceWithStreamingResponse:
        return WhereResourceWithStreamingResponse(self._metadata.where)


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._metadata.comments)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._metadata.images)

    @cached_property
    def narrative(self) -> AsyncNarrativeResourceWithStreamingResponse:
        return AsyncNarrativeResourceWithStreamingResponse(self._metadata.narrative)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._metadata.tags)

    @cached_property
    def where(self) -> AsyncWhereResourceWithStreamingResponse:
        return AsyncWhereResourceWithStreamingResponse(self._metadata.where)
