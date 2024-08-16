# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .current import (
    CurrentResource,
    AsyncCurrentResource,
    CurrentResourceWithRawResponse,
    AsyncCurrentResourceWithRawResponse,
    CurrentResourceWithStreamingResponse,
    AsyncCurrentResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CertificateResource", "AsyncCertificateResource"]


class CertificateResource(SyncAPIResource):
    @cached_property
    def current(self) -> CurrentResource:
        return CurrentResource(self._client)

    @cached_property
    def with_raw_response(self) -> CertificateResourceWithRawResponse:
        return CertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificateResourceWithStreamingResponse:
        return CertificateResourceWithStreamingResponse(self)


class AsyncCertificateResource(AsyncAPIResource):
    @cached_property
    def current(self) -> AsyncCurrentResource:
        return AsyncCurrentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificateResourceWithRawResponse:
        return AsyncCertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificateResourceWithStreamingResponse:
        return AsyncCertificateResourceWithStreamingResponse(self)


class CertificateResourceWithRawResponse:
    def __init__(self, certificate: CertificateResource) -> None:
        self._certificate = certificate

    @cached_property
    def current(self) -> CurrentResourceWithRawResponse:
        return CurrentResourceWithRawResponse(self._certificate.current)


class AsyncCertificateResourceWithRawResponse:
    def __init__(self, certificate: AsyncCertificateResource) -> None:
        self._certificate = certificate

    @cached_property
    def current(self) -> AsyncCurrentResourceWithRawResponse:
        return AsyncCurrentResourceWithRawResponse(self._certificate.current)


class CertificateResourceWithStreamingResponse:
    def __init__(self, certificate: CertificateResource) -> None:
        self._certificate = certificate

    @cached_property
    def current(self) -> CurrentResourceWithStreamingResponse:
        return CurrentResourceWithStreamingResponse(self._certificate.current)


class AsyncCertificateResourceWithStreamingResponse:
    def __init__(self, certificate: AsyncCertificateResource) -> None:
        self._certificate = certificate

    @cached_property
    def current(self) -> AsyncCurrentResourceWithStreamingResponse:
        return AsyncCurrentResourceWithStreamingResponse(self._certificate.current)
