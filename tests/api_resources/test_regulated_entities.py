# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from obp_api import ObpAPI, AsyncObpAPI
from obp_api._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegulatedEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        regulated_entity = client.regulated_entities.create(
            certificate_authority_ca_owner_id="CY_CBC",
            entity_address="EXAMPLE COMPANY LTD, 5 SOME STREET",
            entity_certificate_public_key="-----BEGIN CERTIFICATE-----MIICsjCCAZqgAwIBAgIGAYwQ62R0MA0GCSqGSIb3DQEBCwUAMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTAeFw0yMzExMjcxMzE1MTFaFw0yNTExMjYxMzE1MTFaMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK9WIodZHWzKyCcf9YfWEhPURbfO6zKuMqzHN27GdqHsVVEGxP4F/J4mso+0ENcRr6ur4u81iREaVdCc40rHDHVJNEtniD8Icbz7tcsqAewIVhc/q6WXGqImJpCq7hA0m247dDsaZT0lb/MVBiMoJxDEmAE/GYYnWTEn84R35WhJsMvuQ7QmLvNg6RkChY6POCT/YKe9NKwa1NqI1U+oA5RFzAaFtytvZCE3jtp+aR0brL7qaGfgxm6B7dEpGyhg0NcVCV7xMQNq2JxZTVdAr6lcsRGaAFulakmW3aNnmK+L35Wu8uW+OxNxwUuC6f3b4FVBa276FMuUTRfu7gc+k6kCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAAU5CjEyAoyTn7PgFpQD48ZNPuUsEQ19gzYgJvHMzFIoZ7jKBodjO5mCzWBcR7A4mpeAsdyiNBl2sTiZscSnNqxk61jVzP5Ba1D7XtOjjr7+3iqowrThj6BY40QqhYh/6BSY9fDzVZQiHnvlo6ZUM5kUK6OavZOovKlp5DIl5sGqoP0qAJnpQ4nhB2WVVsKfPlOXc+2KSsbJ23g9l8zaTMr+X0umlvfEKqyEl1Fa2L1dO0y/KFQ+ILmxcZLpRdq1hRAjd0quq9qGC8ucXhRWDgM4hslVpau0da68g0aItWNez3mc5lB82b3dcZpFMzO41bgw7gvw10AvvTfQDqEYIuQ==-----END CERTIFICATE-----",
            entity_code="PSD_PICY_CBC!12345",
            entity_country="CY",
            entity_name="EXAMPLE COMPANY LTD",
            entity_post_code="1060",
            entity_town_city="SOME CITY",
            entity_type="PSD_PI",
            entity_web_site="www.example.com",
            services=[{"cy": ["PS_010"]}],
        )
        assert regulated_entity.is_closed
        assert regulated_entity.json() == {"foo": "bar"}
        assert cast(Any, regulated_entity.is_closed) is True
        assert isinstance(regulated_entity, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        regulated_entity = client.regulated_entities.with_raw_response.create(
            certificate_authority_ca_owner_id="CY_CBC",
            entity_address="EXAMPLE COMPANY LTD, 5 SOME STREET",
            entity_certificate_public_key="-----BEGIN CERTIFICATE-----MIICsjCCAZqgAwIBAgIGAYwQ62R0MA0GCSqGSIb3DQEBCwUAMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTAeFw0yMzExMjcxMzE1MTFaFw0yNTExMjYxMzE1MTFaMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK9WIodZHWzKyCcf9YfWEhPURbfO6zKuMqzHN27GdqHsVVEGxP4F/J4mso+0ENcRr6ur4u81iREaVdCc40rHDHVJNEtniD8Icbz7tcsqAewIVhc/q6WXGqImJpCq7hA0m247dDsaZT0lb/MVBiMoJxDEmAE/GYYnWTEn84R35WhJsMvuQ7QmLvNg6RkChY6POCT/YKe9NKwa1NqI1U+oA5RFzAaFtytvZCE3jtp+aR0brL7qaGfgxm6B7dEpGyhg0NcVCV7xMQNq2JxZTVdAr6lcsRGaAFulakmW3aNnmK+L35Wu8uW+OxNxwUuC6f3b4FVBa276FMuUTRfu7gc+k6kCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAAU5CjEyAoyTn7PgFpQD48ZNPuUsEQ19gzYgJvHMzFIoZ7jKBodjO5mCzWBcR7A4mpeAsdyiNBl2sTiZscSnNqxk61jVzP5Ba1D7XtOjjr7+3iqowrThj6BY40QqhYh/6BSY9fDzVZQiHnvlo6ZUM5kUK6OavZOovKlp5DIl5sGqoP0qAJnpQ4nhB2WVVsKfPlOXc+2KSsbJ23g9l8zaTMr+X0umlvfEKqyEl1Fa2L1dO0y/KFQ+ILmxcZLpRdq1hRAjd0quq9qGC8ucXhRWDgM4hslVpau0da68g0aItWNez3mc5lB82b3dcZpFMzO41bgw7gvw10AvvTfQDqEYIuQ==-----END CERTIFICATE-----",
            entity_code="PSD_PICY_CBC!12345",
            entity_country="CY",
            entity_name="EXAMPLE COMPANY LTD",
            entity_post_code="1060",
            entity_town_city="SOME CITY",
            entity_type="PSD_PI",
            entity_web_site="www.example.com",
            services=[{"cy": ["PS_010"]}],
        )

        assert regulated_entity.is_closed is True
        assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"
        assert regulated_entity.json() == {"foo": "bar"}
        assert isinstance(regulated_entity, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.regulated_entities.with_streaming_response.create(
            certificate_authority_ca_owner_id="CY_CBC",
            entity_address="EXAMPLE COMPANY LTD, 5 SOME STREET",
            entity_certificate_public_key="-----BEGIN CERTIFICATE-----MIICsjCCAZqgAwIBAgIGAYwQ62R0MA0GCSqGSIb3DQEBCwUAMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTAeFw0yMzExMjcxMzE1MTFaFw0yNTExMjYxMzE1MTFaMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK9WIodZHWzKyCcf9YfWEhPURbfO6zKuMqzHN27GdqHsVVEGxP4F/J4mso+0ENcRr6ur4u81iREaVdCc40rHDHVJNEtniD8Icbz7tcsqAewIVhc/q6WXGqImJpCq7hA0m247dDsaZT0lb/MVBiMoJxDEmAE/GYYnWTEn84R35WhJsMvuQ7QmLvNg6RkChY6POCT/YKe9NKwa1NqI1U+oA5RFzAaFtytvZCE3jtp+aR0brL7qaGfgxm6B7dEpGyhg0NcVCV7xMQNq2JxZTVdAr6lcsRGaAFulakmW3aNnmK+L35Wu8uW+OxNxwUuC6f3b4FVBa276FMuUTRfu7gc+k6kCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAAU5CjEyAoyTn7PgFpQD48ZNPuUsEQ19gzYgJvHMzFIoZ7jKBodjO5mCzWBcR7A4mpeAsdyiNBl2sTiZscSnNqxk61jVzP5Ba1D7XtOjjr7+3iqowrThj6BY40QqhYh/6BSY9fDzVZQiHnvlo6ZUM5kUK6OavZOovKlp5DIl5sGqoP0qAJnpQ4nhB2WVVsKfPlOXc+2KSsbJ23g9l8zaTMr+X0umlvfEKqyEl1Fa2L1dO0y/KFQ+ILmxcZLpRdq1hRAjd0quq9qGC8ucXhRWDgM4hslVpau0da68g0aItWNez3mc5lB82b3dcZpFMzO41bgw7gvw10AvvTfQDqEYIuQ==-----END CERTIFICATE-----",
            entity_code="PSD_PICY_CBC!12345",
            entity_country="CY",
            entity_name="EXAMPLE COMPANY LTD",
            entity_post_code="1060",
            entity_town_city="SOME CITY",
            entity_type="PSD_PI",
            entity_web_site="www.example.com",
            services=[{"cy": ["PS_010"]}],
        ) as regulated_entity:
            assert not regulated_entity.is_closed
            assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"

            assert regulated_entity.json() == {"foo": "bar"}
            assert cast(Any, regulated_entity.is_closed) is True
            assert isinstance(regulated_entity, StreamedBinaryAPIResponse)

        assert cast(Any, regulated_entity.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities/REGULATED_ENTITY_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        regulated_entity = client.regulated_entities.retrieve()
        assert regulated_entity.is_closed
        assert regulated_entity.json() == {"foo": "bar"}
        assert cast(Any, regulated_entity.is_closed) is True
        assert isinstance(regulated_entity, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities/REGULATED_ENTITY_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        regulated_entity = client.regulated_entities.with_raw_response.retrieve()

        assert regulated_entity.is_closed is True
        assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"
        assert regulated_entity.json() == {"foo": "bar"}
        assert isinstance(regulated_entity, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities/REGULATED_ENTITY_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.regulated_entities.with_streaming_response.retrieve() as regulated_entity:
            assert not regulated_entity.is_closed
            assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"

            assert regulated_entity.json() == {"foo": "bar"}
            assert cast(Any, regulated_entity.is_closed) is True
            assert isinstance(regulated_entity, StreamedBinaryAPIResponse)

        assert cast(Any, regulated_entity.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        regulated_entity = client.regulated_entities.list()
        assert regulated_entity.is_closed
        assert regulated_entity.json() == {"foo": "bar"}
        assert cast(Any, regulated_entity.is_closed) is True
        assert isinstance(regulated_entity, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        regulated_entity = client.regulated_entities.with_raw_response.list()

        assert regulated_entity.is_closed is True
        assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"
        assert regulated_entity.json() == {"foo": "bar"}
        assert isinstance(regulated_entity, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: ObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.regulated_entities.with_streaming_response.list() as regulated_entity:
            assert not regulated_entity.is_closed
            assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"

            assert regulated_entity.json() == {"foo": "bar"}
            assert cast(Any, regulated_entity.is_closed) is True
            assert isinstance(regulated_entity, StreamedBinaryAPIResponse)

        assert cast(Any, regulated_entity.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ObpAPI) -> None:
        regulated_entity = client.regulated_entities.delete()
        assert regulated_entity is None

    @parametrize
    def test_raw_response_delete(self, client: ObpAPI) -> None:
        response = client.regulated_entities.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulated_entity = response.parse()
        assert regulated_entity is None

    @parametrize
    def test_streaming_response_delete(self, client: ObpAPI) -> None:
        with client.regulated_entities.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulated_entity = response.parse()
            assert regulated_entity is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRegulatedEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        regulated_entity = await async_client.regulated_entities.create(
            certificate_authority_ca_owner_id="CY_CBC",
            entity_address="EXAMPLE COMPANY LTD, 5 SOME STREET",
            entity_certificate_public_key="-----BEGIN CERTIFICATE-----MIICsjCCAZqgAwIBAgIGAYwQ62R0MA0GCSqGSIb3DQEBCwUAMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTAeFw0yMzExMjcxMzE1MTFaFw0yNTExMjYxMzE1MTFaMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK9WIodZHWzKyCcf9YfWEhPURbfO6zKuMqzHN27GdqHsVVEGxP4F/J4mso+0ENcRr6ur4u81iREaVdCc40rHDHVJNEtniD8Icbz7tcsqAewIVhc/q6WXGqImJpCq7hA0m247dDsaZT0lb/MVBiMoJxDEmAE/GYYnWTEn84R35WhJsMvuQ7QmLvNg6RkChY6POCT/YKe9NKwa1NqI1U+oA5RFzAaFtytvZCE3jtp+aR0brL7qaGfgxm6B7dEpGyhg0NcVCV7xMQNq2JxZTVdAr6lcsRGaAFulakmW3aNnmK+L35Wu8uW+OxNxwUuC6f3b4FVBa276FMuUTRfu7gc+k6kCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAAU5CjEyAoyTn7PgFpQD48ZNPuUsEQ19gzYgJvHMzFIoZ7jKBodjO5mCzWBcR7A4mpeAsdyiNBl2sTiZscSnNqxk61jVzP5Ba1D7XtOjjr7+3iqowrThj6BY40QqhYh/6BSY9fDzVZQiHnvlo6ZUM5kUK6OavZOovKlp5DIl5sGqoP0qAJnpQ4nhB2WVVsKfPlOXc+2KSsbJ23g9l8zaTMr+X0umlvfEKqyEl1Fa2L1dO0y/KFQ+ILmxcZLpRdq1hRAjd0quq9qGC8ucXhRWDgM4hslVpau0da68g0aItWNez3mc5lB82b3dcZpFMzO41bgw7gvw10AvvTfQDqEYIuQ==-----END CERTIFICATE-----",
            entity_code="PSD_PICY_CBC!12345",
            entity_country="CY",
            entity_name="EXAMPLE COMPANY LTD",
            entity_post_code="1060",
            entity_town_city="SOME CITY",
            entity_type="PSD_PI",
            entity_web_site="www.example.com",
            services=[{"cy": ["PS_010"]}],
        )
        assert regulated_entity.is_closed
        assert await regulated_entity.json() == {"foo": "bar"}
        assert cast(Any, regulated_entity.is_closed) is True
        assert isinstance(regulated_entity, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        regulated_entity = await async_client.regulated_entities.with_raw_response.create(
            certificate_authority_ca_owner_id="CY_CBC",
            entity_address="EXAMPLE COMPANY LTD, 5 SOME STREET",
            entity_certificate_public_key="-----BEGIN CERTIFICATE-----MIICsjCCAZqgAwIBAgIGAYwQ62R0MA0GCSqGSIb3DQEBCwUAMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTAeFw0yMzExMjcxMzE1MTFaFw0yNTExMjYxMzE1MTFaMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK9WIodZHWzKyCcf9YfWEhPURbfO6zKuMqzHN27GdqHsVVEGxP4F/J4mso+0ENcRr6ur4u81iREaVdCc40rHDHVJNEtniD8Icbz7tcsqAewIVhc/q6WXGqImJpCq7hA0m247dDsaZT0lb/MVBiMoJxDEmAE/GYYnWTEn84R35WhJsMvuQ7QmLvNg6RkChY6POCT/YKe9NKwa1NqI1U+oA5RFzAaFtytvZCE3jtp+aR0brL7qaGfgxm6B7dEpGyhg0NcVCV7xMQNq2JxZTVdAr6lcsRGaAFulakmW3aNnmK+L35Wu8uW+OxNxwUuC6f3b4FVBa276FMuUTRfu7gc+k6kCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAAU5CjEyAoyTn7PgFpQD48ZNPuUsEQ19gzYgJvHMzFIoZ7jKBodjO5mCzWBcR7A4mpeAsdyiNBl2sTiZscSnNqxk61jVzP5Ba1D7XtOjjr7+3iqowrThj6BY40QqhYh/6BSY9fDzVZQiHnvlo6ZUM5kUK6OavZOovKlp5DIl5sGqoP0qAJnpQ4nhB2WVVsKfPlOXc+2KSsbJ23g9l8zaTMr+X0umlvfEKqyEl1Fa2L1dO0y/KFQ+ILmxcZLpRdq1hRAjd0quq9qGC8ucXhRWDgM4hslVpau0da68g0aItWNez3mc5lB82b3dcZpFMzO41bgw7gvw10AvvTfQDqEYIuQ==-----END CERTIFICATE-----",
            entity_code="PSD_PICY_CBC!12345",
            entity_country="CY",
            entity_name="EXAMPLE COMPANY LTD",
            entity_post_code="1060",
            entity_town_city="SOME CITY",
            entity_type="PSD_PI",
            entity_web_site="www.example.com",
            services=[{"cy": ["PS_010"]}],
        )

        assert regulated_entity.is_closed is True
        assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await regulated_entity.json() == {"foo": "bar"}
        assert isinstance(regulated_entity, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.post("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.regulated_entities.with_streaming_response.create(
            certificate_authority_ca_owner_id="CY_CBC",
            entity_address="EXAMPLE COMPANY LTD, 5 SOME STREET",
            entity_certificate_public_key="-----BEGIN CERTIFICATE-----MIICsjCCAZqgAwIBAgIGAYwQ62R0MA0GCSqGSIb3DQEBCwUAMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTAeFw0yMzExMjcxMzE1MTFaFw0yNTExMjYxMzE1MTFaMBoxGDAWBgNVBAMMD2FwcC5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK9WIodZHWzKyCcf9YfWEhPURbfO6zKuMqzHN27GdqHsVVEGxP4F/J4mso+0ENcRr6ur4u81iREaVdCc40rHDHVJNEtniD8Icbz7tcsqAewIVhc/q6WXGqImJpCq7hA0m247dDsaZT0lb/MVBiMoJxDEmAE/GYYnWTEn84R35WhJsMvuQ7QmLvNg6RkChY6POCT/YKe9NKwa1NqI1U+oA5RFzAaFtytvZCE3jtp+aR0brL7qaGfgxm6B7dEpGyhg0NcVCV7xMQNq2JxZTVdAr6lcsRGaAFulakmW3aNnmK+L35Wu8uW+OxNxwUuC6f3b4FVBa276FMuUTRfu7gc+k6kCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAAU5CjEyAoyTn7PgFpQD48ZNPuUsEQ19gzYgJvHMzFIoZ7jKBodjO5mCzWBcR7A4mpeAsdyiNBl2sTiZscSnNqxk61jVzP5Ba1D7XtOjjr7+3iqowrThj6BY40QqhYh/6BSY9fDzVZQiHnvlo6ZUM5kUK6OavZOovKlp5DIl5sGqoP0qAJnpQ4nhB2WVVsKfPlOXc+2KSsbJ23g9l8zaTMr+X0umlvfEKqyEl1Fa2L1dO0y/KFQ+ILmxcZLpRdq1hRAjd0quq9qGC8ucXhRWDgM4hslVpau0da68g0aItWNez3mc5lB82b3dcZpFMzO41bgw7gvw10AvvTfQDqEYIuQ==-----END CERTIFICATE-----",
            entity_code="PSD_PICY_CBC!12345",
            entity_country="CY",
            entity_name="EXAMPLE COMPANY LTD",
            entity_post_code="1060",
            entity_town_city="SOME CITY",
            entity_type="PSD_PI",
            entity_web_site="www.example.com",
            services=[{"cy": ["PS_010"]}],
        ) as regulated_entity:
            assert not regulated_entity.is_closed
            assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await regulated_entity.json() == {"foo": "bar"}
            assert cast(Any, regulated_entity.is_closed) is True
            assert isinstance(regulated_entity, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, regulated_entity.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities/REGULATED_ENTITY_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        regulated_entity = await async_client.regulated_entities.retrieve()
        assert regulated_entity.is_closed
        assert await regulated_entity.json() == {"foo": "bar"}
        assert cast(Any, regulated_entity.is_closed) is True
        assert isinstance(regulated_entity, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities/REGULATED_ENTITY_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        regulated_entity = await async_client.regulated_entities.with_raw_response.retrieve()

        assert regulated_entity.is_closed is True
        assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await regulated_entity.json() == {"foo": "bar"}
        assert isinstance(regulated_entity, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities/REGULATED_ENTITY_ID").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.regulated_entities.with_streaming_response.retrieve() as regulated_entity:
            assert not regulated_entity.is_closed
            assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await regulated_entity.json() == {"foo": "bar"}
            assert cast(Any, regulated_entity.is_closed) is True
            assert isinstance(regulated_entity, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, regulated_entity.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        regulated_entity = await async_client.regulated_entities.list()
        assert regulated_entity.is_closed
        assert await regulated_entity.json() == {"foo": "bar"}
        assert cast(Any, regulated_entity.is_closed) is True
        assert isinstance(regulated_entity, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        regulated_entity = await async_client.regulated_entities.with_raw_response.list()

        assert regulated_entity.is_closed is True
        assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await regulated_entity.json() == {"foo": "bar"}
        assert isinstance(regulated_entity, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncObpAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/obp/v5.1.0/regulated-entities").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.regulated_entities.with_streaming_response.list() as regulated_entity:
            assert not regulated_entity.is_closed
            assert regulated_entity.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await regulated_entity.json() == {"foo": "bar"}
            assert cast(Any, regulated_entity.is_closed) is True
            assert isinstance(regulated_entity, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, regulated_entity.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncObpAPI) -> None:
        regulated_entity = await async_client.regulated_entities.delete()
        assert regulated_entity is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncObpAPI) -> None:
        response = await async_client.regulated_entities.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulated_entity = await response.parse()
        assert regulated_entity is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncObpAPI) -> None:
        async with async_client.regulated_entities.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulated_entity = await response.parse()
            assert regulated_entity is None

        assert cast(Any, response.is_closed) is True
