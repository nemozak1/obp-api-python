# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .notifications import (
    NotificationsResource,
    AsyncNotificationsResource,
    NotificationsResourceWithRawResponse,
    AsyncNotificationsResourceWithRawResponse,
    NotificationsResourceWithStreamingResponse,
    AsyncNotificationsResourceWithStreamingResponse,
)

__all__ = ["WebHooksResource", "AsyncWebHooksResource"]


class WebHooksResource(SyncAPIResource):
    @cached_property
    def notifications(self) -> NotificationsResource:
        return NotificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebHooksResourceWithRawResponse:
        return WebHooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebHooksResourceWithStreamingResponse:
        return WebHooksResourceWithStreamingResponse(self)


class AsyncWebHooksResource(AsyncAPIResource):
    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        return AsyncNotificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebHooksResourceWithRawResponse:
        return AsyncWebHooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebHooksResourceWithStreamingResponse:
        return AsyncWebHooksResourceWithStreamingResponse(self)


class WebHooksResourceWithRawResponse:
    def __init__(self, web_hooks: WebHooksResource) -> None:
        self._web_hooks = web_hooks

    @cached_property
    def notifications(self) -> NotificationsResourceWithRawResponse:
        return NotificationsResourceWithRawResponse(self._web_hooks.notifications)


class AsyncWebHooksResourceWithRawResponse:
    def __init__(self, web_hooks: AsyncWebHooksResource) -> None:
        self._web_hooks = web_hooks

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithRawResponse:
        return AsyncNotificationsResourceWithRawResponse(self._web_hooks.notifications)


class WebHooksResourceWithStreamingResponse:
    def __init__(self, web_hooks: WebHooksResource) -> None:
        self._web_hooks = web_hooks

    @cached_property
    def notifications(self) -> NotificationsResourceWithStreamingResponse:
        return NotificationsResourceWithStreamingResponse(self._web_hooks.notifications)


class AsyncWebHooksResourceWithStreamingResponse:
    def __init__(self, web_hooks: AsyncWebHooksResource) -> None:
        self._web_hooks = web_hooks

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithStreamingResponse:
        return AsyncNotificationsResourceWithStreamingResponse(self._web_hooks.notifications)
