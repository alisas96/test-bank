from enum import Enum


class TransactionType(str, Enum):
    CREDIT_REPAYMENT = "credit_repayment"
    CREDIT_ISSUANCE = "credit_issuance"
    DEPOSIT = "deposit"
    TRANSFER = "transfer"
