# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .secret_link import (
    SecretLinkResource,
    AsyncSecretLinkResource,
    SecretLinkResourceWithRawResponse,
    AsyncSecretLinkResourceWithRawResponse,
    SecretLinkResourceWithStreamingResponse,
    AsyncSecretLinkResourceWithStreamingResponse,
)

__all__ = ["UserInvitationsResource", "AsyncUserInvitationsResource"]


class UserInvitationsResource(SyncAPIResource):
    @cached_property
    def secret_link(self) -> SecretLinkResource:
        return SecretLinkResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserInvitationsResourceWithRawResponse:
        return UserInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserInvitationsResourceWithStreamingResponse:
        return UserInvitationsResourceWithStreamingResponse(self)


class AsyncUserInvitationsResource(AsyncAPIResource):
    @cached_property
    def secret_link(self) -> AsyncSecretLinkResource:
        return AsyncSecretLinkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserInvitationsResourceWithRawResponse:
        return AsyncUserInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserInvitationsResourceWithStreamingResponse:
        return AsyncUserInvitationsResourceWithStreamingResponse(self)


class UserInvitationsResourceWithRawResponse:
    def __init__(self, user_invitations: UserInvitationsResource) -> None:
        self._user_invitations = user_invitations

    @cached_property
    def secret_link(self) -> SecretLinkResourceWithRawResponse:
        return SecretLinkResourceWithRawResponse(self._user_invitations.secret_link)


class AsyncUserInvitationsResourceWithRawResponse:
    def __init__(self, user_invitations: AsyncUserInvitationsResource) -> None:
        self._user_invitations = user_invitations

    @cached_property
    def secret_link(self) -> AsyncSecretLinkResourceWithRawResponse:
        return AsyncSecretLinkResourceWithRawResponse(self._user_invitations.secret_link)


class UserInvitationsResourceWithStreamingResponse:
    def __init__(self, user_invitations: UserInvitationsResource) -> None:
        self._user_invitations = user_invitations

    @cached_property
    def secret_link(self) -> SecretLinkResourceWithStreamingResponse:
        return SecretLinkResourceWithStreamingResponse(self._user_invitations.secret_link)


class AsyncUserInvitationsResourceWithStreamingResponse:
    def __init__(self, user_invitations: AsyncUserInvitationsResource) -> None:
        self._user_invitations = user_invitations

    @cached_property
    def secret_link(self) -> AsyncSecretLinkResourceWithStreamingResponse:
        return AsyncSecretLinkResourceWithStreamingResponse(self._user_invitations.secret_link)
