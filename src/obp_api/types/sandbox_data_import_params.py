# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SandboxDataImportParams",
    "Account",
    "AccountBalance",
    "Atm",
    "AtmAddress",
    "AtmLocation",
    "AtmMeta",
    "AtmMetaLicense",
    "Bank",
    "Branch",
    "BranchAddress",
    "BranchLocation",
    "BranchMeta",
    "BranchMetaLicense",
    "BranchDriveUp",
    "BranchLobby",
    "CRMEvent",
    "CRMEventCustomer",
    "Product",
    "ProductMeta",
    "ProductMetaLicense",
    "Transaction",
    "TransactionDetails",
    "TransactionThisAccount",
    "TransactionCounterparty",
    "User",
]


class SandboxDataImportParams(TypedDict, total=False):
    accounts: Required[Iterable[Account]]

    atms: Required[Iterable[Atm]]

    banks: Required[Iterable[Bank]]

    branches: Required[Iterable[Branch]]

    crm_events: Required[Iterable[CRMEvent]]

    products: Required[Iterable[Product]]

    transactions: Required[Iterable[Transaction]]

    users: Required[Iterable[User]]


class AccountBalance(TypedDict, total=False):
    amount: Required[str]

    currency: Required[str]


class Account(TypedDict, total=False):
    id: Required[str]

    balance: Required[AccountBalance]

    bank: Required[str]

    generate_accountants_view: Required[bool]

    generate_auditors_view: Required[bool]

    generate_public_view: Required[bool]

    iban: Required[Annotated[str, PropertyInfo(alias="IBAN")]]

    label: Required[str]

    number: Required[str]

    owners: Required[List[str]]

    type: Required[str]


class AtmAddress(TypedDict, total=False):
    city: Required[str]

    country_code: Required[str]

    county: Required[str]

    line_1: Required[str]

    line_2: Required[str]

    line_3: Required[str]

    post_code: Required[str]

    state: Required[str]


class AtmLocation(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]


class AtmMetaLicense(TypedDict, total=False):
    id: Required[str]

    name: Required[str]


class AtmMeta(TypedDict, total=False):
    license: Required[AtmMetaLicense]


class Atm(TypedDict, total=False):
    id: Required[str]

    address: Required[AtmAddress]

    bank_id: Required[str]

    location: Required[AtmLocation]

    meta: Required[AtmMeta]

    name: Required[str]


class Bank(TypedDict, total=False):
    id: Required[str]

    full_name: Required[str]

    logo: Required[str]

    short_name: Required[str]

    website: Required[str]


class BranchAddress(TypedDict, total=False):
    city: Required[str]

    country_code: Required[str]

    county: Required[str]

    line_1: Required[str]

    line_2: Required[str]

    line_3: Required[str]

    post_code: Required[str]

    state: Required[str]


class BranchLocation(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]


class BranchMetaLicense(TypedDict, total=False):
    id: Required[str]

    name: Required[str]


class BranchMeta(TypedDict, total=False):
    license: Required[BranchMetaLicense]


class BranchDriveUp(TypedDict, total=False):
    hours: Required[str]


class BranchLobby(TypedDict, total=False):
    hours: Required[str]


class Branch(TypedDict, total=False):
    id: Required[str]

    address: Required[BranchAddress]

    bank_id: Required[str]

    location: Required[BranchLocation]

    meta: Required[BranchMeta]

    name: Required[str]

    drive_up: Annotated[BranchDriveUp, PropertyInfo(alias="driveUp")]

    lobby: BranchLobby


class CRMEventCustomer(TypedDict, total=False):
    name: Required[str]

    number: Required[str]


class CRMEvent(TypedDict, total=False):
    id: Required[str]

    actual_date: Required[str]

    bank_id: Required[str]

    category: Required[str]

    channel: Required[str]

    customer: Required[CRMEventCustomer]

    detail: Required[str]


class ProductMetaLicense(TypedDict, total=False):
    id: Required[str]

    name: Required[str]


class ProductMeta(TypedDict, total=False):
    license: Required[ProductMetaLicense]


class Product(TypedDict, total=False):
    bank_id: Required[str]

    category: Required[str]

    code: Required[str]

    family: Required[str]

    meta: Required[ProductMeta]

    more_info_url: Required[str]

    name: Required[str]

    super_family: Required[str]


class TransactionDetails(TypedDict, total=False):
    completed: Required[str]

    description: Required[str]

    new_balance: Required[str]

    posted: Required[str]

    type: Required[str]

    value: Required[str]


class TransactionThisAccount(TypedDict, total=False):
    id: Required[str]

    bank: Required[str]


class TransactionCounterparty(TypedDict, total=False):
    account_number: str

    name: str


class Transaction(TypedDict, total=False):
    id: Required[str]

    details: Required[TransactionDetails]

    this_account: Required[TransactionThisAccount]

    counterparty: TransactionCounterparty


class User(TypedDict, total=False):
    email: Required[str]

    password: Required[str]

    user_name: Required[str]
