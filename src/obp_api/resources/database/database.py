# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DatabaseResource", "AsyncDatabaseResource"]


class DatabaseResource(SyncAPIResource):
    @cached_property
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatabaseResourceWithRawResponse:
        return DatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabaseResourceWithStreamingResponse:
        return DatabaseResourceWithStreamingResponse(self)


class AsyncDatabaseResource(AsyncAPIResource):
    @cached_property
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatabaseResourceWithRawResponse:
        return AsyncDatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabaseResourceWithStreamingResponse:
        return AsyncDatabaseResourceWithStreamingResponse(self)


class DatabaseResourceWithRawResponse:
    def __init__(self, database: DatabaseResource) -> None:
        self._database = database

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._database.info)


class AsyncDatabaseResourceWithRawResponse:
    def __init__(self, database: AsyncDatabaseResource) -> None:
        self._database = database

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._database.info)


class DatabaseResourceWithStreamingResponse:
    def __init__(self, database: DatabaseResource) -> None:
        self._database = database

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._database.info)


class AsyncDatabaseResourceWithStreamingResponse:
    def __init__(self, database: AsyncDatabaseResource) -> None:
        self._database = database

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._database.info)
