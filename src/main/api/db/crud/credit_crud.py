from sqlalchemy.orm import Session
from src.main.api.db.models.credit_table import Credit


class CreditCrud:
    @staticmethod
    def get_credit_by_id(db: Session, credit_id: int) -> Credit:
        return db.query(Credit).filter_by(id=credit_id).first()
    
    @staticmethod
    def get_credit_by_account_id(db: Session, account_id: int) -> Credit:
        return db.query(Credit).filter_by(account_id=account_id).first()

    @staticmethod
    def create_credit(
        db: Session, account_id: int, amount: float, term_months: int
    ) -> Credit:
        credit = Credit(
            account_id=account_id,
            amount=amount,
            term_months=term_months,
        )
        db.add(credit)
        db.commit()
        db.refresh(credit)
        return credit
