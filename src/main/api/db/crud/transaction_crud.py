from sqlalchemy.orm import Session
from src.main.api.db.models.transaction_table import Transaction


class TransactionCrud:
    @staticmethod
    def get_transaction_by_credit_id(db: Session, credit_id: int) -> Transaction:
        return db.query(Transaction).filter_by(credit_id=credit_id).first()

    @staticmethod
    def get_transaction_by_to_account_id(
        db: Session, to_account_id: int
    ) -> Transaction:
        return db.query(Transaction).filter_by(to_account_id=to_account_id).first()
