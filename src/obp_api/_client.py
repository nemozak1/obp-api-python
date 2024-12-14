# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    certs,
    roles,
    config,
    spaces,
    adapter,
    consent,
    sandbox,
    jwks_uris,
    crm_events,
    currencies,
    permissions,
    rate_limits,
    webui_props,
    entitlements,
    product_tree,
    accounts_held,
    resource_docs,
    method_routings,
    standing_orders,
    consent_requests,
    dynamic_entities,
    connector_methods,
    customers_minimal,
    endpoint_mappings,
    user_entitlements,
    regulated_entities,
    correlated_entities,
    product_collections,
    dynamic_message_docs,
    entitlement_requests,
    customer_account_links,
    fast_firehose_accounts,
    json_schema_validations,
    system_dynamic_entities,
    authentication_type_validations,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.api import api
from .resources.mtls import mtls
from .resources.user import user
from .resources.banks import banks
from .resources.cards import cards
from .resources.users import users
from .resources.views import views
from .resources.search import search
from .resources.metrics import metrics
from .resources.accounts import accounts
from .resources.consents import consents
from .resources.consumer import consumer
from .resources.database import database
from .resources.products import products
from .resources.connector import connector
from .resources.consumers import consumers
from .resources.customers import customers
from .resources.endpoints import endpoints
from .resources.web_hooks import web_hooks
from .resources.management import management
from .resources.development import development
from .resources.system_views import system_views
from .resources.transactions import transactions
from .resources.bank_accounts import bank_accounts
from .resources.documentation import documentation
from .resources.counterparties import counterparties
from .resources.api_collections import api_collections
from .resources.cascading_banks import cascading_banks
from .resources.public_accounts import public_accounts
from .resources.account_products import account_products
from .resources.system_integrity import system_integrity
from .resources.user_invitations import user_invitations
from .resources.dynamic_endpoints import dynamic_endpoints
from .resources.user_customer_links import user_customer_links
from .resources.dynamic_registration import dynamic_registration
from .resources.transaction_requests import transaction_requests
from .resources.dynamic_resource_docs import dynamic_resource_docs

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ObpAPI",
    "AsyncObpAPI",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "http://apisandbox.openbankproject.com/",
    "environment_1": "https://apisandbox.openbankproject.com/",
}


