# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import transaction_request_create_params
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
from ..._base_client import make_request_options
from .transaction_request_attributes import (
    TransactionRequestAttributesResource,
    AsyncTransactionRequestAttributesResource,
    TransactionRequestAttributesResourceWithRawResponse,
    AsyncTransactionRequestAttributesResourceWithRawResponse,
    TransactionRequestAttributesResourceWithStreamingResponse,
    AsyncTransactionRequestAttributesResourceWithStreamingResponse,
)

__all__ = ["TransactionRequestsResource", "AsyncTransactionRequestsResource"]


class TransactionRequestsResource(SyncAPIResource):
    @cached_property
    def transaction_request_attributes(self) -> TransactionRequestAttributesResource:
        return TransactionRequestAttributesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionRequestsResourceWithRawResponse:
        return TransactionRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionRequestsResourceWithStreamingResponse:
        return TransactionRequestsResourceWithStreamingResponse(self)

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
        <p>When using CARD, the payee is set in the request body .</p><p>Money goes into the Counterparty in the request body.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href="https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate">https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href="https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href="https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests">here</a></p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/obp/v5.1.0/transaction-request-types/CARD/transaction-requests",
            body=maybe_transform(body, transaction_request_create_params.TransactionRequestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncTransactionRequestsResource(AsyncAPIResource):
    @cached_property
    def transaction_request_attributes(self) -> AsyncTransactionRequestAttributesResource:
        return AsyncTransactionRequestAttributesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionRequestsResourceWithRawResponse:
        return AsyncTransactionRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionRequestsResourceWithStreamingResponse:
        return AsyncTransactionRequestsResourceWithStreamingResponse(self)

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
        <p>When using CARD, the payee is set in the request body .</p><p>Money goes into the Counterparty in the request body.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href="https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate">https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href="https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href="https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests">here</a></p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/obp/v5.1.0/transaction-request-types/CARD/transaction-requests",
            body=await async_maybe_transform(body, transaction_request_create_params.TransactionRequestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class TransactionRequestsResourceWithRawResponse:
    def __init__(self, transaction_requests: TransactionRequestsResource) -> None:
        self._transaction_requests = transaction_requests

        self.create = to_custom_raw_response_wrapper(
            transaction_requests.create,
            BinaryAPIResponse,
        )

    @cached_property
    def transaction_request_attributes(self) -> TransactionRequestAttributesResourceWithRawResponse:
        return TransactionRequestAttributesResourceWithRawResponse(
            self._transaction_requests.transaction_request_attributes
        )


class AsyncTransactionRequestsResourceWithRawResponse:
    def __init__(self, transaction_requests: AsyncTransactionRequestsResource) -> None:
        self._transaction_requests = transaction_requests

        self.create = async_to_custom_raw_response_wrapper(
            transaction_requests.create,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def transaction_request_attributes(self) -> AsyncTransactionRequestAttributesResourceWithRawResponse:
        return AsyncTransactionRequestAttributesResourceWithRawResponse(
            self._transaction_requests.transaction_request_attributes
        )


class TransactionRequestsResourceWithStreamingResponse:
    def __init__(self, transaction_requests: TransactionRequestsResource) -> None:
        self._transaction_requests = transaction_requests

        self.create = to_custom_streamed_response_wrapper(
            transaction_requests.create,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def transaction_request_attributes(self) -> TransactionRequestAttributesResourceWithStreamingResponse:
        return TransactionRequestAttributesResourceWithStreamingResponse(
            self._transaction_requests.transaction_request_attributes
        )


class AsyncTransactionRequestsResourceWithStreamingResponse:
    def __init__(self, transaction_requests: AsyncTransactionRequestsResource) -> None:
        self._transaction_requests = transaction_requests

        self.create = async_to_custom_streamed_response_wrapper(
            transaction_requests.create,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def transaction_request_attributes(self) -> AsyncTransactionRequestAttributesResourceWithStreamingResponse:
        return AsyncTransactionRequestAttributesResourceWithStreamingResponse(
            self._transaction_requests.transaction_request_attributes
        )
