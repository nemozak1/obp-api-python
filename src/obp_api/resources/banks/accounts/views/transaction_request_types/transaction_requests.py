# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.banks.accounts.views.transaction_request_types import (
    transaction_request_create_params,
    transaction_request_challenge_params,
)

__all__ = ["TransactionRequestsResource", "AsyncTransactionRequestsResource"]


class TransactionRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionRequestsResourceWithRawResponse:
        return TransactionRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionRequestsResourceWithStreamingResponse:
        return TransactionRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        view_id: str,
        *,
        bank_id: str,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        <p>Special instructions for SIMPLE:</p><p>You can transfer money to the Bank Account Number or IBAN directly.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href="https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate">https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href="https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href="https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests">here</a></p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/obp/v5.1.0/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/SIMPLE/transaction-requests",
            body=maybe_transform(body, transaction_request_create_params.TransactionRequestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def challenge(
        self,
        transaction_request_id: str,
        *,
        bank_id: str,
        account_id: str,
        view_id: str,
        transaction_request_type: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        <p>In Sandbox mode, any string that can be converted to a positive integer will be accepted as an answer.</p><p>This endpoint totally depends on createTransactionRequest, it need get the following data from createTransactionRequest response body.</p><p>1)<code>TRANSACTION_REQUEST_TYPE</code> : is the same as createTransactionRequest request URL .</p><p>2)<code>TRANSACTION_REQUEST_ID</code> : is the <code>id</code> field in createTransactionRequest response body.</p><p>3) <code>id</code> :  is <code>challenge.id</code> field in createTransactionRequest response body.</p><p>4) <code>answer</code> : must be <code>123</code> in case that Strong Customer Authentication method for OTP challenge is dummy.<br />For instance: SANDBOX_TAN_OTP_INSTRUCTION_TRANSPORT=dummy<br />Possible values are dummy,email and sms<br />In kafka mode, the answer can be got by phone message or other SCA methods.</p><p>Note that each Transaction Request Type can have its own OTP_INSTRUCTION_TRANSPORT method.<br />OTP_INSTRUCTION_TRANSPORT methods are set in Props. See sample.props.template for instructions.</p><p>Single or Multiple authorisations</p><p>OBP allows single or multi party authorisations.</p><p>Single party authorisation:</p><p>In the case that only one person needs to authorise i.e. answer a security challenge we have the following change of state of a <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED</p><p>Multiparty authorisation:</p><p>In the case that multiple parties (n persons) need to authorise a transaction request i.e. answer security challenges, we have the followings state flow for a <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in the case of a correct answer but the user is different than expected the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If Product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In the case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute, the default number of security challenges created is one.</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not transaction_request_type:
            raise ValueError(
                f"Expected a non-empty value for `transaction_request_type` but received {transaction_request_type!r}"
            )
        if not transaction_request_id:
            raise ValueError(
                f"Expected a non-empty value for `transaction_request_id` but received {transaction_request_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/obp/v5.1.0/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/{transaction_request_type}/transaction-requests/{transaction_request_id}/challenge",
            body=maybe_transform(body, transaction_request_challenge_params.TransactionRequestChallengeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncTransactionRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionRequestsResourceWithRawResponse:
        return AsyncTransactionRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionRequestsResourceWithStreamingResponse:
        return AsyncTransactionRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        view_id: str,
        *,
        bank_id: str,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        <p>Special instructions for SIMPLE:</p><p>You can transfer money to the Bank Account Number or IBAN directly.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href="https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate">https://apiexplorer-ii-sandbox.openbankproject.com//more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href="https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href="https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests">here</a></p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/obp/v5.1.0/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/SIMPLE/transaction-requests",
            body=await async_maybe_transform(body, transaction_request_create_params.TransactionRequestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def challenge(
        self,
        transaction_request_id: str,
        *,
        bank_id: str,
        account_id: str,
        view_id: str,
        transaction_request_type: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        <p>In Sandbox mode, any string that can be converted to a positive integer will be accepted as an answer.</p><p>This endpoint totally depends on createTransactionRequest, it need get the following data from createTransactionRequest response body.</p><p>1)<code>TRANSACTION_REQUEST_TYPE</code> : is the same as createTransactionRequest request URL .</p><p>2)<code>TRANSACTION_REQUEST_ID</code> : is the <code>id</code> field in createTransactionRequest response body.</p><p>3) <code>id</code> :  is <code>challenge.id</code> field in createTransactionRequest response body.</p><p>4) <code>answer</code> : must be <code>123</code> in case that Strong Customer Authentication method for OTP challenge is dummy.<br />For instance: SANDBOX_TAN_OTP_INSTRUCTION_TRANSPORT=dummy<br />Possible values are dummy,email and sms<br />In kafka mode, the answer can be got by phone message or other SCA methods.</p><p>Note that each Transaction Request Type can have its own OTP_INSTRUCTION_TRANSPORT method.<br />OTP_INSTRUCTION_TRANSPORT methods are set in Props. See sample.props.template for instructions.</p><p>Single or Multiple authorisations</p><p>OBP allows single or multi party authorisations.</p><p>Single party authorisation:</p><p>In the case that only one person needs to authorise i.e. answer a security challenge we have the following change of state of a <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED</p><p>Multiparty authorisation:</p><p>In the case that multiple parties (n persons) need to authorise a transaction request i.e. answer security challenges, we have the followings state flow for a <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in the case of a correct answer but the user is different than expected the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If Product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In the case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute, the default number of security challenges created is one.</p><p>Authentication is Mandatory</p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bank_id:
            raise ValueError(f"Expected a non-empty value for `bank_id` but received {bank_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not transaction_request_type:
            raise ValueError(
                f"Expected a non-empty value for `transaction_request_type` but received {transaction_request_type!r}"
            )
        if not transaction_request_id:
            raise ValueError(
                f"Expected a non-empty value for `transaction_request_id` but received {transaction_request_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/obp/v5.1.0/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/{transaction_request_type}/transaction-requests/{transaction_request_id}/challenge",
            body=await async_maybe_transform(
                body, transaction_request_challenge_params.TransactionRequestChallengeParams
            ),
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
        self.challenge = to_custom_raw_response_wrapper(
            transaction_requests.challenge,
            BinaryAPIResponse,
        )


class AsyncTransactionRequestsResourceWithRawResponse:
    def __init__(self, transaction_requests: AsyncTransactionRequestsResource) -> None:
        self._transaction_requests = transaction_requests

        self.create = async_to_custom_raw_response_wrapper(
            transaction_requests.create,
            AsyncBinaryAPIResponse,
        )
        self.challenge = async_to_custom_raw_response_wrapper(
            transaction_requests.challenge,
            AsyncBinaryAPIResponse,
        )


class TransactionRequestsResourceWithStreamingResponse:
    def __init__(self, transaction_requests: TransactionRequestsResource) -> None:
        self._transaction_requests = transaction_requests

        self.create = to_custom_streamed_response_wrapper(
            transaction_requests.create,
            StreamedBinaryAPIResponse,
        )
        self.challenge = to_custom_streamed_response_wrapper(
            transaction_requests.challenge,
            StreamedBinaryAPIResponse,
        )


class AsyncTransactionRequestsResourceWithStreamingResponse:
    def __init__(self, transaction_requests: AsyncTransactionRequestsResource) -> None:
        self._transaction_requests = transaction_requests

        self.create = async_to_custom_streamed_response_wrapper(
            transaction_requests.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.challenge = async_to_custom_streamed_response_wrapper(
            transaction_requests.challenge,
            AsyncStreamedBinaryAPIResponse,
        )