class ObpAPI(SyncAPIClient):
    accounts: accounts.AccountsResource
    adapter: adapter.AdapterResource
    api_collections: api_collections.APICollectionsResource
    api: api.APIResource
    banks: banks.BanksResource
    accounts_held: accounts_held.AccountsHeldResource
    counterparties: counterparties.CounterpartiesResource
    transactions: transactions.TransactionsResource
    customer_account_links: customer_account_links.CustomerAccountLinksResource
    permissions: permissions.PermissionsResource
    account_products: account_products.AccountProductsResource
    transaction_requests: transaction_requests.TransactionRequestsResource
    bank_accounts: bank_accounts.BankAccountsResource
    consents: consents.ConsentsResource
    crm_events: crm_events.CRMEventsResource
    currencies: currencies.CurrenciesResource
    customers: customers.CustomersResource
    product_collections: product_collections.ProductCollectionsResource
    product_tree: product_tree.ProductTreeResource
    products: products.ProductsResource
    public_accounts: public_accounts.PublicAccountsResource
    user_invitations: user_invitations.UserInvitationsResource
    user_customer_links: user_customer_links.UserCustomerLinksResource
    users: users.UsersResource
    views: views.ViewsResource
    web_hooks: web_hooks.WebHooksResource
    cards: cards.CardsResource
    certs: certs.CertsResource
    config: config.ConfigResource
    connector: connector.ConnectorResource
    consumer: consumer.ConsumerResource
    consent_requests: consent_requests.ConsentRequestsResource
    consumers: consumers.ConsumersResource
    customers_minimal: customers_minimal.CustomersMinimalResource
    database: database.DatabaseResource
    development: development.DevelopmentResource
    dynamic_registration: dynamic_registration.DynamicRegistrationResource
    endpoints: endpoints.EndpointsResource
    entitlement_requests: entitlement_requests.EntitlementRequestsResource
    entitlements: entitlements.EntitlementsResource
    jwks_uris: jwks_uris.JwksUrisResource
    management: management.ManagementResource
    authentication_type_validations: authentication_type_validations.AuthenticationTypeValidationsResource
    standing_orders: standing_orders.StandingOrdersResource
    dynamic_endpoints: dynamic_endpoints.DynamicEndpointsResource
    dynamic_message_docs: dynamic_message_docs.DynamicMessageDocsResource
    dynamic_resource_docs: dynamic_resource_docs.DynamicResourceDocsResource
    endpoint_mappings: endpoint_mappings.EndpointMappingsResource
    fast_firehose_accounts: fast_firehose_accounts.FastFirehoseAccountsResource
    cascading_banks: cascading_banks.CascadingBanksResource
    connector_methods: connector_methods.ConnectorMethodsResource
    json_schema_validations: json_schema_validations.JsonSchemaValidationsResource
    method_routings: method_routings.MethodRoutingsResource
    metrics: metrics.MetricsResource
    system_dynamic_entities: system_dynamic_entities.SystemDynamicEntitiesResource
    system_integrity: system_integrity.SystemIntegrityResource
    webui_props: webui_props.WebuiPropsResource
    documentation: documentation.DocumentationResource
    consent: consent.ConsentResource
    correlated_entities: correlated_entities.CorrelatedEntitiesResource
    dynamic_entities: dynamic_entities.DynamicEntitiesResource
    mtls: mtls.MtlsResource
    spaces: spaces.SpacesResource
    user: user.UserResource
    rate_limits: rate_limits.RateLimitsResource
    regulated_entities: regulated_entities.RegulatedEntitiesResource
    resource_docs: resource_docs.ResourceDocsResource
    roles: roles.RolesResource
    sandbox: sandbox.SandboxResource
    search: search.SearchResource
    system_views: system_views.SystemViewsResource
    user_entitlements: user_entitlements.UserEntitlementsResource
    with_raw_response: ObpAPIWithRawResponse
    with_streaming_response: ObpAPIWithStreamedResponse

    # client options

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous obp-api client instance."""
        self._environment = environment

        base_url_env = os.environ.get("OBP_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `OBP_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AccountsResource(self)
        self.adapter = adapter.AdapterResource(self)
        self.api_collections = api_collections.APICollectionsResource(self)
        self.api = api.APIResource(self)
        self.banks = banks.BanksResource(self)
        self.accounts_held = accounts_held.AccountsHeldResource(self)
        self.counterparties = counterparties.CounterpartiesResource(self)
        self.transactions = transactions.TransactionsResource(self)
        self.customer_account_links = customer_account_links.CustomerAccountLinksResource(self)
        self.permissions = permissions.PermissionsResource(self)
        self.account_products = account_products.AccountProductsResource(self)
        self.transaction_requests = transaction_requests.TransactionRequestsResource(self)
        self.bank_accounts = bank_accounts.BankAccountsResource(self)
        self.consents = consents.ConsentsResource(self)
        self.crm_events = crm_events.CRMEventsResource(self)
        self.currencies = currencies.CurrenciesResource(self)
        self.customers = customers.CustomersResource(self)
        self.product_collections = product_collections.ProductCollectionsResource(self)
        self.product_tree = product_tree.ProductTreeResource(self)
        self.products = products.ProductsResource(self)
        self.public_accounts = public_accounts.PublicAccountsResource(self)
        self.user_invitations = user_invitations.UserInvitationsResource(self)
        self.user_customer_links = user_customer_links.UserCustomerLinksResource(self)
        self.users = users.UsersResource(self)
        self.views = views.ViewsResource(self)
        self.web_hooks = web_hooks.WebHooksResource(self)
        self.cards = cards.CardsResource(self)
        self.certs = certs.CertsResource(self)
        self.config = config.ConfigResource(self)
        self.connector = connector.ConnectorResource(self)
        self.consumer = consumer.ConsumerResource(self)
        self.consent_requests = consent_requests.ConsentRequestsResource(self)
        self.consumers = consumers.ConsumersResource(self)
        self.customers_minimal = customers_minimal.CustomersMinimalResource(self)
        self.database = database.DatabaseResource(self)
        self.development = development.DevelopmentResource(self)
        self.dynamic_registration = dynamic_registration.DynamicRegistrationResource(self)
        self.endpoints = endpoints.EndpointsResource(self)
        self.entitlement_requests = entitlement_requests.EntitlementRequestsResource(self)
        self.entitlements = entitlements.EntitlementsResource(self)
        self.jwks_uris = jwks_uris.JwksUrisResource(self)
        self.management = management.ManagementResource(self)
        self.authentication_type_validations = authentication_type_validations.AuthenticationTypeValidationsResource(
            self
        )
        self.standing_orders = standing_orders.StandingOrdersResource(self)
        self.dynamic_endpoints = dynamic_endpoints.DynamicEndpointsResource(self)
        self.dynamic_message_docs = dynamic_message_docs.DynamicMessageDocsResource(self)
        self.dynamic_resource_docs = dynamic_resource_docs.DynamicResourceDocsResource(self)
        self.endpoint_mappings = endpoint_mappings.EndpointMappingsResource(self)
        self.fast_firehose_accounts = fast_firehose_accounts.FastFirehoseAccountsResource(self)
        self.cascading_banks = cascading_banks.CascadingBanksResource(self)
        self.connector_methods = connector_methods.ConnectorMethodsResource(self)
        self.json_schema_validations = json_schema_validations.JsonSchemaValidationsResource(self)
        self.method_routings = method_routings.MethodRoutingsResource(self)
        self.metrics = metrics.MetricsResource(self)
        self.system_dynamic_entities = system_dynamic_entities.SystemDynamicEntitiesResource(self)
        self.system_integrity = system_integrity.SystemIntegrityResource(self)
        self.webui_props = webui_props.WebuiPropsResource(self)
        self.documentation = documentation.DocumentationResource(self)
        self.consent = consent.ConsentResource(self)
        self.correlated_entities = correlated_entities.CorrelatedEntitiesResource(self)
        self.dynamic_entities = dynamic_entities.DynamicEntitiesResource(self)
        self.mtls = mtls.MtlsResource(self)
        self.spaces = spaces.SpacesResource(self)
        self.user = user.UserResource(self)
        self.rate_limits = rate_limits.RateLimitsResource(self)
        self.regulated_entities = regulated_entities.RegulatedEntitiesResource(self)
        self.resource_docs = resource_docs.ResourceDocsResource(self)
        self.roles = roles.RolesResource(self)
        self.sandbox = sandbox.SandboxResource(self)
        self.search = search.SearchResource(self)
        self.system_views = system_views.SystemViewsResource(self)
        self.user_entitlements = user_entitlements.UserEntitlementsResource(self)
        self.with_raw_response = ObpAPIWithRawResponse(self)
        self.with_streaming_response = ObpAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncObpAPI(AsyncAPIClient):
    accounts: accounts.AsyncAccountsResource
    adapter: adapter.AsyncAdapterResource
    api_collections: api_collections.AsyncAPICollectionsResource
    api: api.AsyncAPIResource
    banks: banks.AsyncBanksResource
    accounts_held: accounts_held.AsyncAccountsHeldResource
    counterparties: counterparties.AsyncCounterpartiesResource
    transactions: transactions.AsyncTransactionsResource
    customer_account_links: customer_account_links.AsyncCustomerAccountLinksResource
    permissions: permissions.AsyncPermissionsResource
    account_products: account_products.AsyncAccountProductsResource
    transaction_requests: transaction_requests.AsyncTransactionRequestsResource
    bank_accounts: bank_accounts.AsyncBankAccountsResource
    consents: consents.AsyncConsentsResource
    crm_events: crm_events.AsyncCRMEventsResource
    currencies: currencies.AsyncCurrenciesResource
    customers: customers.AsyncCustomersResource
    product_collections: product_collections.AsyncProductCollectionsResource
    product_tree: product_tree.AsyncProductTreeResource
    products: products.AsyncProductsResource
    public_accounts: public_accounts.AsyncPublicAccountsResource
    user_invitations: user_invitations.AsyncUserInvitationsResource
    user_customer_links: user_customer_links.AsyncUserCustomerLinksResource
    users: users.AsyncUsersResource
    views: views.AsyncViewsResource
    web_hooks: web_hooks.AsyncWebHooksResource
    cards: cards.AsyncCardsResource
    certs: certs.AsyncCertsResource
    config: config.AsyncConfigResource
    connector: connector.AsyncConnectorResource
    consumer: consumer.AsyncConsumerResource
    consent_requests: consent_requests.AsyncConsentRequestsResource
    consumers: consumers.AsyncConsumersResource
    customers_minimal: customers_minimal.AsyncCustomersMinimalResource
    database: database.AsyncDatabaseResource
    development: development.AsyncDevelopmentResource
    dynamic_registration: dynamic_registration.AsyncDynamicRegistrationResource
    endpoints: endpoints.AsyncEndpointsResource
    entitlement_requests: entitlement_requests.AsyncEntitlementRequestsResource
    entitlements: entitlements.AsyncEntitlementsResource
    jwks_uris: jwks_uris.AsyncJwksUrisResource
    management: management.AsyncManagementResource
    authentication_type_validations: authentication_type_validations.AsyncAuthenticationTypeValidationsResource
    standing_orders: standing_orders.AsyncStandingOrdersResource
    dynamic_endpoints: dynamic_endpoints.AsyncDynamicEndpointsResource
    dynamic_message_docs: dynamic_message_docs.AsyncDynamicMessageDocsResource
    dynamic_resource_docs: dynamic_resource_docs.AsyncDynamicResourceDocsResource
    endpoint_mappings: endpoint_mappings.AsyncEndpointMappingsResource
    fast_firehose_accounts: fast_firehose_accounts.AsyncFastFirehoseAccountsResource
    cascading_banks: cascading_banks.AsyncCascadingBanksResource
    connector_methods: connector_methods.AsyncConnectorMethodsResource
    json_schema_validations: json_schema_validations.AsyncJsonSchemaValidationsResource
    method_routings: method_routings.AsyncMethodRoutingsResource
    metrics: metrics.AsyncMetricsResource
    system_dynamic_entities: system_dynamic_entities.AsyncSystemDynamicEntitiesResource
    system_integrity: system_integrity.AsyncSystemIntegrityResource
    webui_props: webui_props.AsyncWebuiPropsResource
    documentation: documentation.AsyncDocumentationResource
    consent: consent.AsyncConsentResource
    correlated_entities: correlated_entities.AsyncCorrelatedEntitiesResource
    dynamic_entities: dynamic_entities.AsyncDynamicEntitiesResource
    mtls: mtls.AsyncMtlsResource
    spaces: spaces.AsyncSpacesResource
    user: user.AsyncUserResource
    rate_limits: rate_limits.AsyncRateLimitsResource
    regulated_entities: regulated_entities.AsyncRegulatedEntitiesResource
    resource_docs: resource_docs.AsyncResourceDocsResource
    roles: roles.AsyncRolesResource
    sandbox: sandbox.AsyncSandboxResource
    search: search.AsyncSearchResource
    system_views: system_views.AsyncSystemViewsResource
    user_entitlements: user_entitlements.AsyncUserEntitlementsResource
    with_raw_response: AsyncObpAPIWithRawResponse
    with_streaming_response: AsyncObpAPIWithStreamedResponse

    # client options

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async obp-api client instance."""
        self._environment = environment

        base_url_env = os.environ.get("OBP_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `OBP_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AsyncAccountsResource(self)
        self.adapter = adapter.AsyncAdapterResource(self)
        self.api_collections = api_collections.AsyncAPICollectionsResource(self)
        self.api = api.AsyncAPIResource(self)
        self.banks = banks.AsyncBanksResource(self)
        self.accounts_held = accounts_held.AsyncAccountsHeldResource(self)
        self.counterparties = counterparties.AsyncCounterpartiesResource(self)
        self.transactions = transactions.AsyncTransactionsResource(self)
        self.customer_account_links = customer_account_links.AsyncCustomerAccountLinksResource(self)
        self.permissions = permissions.AsyncPermissionsResource(self)
        self.account_products = account_products.AsyncAccountProductsResource(self)
        self.transaction_requests = transaction_requests.AsyncTransactionRequestsResource(self)
        self.bank_accounts = bank_accounts.AsyncBankAccountsResource(self)
        self.consents = consents.AsyncConsentsResource(self)
        self.crm_events = crm_events.AsyncCRMEventsResource(self)
        self.currencies = currencies.AsyncCurrenciesResource(self)
        self.customers = customers.AsyncCustomersResource(self)
        self.product_collections = product_collections.AsyncProductCollectionsResource(self)
        self.product_tree = product_tree.AsyncProductTreeResource(self)
        self.products = products.AsyncProductsResource(self)
        self.public_accounts = public_accounts.AsyncPublicAccountsResource(self)
        self.user_invitations = user_invitations.AsyncUserInvitationsResource(self)
        self.user_customer_links = user_customer_links.AsyncUserCustomerLinksResource(self)
        self.users = users.AsyncUsersResource(self)
        self.views = views.AsyncViewsResource(self)
        self.web_hooks = web_hooks.AsyncWebHooksResource(self)
        self.cards = cards.AsyncCardsResource(self)
        self.certs = certs.AsyncCertsResource(self)
        self.config = config.AsyncConfigResource(self)
        self.connector = connector.AsyncConnectorResource(self)
        self.consumer = consumer.AsyncConsumerResource(self)
        self.consent_requests = consent_requests.AsyncConsentRequestsResource(self)
        self.consumers = consumers.AsyncConsumersResource(self)
        self.customers_minimal = customers_minimal.AsyncCustomersMinimalResource(self)
        self.database = database.AsyncDatabaseResource(self)
        self.development = development.AsyncDevelopmentResource(self)
        self.dynamic_registration = dynamic_registration.AsyncDynamicRegistrationResource(self)
        self.endpoints = endpoints.AsyncEndpointsResource(self)
        self.entitlement_requests = entitlement_requests.AsyncEntitlementRequestsResource(self)
        self.entitlements = entitlements.AsyncEntitlementsResource(self)
        self.jwks_uris = jwks_uris.AsyncJwksUrisResource(self)
        self.management = management.AsyncManagementResource(self)
        self.authentication_type_validations = (
            authentication_type_validations.AsyncAuthenticationTypeValidationsResource(self)
        )
        self.standing_orders = standing_orders.AsyncStandingOrdersResource(self)
        self.dynamic_endpoints = dynamic_endpoints.AsyncDynamicEndpointsResource(self)
        self.dynamic_message_docs = dynamic_message_docs.AsyncDynamicMessageDocsResource(self)
        self.dynamic_resource_docs = dynamic_resource_docs.AsyncDynamicResourceDocsResource(self)
        self.endpoint_mappings = endpoint_mappings.AsyncEndpointMappingsResource(self)
        self.fast_firehose_accounts = fast_firehose_accounts.AsyncFastFirehoseAccountsResource(self)
        self.cascading_banks = cascading_banks.AsyncCascadingBanksResource(self)
        self.connector_methods = connector_methods.AsyncConnectorMethodsResource(self)
        self.json_schema_validations = json_schema_validations.AsyncJsonSchemaValidationsResource(self)
        self.method_routings = method_routings.AsyncMethodRoutingsResource(self)
        self.metrics = metrics.AsyncMetricsResource(self)
        self.system_dynamic_entities = system_dynamic_entities.AsyncSystemDynamicEntitiesResource(self)
        self.system_integrity = system_integrity.AsyncSystemIntegrityResource(self)
        self.webui_props = webui_props.AsyncWebuiPropsResource(self)
        self.documentation = documentation.AsyncDocumentationResource(self)
        self.consent = consent.AsyncConsentResource(self)
        self.correlated_entities = correlated_entities.AsyncCorrelatedEntitiesResource(self)
        self.dynamic_entities = dynamic_entities.AsyncDynamicEntitiesResource(self)
        self.mtls = mtls.AsyncMtlsResource(self)
        self.spaces = spaces.AsyncSpacesResource(self)
        self.user = user.AsyncUserResource(self)
        self.rate_limits = rate_limits.AsyncRateLimitsResource(self)
        self.regulated_entities = regulated_entities.AsyncRegulatedEntitiesResource(self)
        self.resource_docs = resource_docs.AsyncResourceDocsResource(self)
        self.roles = roles.AsyncRolesResource(self)
        self.sandbox = sandbox.AsyncSandboxResource(self)
        self.search = search.AsyncSearchResource(self)
        self.system_views = system_views.AsyncSystemViewsResource(self)
        self.user_entitlements = user_entitlements.AsyncUserEntitlementsResource(self)
        self.with_raw_response = AsyncObpAPIWithRawResponse(self)
        self.with_streaming_response = AsyncObpAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ObpAPIWithRawResponse:
    def __init__(self, client: ObpAPI) -> None:
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.adapter = adapter.AdapterResourceWithRawResponse(client.adapter)
        self.api_collections = api_collections.APICollectionsResourceWithRawResponse(client.api_collections)
        self.api = api.APIResourceWithRawResponse(client.api)
        self.banks = banks.BanksResourceWithRawResponse(client.banks)
        self.accounts_held = accounts_held.AccountsHeldResourceWithRawResponse(client.accounts_held)
        self.counterparties = counterparties.CounterpartiesResourceWithRawResponse(client.counterparties)
        self.transactions = transactions.TransactionsResourceWithRawResponse(client.transactions)
        self.customer_account_links = customer_account_links.CustomerAccountLinksResourceWithRawResponse(
            client.customer_account_links
        )
        self.permissions = permissions.PermissionsResourceWithRawResponse(client.permissions)
        self.account_products = account_products.AccountProductsResourceWithRawResponse(client.account_products)
        self.transaction_requests = transaction_requests.TransactionRequestsResourceWithRawResponse(
            client.transaction_requests
        )
        self.bank_accounts = bank_accounts.BankAccountsResourceWithRawResponse(client.bank_accounts)
        self.consents = consents.ConsentsResourceWithRawResponse(client.consents)
        self.crm_events = crm_events.CRMEventsResourceWithRawResponse(client.crm_events)
        self.currencies = currencies.CurrenciesResourceWithRawResponse(client.currencies)
        self.customers = customers.CustomersResourceWithRawResponse(client.customers)
        self.product_collections = product_collections.ProductCollectionsResourceWithRawResponse(
            client.product_collections
        )
        self.product_tree = product_tree.ProductTreeResourceWithRawResponse(client.product_tree)
        self.products = products.ProductsResourceWithRawResponse(client.products)
        self.public_accounts = public_accounts.PublicAccountsResourceWithRawResponse(client.public_accounts)
        self.user_invitations = user_invitations.UserInvitationsResourceWithRawResponse(client.user_invitations)
        self.user_customer_links = user_customer_links.UserCustomerLinksResourceWithRawResponse(
            client.user_customer_links
        )
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.views = views.ViewsResourceWithRawResponse(client.views)
        self.web_hooks = web_hooks.WebHooksResourceWithRawResponse(client.web_hooks)
        self.cards = cards.CardsResourceWithRawResponse(client.cards)
        self.certs = certs.CertsResourceWithRawResponse(client.certs)
        self.config = config.ConfigResourceWithRawResponse(client.config)
        self.connector = connector.ConnectorResourceWithRawResponse(client.connector)
        self.consumer = consumer.ConsumerResourceWithRawResponse(client.consumer)
        self.consent_requests = consent_requests.ConsentRequestsResourceWithRawResponse(client.consent_requests)
        self.consumers = consumers.ConsumersResourceWithRawResponse(client.consumers)
        self.customers_minimal = customers_minimal.CustomersMinimalResourceWithRawResponse(client.customers_minimal)
        self.database = database.DatabaseResourceWithRawResponse(client.database)
        self.development = development.DevelopmentResourceWithRawResponse(client.development)
        self.dynamic_registration = dynamic_registration.DynamicRegistrationResourceWithRawResponse(
            client.dynamic_registration
        )
        self.endpoints = endpoints.EndpointsResourceWithRawResponse(client.endpoints)
        self.entitlement_requests = entitlement_requests.EntitlementRequestsResourceWithRawResponse(
            client.entitlement_requests
        )
        self.entitlements = entitlements.EntitlementsResourceWithRawResponse(client.entitlements)
        self.jwks_uris = jwks_uris.JwksUrisResourceWithRawResponse(client.jwks_uris)
        self.management = management.ManagementResourceWithRawResponse(client.management)
        self.authentication_type_validations = (
            authentication_type_validations.AuthenticationTypeValidationsResourceWithRawResponse(
                client.authentication_type_validations
            )
        )
        self.standing_orders = standing_orders.StandingOrdersResourceWithRawResponse(client.standing_orders)
        self.dynamic_endpoints = dynamic_endpoints.DynamicEndpointsResourceWithRawResponse(client.dynamic_endpoints)
        self.dynamic_message_docs = dynamic_message_docs.DynamicMessageDocsResourceWithRawResponse(
            client.dynamic_message_docs
        )
        self.dynamic_resource_docs = dynamic_resource_docs.DynamicResourceDocsResourceWithRawResponse(
            client.dynamic_resource_docs
        )
        self.endpoint_mappings = endpoint_mappings.EndpointMappingsResourceWithRawResponse(client.endpoint_mappings)
        self.fast_firehose_accounts = fast_firehose_accounts.FastFirehoseAccountsResourceWithRawResponse(
            client.fast_firehose_accounts
        )
        self.cascading_banks = cascading_banks.CascadingBanksResourceWithRawResponse(client.cascading_banks)
        self.connector_methods = connector_methods.ConnectorMethodsResourceWithRawResponse(client.connector_methods)
        self.json_schema_validations = json_schema_validations.JsonSchemaValidationsResourceWithRawResponse(
            client.json_schema_validations
        )
        self.method_routings = method_routings.MethodRoutingsResourceWithRawResponse(client.method_routings)
        self.metrics = metrics.MetricsResourceWithRawResponse(client.metrics)
        self.system_dynamic_entities = system_dynamic_entities.SystemDynamicEntitiesResourceWithRawResponse(
            client.system_dynamic_entities
        )
        self.system_integrity = system_integrity.SystemIntegrityResourceWithRawResponse(client.system_integrity)
        self.webui_props = webui_props.WebuiPropsResourceWithRawResponse(client.webui_props)
        self.documentation = documentation.DocumentationResourceWithRawResponse(client.documentation)
        self.consent = consent.ConsentResourceWithRawResponse(client.consent)
        self.correlated_entities = correlated_entities.CorrelatedEntitiesResourceWithRawResponse(
            client.correlated_entities
        )
        self.dynamic_entities = dynamic_entities.DynamicEntitiesResourceWithRawResponse(client.dynamic_entities)
        self.mtls = mtls.MtlsResourceWithRawResponse(client.mtls)
        self.spaces = spaces.SpacesResourceWithRawResponse(client.spaces)
        self.user = user.UserResourceWithRawResponse(client.user)
        self.rate_limits = rate_limits.RateLimitsResourceWithRawResponse(client.rate_limits)
        self.regulated_entities = regulated_entities.RegulatedEntitiesResourceWithRawResponse(client.regulated_entities)
        self.resource_docs = resource_docs.ResourceDocsResourceWithRawResponse(client.resource_docs)
        self.roles = roles.RolesResourceWithRawResponse(client.roles)
        self.sandbox = sandbox.SandboxResourceWithRawResponse(client.sandbox)
        self.search = search.SearchResourceWithRawResponse(client.search)
        self.system_views = system_views.SystemViewsResourceWithRawResponse(client.system_views)
        self.user_entitlements = user_entitlements.UserEntitlementsResourceWithRawResponse(client.user_entitlements)


class AsyncObpAPIWithRawResponse:
    def __init__(self, client: AsyncObpAPI) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.adapter = adapter.AsyncAdapterResourceWithRawResponse(client.adapter)
        self.api_collections = api_collections.AsyncAPICollectionsResourceWithRawResponse(client.api_collections)
        self.api = api.AsyncAPIResourceWithRawResponse(client.api)
        self.banks = banks.AsyncBanksResourceWithRawResponse(client.banks)
        self.accounts_held = accounts_held.AsyncAccountsHeldResourceWithRawResponse(client.accounts_held)
        self.counterparties = counterparties.AsyncCounterpartiesResourceWithRawResponse(client.counterparties)
        self.transactions = transactions.AsyncTransactionsResourceWithRawResponse(client.transactions)
        self.customer_account_links = customer_account_links.AsyncCustomerAccountLinksResourceWithRawResponse(
            client.customer_account_links
        )
        self.permissions = permissions.AsyncPermissionsResourceWithRawResponse(client.permissions)
        self.account_products = account_products.AsyncAccountProductsResourceWithRawResponse(client.account_products)
        self.transaction_requests = transaction_requests.AsyncTransactionRequestsResourceWithRawResponse(
            client.transaction_requests
        )
        self.bank_accounts = bank_accounts.AsyncBankAccountsResourceWithRawResponse(client.bank_accounts)
        self.consents = consents.AsyncConsentsResourceWithRawResponse(client.consents)
        self.crm_events = crm_events.AsyncCRMEventsResourceWithRawResponse(client.crm_events)
        self.currencies = currencies.AsyncCurrenciesResourceWithRawResponse(client.currencies)
        self.customers = customers.AsyncCustomersResourceWithRawResponse(client.customers)
        self.product_collections = product_collections.AsyncProductCollectionsResourceWithRawResponse(
            client.product_collections
        )
        self.product_tree = product_tree.AsyncProductTreeResourceWithRawResponse(client.product_tree)
        self.products = products.AsyncProductsResourceWithRawResponse(client.products)
        self.public_accounts = public_accounts.AsyncPublicAccountsResourceWithRawResponse(client.public_accounts)
        self.user_invitations = user_invitations.AsyncUserInvitationsResourceWithRawResponse(client.user_invitations)
        self.user_customer_links = user_customer_links.AsyncUserCustomerLinksResourceWithRawResponse(
            client.user_customer_links
        )
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.views = views.AsyncViewsResourceWithRawResponse(client.views)
        self.web_hooks = web_hooks.AsyncWebHooksResourceWithRawResponse(client.web_hooks)
        self.cards = cards.AsyncCardsResourceWithRawResponse(client.cards)
        self.certs = certs.AsyncCertsResourceWithRawResponse(client.certs)
        self.config = config.AsyncConfigResourceWithRawResponse(client.config)
        self.connector = connector.AsyncConnectorResourceWithRawResponse(client.connector)
        self.consumer = consumer.AsyncConsumerResourceWithRawResponse(client.consumer)
        self.consent_requests = consent_requests.AsyncConsentRequestsResourceWithRawResponse(client.consent_requests)
        self.consumers = consumers.AsyncConsumersResourceWithRawResponse(client.consumers)
        self.customers_minimal = customers_minimal.AsyncCustomersMinimalResourceWithRawResponse(
            client.customers_minimal
        )
        self.database = database.AsyncDatabaseResourceWithRawResponse(client.database)
        self.development = development.AsyncDevelopmentResourceWithRawResponse(client.development)
        self.dynamic_registration = dynamic_registration.AsyncDynamicRegistrationResourceWithRawResponse(
            client.dynamic_registration
        )
        self.endpoints = endpoints.AsyncEndpointsResourceWithRawResponse(client.endpoints)
        self.entitlement_requests = entitlement_requests.AsyncEntitlementRequestsResourceWithRawResponse(
            client.entitlement_requests
        )
        self.entitlements = entitlements.AsyncEntitlementsResourceWithRawResponse(client.entitlements)
        self.jwks_uris = jwks_uris.AsyncJwksUrisResourceWithRawResponse(client.jwks_uris)
        self.management = management.AsyncManagementResourceWithRawResponse(client.management)
        self.authentication_type_validations = (
            authentication_type_validations.AsyncAuthenticationTypeValidationsResourceWithRawResponse(
                client.authentication_type_validations
            )
        )
        self.standing_orders = standing_orders.AsyncStandingOrdersResourceWithRawResponse(client.standing_orders)
        self.dynamic_endpoints = dynamic_endpoints.AsyncDynamicEndpointsResourceWithRawResponse(
            client.dynamic_endpoints
        )
        self.dynamic_message_docs = dynamic_message_docs.AsyncDynamicMessageDocsResourceWithRawResponse(
            client.dynamic_message_docs
        )
        self.dynamic_resource_docs = dynamic_resource_docs.AsyncDynamicResourceDocsResourceWithRawResponse(
            client.dynamic_resource_docs
        )
        self.endpoint_mappings = endpoint_mappings.AsyncEndpointMappingsResourceWithRawResponse(
            client.endpoint_mappings
        )
        self.fast_firehose_accounts = fast_firehose_accounts.AsyncFastFirehoseAccountsResourceWithRawResponse(
            client.fast_firehose_accounts
        )
        self.cascading_banks = cascading_banks.AsyncCascadingBanksResourceWithRawResponse(client.cascading_banks)
        self.connector_methods = connector_methods.AsyncConnectorMethodsResourceWithRawResponse(
            client.connector_methods
        )
        self.json_schema_validations = json_schema_validations.AsyncJsonSchemaValidationsResourceWithRawResponse(
            client.json_schema_validations
        )
        self.method_routings = method_routings.AsyncMethodRoutingsResourceWithRawResponse(client.method_routings)
        self.metrics = metrics.AsyncMetricsResourceWithRawResponse(client.metrics)
        self.system_dynamic_entities = system_dynamic_entities.AsyncSystemDynamicEntitiesResourceWithRawResponse(
            client.system_dynamic_entities
        )
        self.system_integrity = system_integrity.AsyncSystemIntegrityResourceWithRawResponse(client.system_integrity)
        self.webui_props = webui_props.AsyncWebuiPropsResourceWithRawResponse(client.webui_props)
        self.documentation = documentation.AsyncDocumentationResourceWithRawResponse(client.documentation)
        self.consent = consent.AsyncConsentResourceWithRawResponse(client.consent)
        self.correlated_entities = correlated_entities.AsyncCorrelatedEntitiesResourceWithRawResponse(
            client.correlated_entities
        )
        self.dynamic_entities = dynamic_entities.AsyncDynamicEntitiesResourceWithRawResponse(client.dynamic_entities)
        self.mtls = mtls.AsyncMtlsResourceWithRawResponse(client.mtls)
        self.spaces = spaces.AsyncSpacesResourceWithRawResponse(client.spaces)
        self.user = user.AsyncUserResourceWithRawResponse(client.user)
        self.rate_limits = rate_limits.AsyncRateLimitsResourceWithRawResponse(client.rate_limits)
        self.regulated_entities = regulated_entities.AsyncRegulatedEntitiesResourceWithRawResponse(
            client.regulated_entities
        )
        self.resource_docs = resource_docs.AsyncResourceDocsResourceWithRawResponse(client.resource_docs)
        self.roles = roles.AsyncRolesResourceWithRawResponse(client.roles)
        self.sandbox = sandbox.AsyncSandboxResourceWithRawResponse(client.sandbox)
        self.search = search.AsyncSearchResourceWithRawResponse(client.search)
        self.system_views = system_views.AsyncSystemViewsResourceWithRawResponse(client.system_views)
        self.user_entitlements = user_entitlements.AsyncUserEntitlementsResourceWithRawResponse(
            client.user_entitlements
        )


class ObpAPIWithStreamedResponse:
    def __init__(self, client: ObpAPI) -> None:
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.adapter = adapter.AdapterResourceWithStreamingResponse(client.adapter)
        self.api_collections = api_collections.APICollectionsResourceWithStreamingResponse(client.api_collections)
        self.api = api.APIResourceWithStreamingResponse(client.api)
        self.banks = banks.BanksResourceWithStreamingResponse(client.banks)
        self.accounts_held = accounts_held.AccountsHeldResourceWithStreamingResponse(client.accounts_held)
        self.counterparties = counterparties.CounterpartiesResourceWithStreamingResponse(client.counterparties)
        self.transactions = transactions.TransactionsResourceWithStreamingResponse(client.transactions)
        self.customer_account_links = customer_account_links.CustomerAccountLinksResourceWithStreamingResponse(
            client.customer_account_links
        )
        self.permissions = permissions.PermissionsResourceWithStreamingResponse(client.permissions)
        self.account_products = account_products.AccountProductsResourceWithStreamingResponse(client.account_products)
        self.transaction_requests = transaction_requests.TransactionRequestsResourceWithStreamingResponse(
            client.transaction_requests
        )
        self.bank_accounts = bank_accounts.BankAccountsResourceWithStreamingResponse(client.bank_accounts)
        self.consents = consents.ConsentsResourceWithStreamingResponse(client.consents)
        self.crm_events = crm_events.CRMEventsResourceWithStreamingResponse(client.crm_events)
        self.currencies = currencies.CurrenciesResourceWithStreamingResponse(client.currencies)
        self.customers = customers.CustomersResourceWithStreamingResponse(client.customers)
        self.product_collections = product_collections.ProductCollectionsResourceWithStreamingResponse(
            client.product_collections
        )
        self.product_tree = product_tree.ProductTreeResourceWithStreamingResponse(client.product_tree)
        self.products = products.ProductsResourceWithStreamingResponse(client.products)
        self.public_accounts = public_accounts.PublicAccountsResourceWithStreamingResponse(client.public_accounts)
        self.user_invitations = user_invitations.UserInvitationsResourceWithStreamingResponse(client.user_invitations)
        self.user_customer_links = user_customer_links.UserCustomerLinksResourceWithStreamingResponse(
            client.user_customer_links
        )
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.views = views.ViewsResourceWithStreamingResponse(client.views)
        self.web_hooks = web_hooks.WebHooksResourceWithStreamingResponse(client.web_hooks)
        self.cards = cards.CardsResourceWithStreamingResponse(client.cards)
        self.certs = certs.CertsResourceWithStreamingResponse(client.certs)
        self.config = config.ConfigResourceWithStreamingResponse(client.config)
        self.connector = connector.ConnectorResourceWithStreamingResponse(client.connector)
        self.consumer = consumer.ConsumerResourceWithStreamingResponse(client.consumer)
        self.consent_requests = consent_requests.ConsentRequestsResourceWithStreamingResponse(client.consent_requests)
        self.consumers = consumers.ConsumersResourceWithStreamingResponse(client.consumers)
        self.customers_minimal = customers_minimal.CustomersMinimalResourceWithStreamingResponse(
            client.customers_minimal
        )
        self.database = database.DatabaseResourceWithStreamingResponse(client.database)
        self.development = development.DevelopmentResourceWithStreamingResponse(client.development)
        self.dynamic_registration = dynamic_registration.DynamicRegistrationResourceWithStreamingResponse(
            client.dynamic_registration
        )
        self.endpoints = endpoints.EndpointsResourceWithStreamingResponse(client.endpoints)
        self.entitlement_requests = entitlement_requests.EntitlementRequestsResourceWithStreamingResponse(
            client.entitlement_requests
        )
        self.entitlements = entitlements.EntitlementsResourceWithStreamingResponse(client.entitlements)
        self.jwks_uris = jwks_uris.JwksUrisResourceWithStreamingResponse(client.jwks_uris)
        self.management = management.ManagementResourceWithStreamingResponse(client.management)
        self.authentication_type_validations = (
            authentication_type_validations.AuthenticationTypeValidationsResourceWithStreamingResponse(
                client.authentication_type_validations
            )
        )
        self.standing_orders = standing_orders.StandingOrdersResourceWithStreamingResponse(client.standing_orders)
        self.dynamic_endpoints = dynamic_endpoints.DynamicEndpointsResourceWithStreamingResponse(
            client.dynamic_endpoints
        )
        self.dynamic_message_docs = dynamic_message_docs.DynamicMessageDocsResourceWithStreamingResponse(
            client.dynamic_message_docs
        )
        self.dynamic_resource_docs = dynamic_resource_docs.DynamicResourceDocsResourceWithStreamingResponse(
            client.dynamic_resource_docs
        )
        self.endpoint_mappings = endpoint_mappings.EndpointMappingsResourceWithStreamingResponse(
            client.endpoint_mappings
        )
        self.fast_firehose_accounts = fast_firehose_accounts.FastFirehoseAccountsResourceWithStreamingResponse(
            client.fast_firehose_accounts
        )
        self.cascading_banks = cascading_banks.CascadingBanksResourceWithStreamingResponse(client.cascading_banks)
        self.connector_methods = connector_methods.ConnectorMethodsResourceWithStreamingResponse(
            client.connector_methods
        )
        self.json_schema_validations = json_schema_validations.JsonSchemaValidationsResourceWithStreamingResponse(
            client.json_schema_validations
        )
        self.method_routings = method_routings.MethodRoutingsResourceWithStreamingResponse(client.method_routings)
        self.metrics = metrics.MetricsResourceWithStreamingResponse(client.metrics)
        self.system_dynamic_entities = system_dynamic_entities.SystemDynamicEntitiesResourceWithStreamingResponse(
            client.system_dynamic_entities
        )
        self.system_integrity = system_integrity.SystemIntegrityResourceWithStreamingResponse(client.system_integrity)
        self.webui_props = webui_props.WebuiPropsResourceWithStreamingResponse(client.webui_props)
        self.documentation = documentation.DocumentationResourceWithStreamingResponse(client.documentation)
        self.consent = consent.ConsentResourceWithStreamingResponse(client.consent)
        self.correlated_entities = correlated_entities.CorrelatedEntitiesResourceWithStreamingResponse(
            client.correlated_entities
        )
        self.dynamic_entities = dynamic_entities.DynamicEntitiesResourceWithStreamingResponse(client.dynamic_entities)
        self.mtls = mtls.MtlsResourceWithStreamingResponse(client.mtls)
        self.spaces = spaces.SpacesResourceWithStreamingResponse(client.spaces)
        self.user = user.UserResourceWithStreamingResponse(client.user)
        self.rate_limits = rate_limits.RateLimitsResourceWithStreamingResponse(client.rate_limits)
        self.regulated_entities = regulated_entities.RegulatedEntitiesResourceWithStreamingResponse(
            client.regulated_entities
        )
        self.resource_docs = resource_docs.ResourceDocsResourceWithStreamingResponse(client.resource_docs)
        self.roles = roles.RolesResourceWithStreamingResponse(client.roles)
        self.sandbox = sandbox.SandboxResourceWithStreamingResponse(client.sandbox)
        self.search = search.SearchResourceWithStreamingResponse(client.search)
        self.system_views = system_views.SystemViewsResourceWithStreamingResponse(client.system_views)
        self.user_entitlements = user_entitlements.UserEntitlementsResourceWithStreamingResponse(
            client.user_entitlements
        )


class AsyncObpAPIWithStreamedResponse:
    def __init__(self, client: AsyncObpAPI) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.adapter = adapter.AsyncAdapterResourceWithStreamingResponse(client.adapter)
        self.api_collections = api_collections.AsyncAPICollectionsResourceWithStreamingResponse(client.api_collections)
        self.api = api.AsyncAPIResourceWithStreamingResponse(client.api)
        self.banks = banks.AsyncBanksResourceWithStreamingResponse(client.banks)
        self.accounts_held = accounts_held.AsyncAccountsHeldResourceWithStreamingResponse(client.accounts_held)
        self.counterparties = counterparties.AsyncCounterpartiesResourceWithStreamingResponse(client.counterparties)
        self.transactions = transactions.AsyncTransactionsResourceWithStreamingResponse(client.transactions)
        self.customer_account_links = customer_account_links.AsyncCustomerAccountLinksResourceWithStreamingResponse(
            client.customer_account_links
        )
        self.permissions = permissions.AsyncPermissionsResourceWithStreamingResponse(client.permissions)
        self.account_products = account_products.AsyncAccountProductsResourceWithStreamingResponse(
            client.account_products
        )
        self.transaction_requests = transaction_requests.AsyncTransactionRequestsResourceWithStreamingResponse(
            client.transaction_requests
        )
        self.bank_accounts = bank_accounts.AsyncBankAccountsResourceWithStreamingResponse(client.bank_accounts)
        self.consents = consents.AsyncConsentsResourceWithStreamingResponse(client.consents)
        self.crm_events = crm_events.AsyncCRMEventsResourceWithStreamingResponse(client.crm_events)
        self.currencies = currencies.AsyncCurrenciesResourceWithStreamingResponse(client.currencies)
        self.customers = customers.AsyncCustomersResourceWithStreamingResponse(client.customers)
        self.product_collections = product_collections.AsyncProductCollectionsResourceWithStreamingResponse(
            client.product_collections
        )
        self.product_tree = product_tree.AsyncProductTreeResourceWithStreamingResponse(client.product_tree)
        self.products = products.AsyncProductsResourceWithStreamingResponse(client.products)
        self.public_accounts = public_accounts.AsyncPublicAccountsResourceWithStreamingResponse(client.public_accounts)
        self.user_invitations = user_invitations.AsyncUserInvitationsResourceWithStreamingResponse(
            client.user_invitations
        )
        self.user_customer_links = user_customer_links.AsyncUserCustomerLinksResourceWithStreamingResponse(
            client.user_customer_links
        )
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.views = views.AsyncViewsResourceWithStreamingResponse(client.views)
        self.web_hooks = web_hooks.AsyncWebHooksResourceWithStreamingResponse(client.web_hooks)
        self.cards = cards.AsyncCardsResourceWithStreamingResponse(client.cards)
        self.certs = certs.AsyncCertsResourceWithStreamingResponse(client.certs)
        self.config = config.AsyncConfigResourceWithStreamingResponse(client.config)
        self.connector = connector.AsyncConnectorResourceWithStreamingResponse(client.connector)
        self.consumer = consumer.AsyncConsumerResourceWithStreamingResponse(client.consumer)
        self.consent_requests = consent_requests.AsyncConsentRequestsResourceWithStreamingResponse(
            client.consent_requests
        )
        self.consumers = consumers.AsyncConsumersResourceWithStreamingResponse(client.consumers)
        self.customers_minimal = customers_minimal.AsyncCustomersMinimalResourceWithStreamingResponse(
            client.customers_minimal
        )
        self.database = database.AsyncDatabaseResourceWithStreamingResponse(client.database)
        self.development = development.AsyncDevelopmentResourceWithStreamingResponse(client.development)
        self.dynamic_registration = dynamic_registration.AsyncDynamicRegistrationResourceWithStreamingResponse(
            client.dynamic_registration
        )
        self.endpoints = endpoints.AsyncEndpointsResourceWithStreamingResponse(client.endpoints)
        self.entitlement_requests = entitlement_requests.AsyncEntitlementRequestsResourceWithStreamingResponse(
            client.entitlement_requests
        )
        self.entitlements = entitlements.AsyncEntitlementsResourceWithStreamingResponse(client.entitlements)
        self.jwks_uris = jwks_uris.AsyncJwksUrisResourceWithStreamingResponse(client.jwks_uris)
        self.management = management.AsyncManagementResourceWithStreamingResponse(client.management)
        self.authentication_type_validations = (
            authentication_type_validations.AsyncAuthenticationTypeValidationsResourceWithStreamingResponse(
                client.authentication_type_validations
            )
        )
        self.standing_orders = standing_orders.AsyncStandingOrdersResourceWithStreamingResponse(client.standing_orders)
        self.dynamic_endpoints = dynamic_endpoints.AsyncDynamicEndpointsResourceWithStreamingResponse(
            client.dynamic_endpoints
        )
        self.dynamic_message_docs = dynamic_message_docs.AsyncDynamicMessageDocsResourceWithStreamingResponse(
            client.dynamic_message_docs
        )
        self.dynamic_resource_docs = dynamic_resource_docs.AsyncDynamicResourceDocsResourceWithStreamingResponse(
            client.dynamic_resource_docs
        )
        self.endpoint_mappings = endpoint_mappings.AsyncEndpointMappingsResourceWithStreamingResponse(
            client.endpoint_mappings
        )
        self.fast_firehose_accounts = fast_firehose_accounts.AsyncFastFirehoseAccountsResourceWithStreamingResponse(
            client.fast_firehose_accounts
        )
        self.cascading_banks = cascading_banks.AsyncCascadingBanksResourceWithStreamingResponse(client.cascading_banks)
        self.connector_methods = connector_methods.AsyncConnectorMethodsResourceWithStreamingResponse(
            client.connector_methods
        )
        self.json_schema_validations = json_schema_validations.AsyncJsonSchemaValidationsResourceWithStreamingResponse(
            client.json_schema_validations
        )
        self.method_routings = method_routings.AsyncMethodRoutingsResourceWithStreamingResponse(client.method_routings)
        self.metrics = metrics.AsyncMetricsResourceWithStreamingResponse(client.metrics)
        self.system_dynamic_entities = system_dynamic_entities.AsyncSystemDynamicEntitiesResourceWithStreamingResponse(
            client.system_dynamic_entities
        )
        self.system_integrity = system_integrity.AsyncSystemIntegrityResourceWithStreamingResponse(
            client.system_integrity
        )
        self.webui_props = webui_props.AsyncWebuiPropsResourceWithStreamingResponse(client.webui_props)
        self.documentation = documentation.AsyncDocumentationResourceWithStreamingResponse(client.documentation)
        self.consent = consent.AsyncConsentResourceWithStreamingResponse(client.consent)
        self.correlated_entities = correlated_entities.AsyncCorrelatedEntitiesResourceWithStreamingResponse(
            client.correlated_entities
        )
        self.dynamic_entities = dynamic_entities.AsyncDynamicEntitiesResourceWithStreamingResponse(
            client.dynamic_entities
        )
        self.mtls = mtls.AsyncMtlsResourceWithStreamingResponse(client.mtls)
        self.spaces = spaces.AsyncSpacesResourceWithStreamingResponse(client.spaces)
        self.user = user.AsyncUserResourceWithStreamingResponse(client.user)
        self.rate_limits = rate_limits.AsyncRateLimitsResourceWithStreamingResponse(client.rate_limits)
        self.regulated_entities = regulated_entities.AsyncRegulatedEntitiesResourceWithStreamingResponse(
            client.regulated_entities
        )
        self.resource_docs = resource_docs.AsyncResourceDocsResourceWithStreamingResponse(client.resource_docs)
        self.roles = roles.AsyncRolesResourceWithStreamingResponse(client.roles)
        self.sandbox = sandbox.AsyncSandboxResourceWithStreamingResponse(client.sandbox)
        self.search = search.AsyncSearchResourceWithStreamingResponse(client.search)
        self.system_views = system_views.AsyncSystemViewsResourceWithStreamingResponse(client.system_views)
        self.user_entitlements = user_entitlements.AsyncUserEntitlementsResourceWithStreamingResponse(
            client.user_entitlements
        )


Client = ObpAPI

AsyncClient = AsyncObpAPI
