"""거래 목록을 관리하고 통계를 내는 Ledger 클래스를 정의하는 모듈."""

from collections import defaultdict

from .core import Transaction
from .transactions import Expense, Income
from .utils import format_amount


class Ledger:
    """거래를 모아 관리하는 가계부 장부 클래스.

    :ivar transactions: 등록된 거래(Transaction) 목록

    >>> ledger = Ledger()
    >>> ledger.add(Income("2026-06-01", 300000, "용돈"))
    >>> ledger.add(Expense("2026-06-02", 50000, "장보기", "식비"))
    >>> ledger.balance()
    250000
    """

    def __init__(self):
        """빈 거래 목록으로 Ledger 인스턴스를 만든다."""
        self.transactions = []

    def add(self, transaction):
        """거래 한 건을 장부에 추가한다.

        :param transaction: Income 또는 Expense 인스턴스
        :return: None

        >>> ledger = Ledger()
        >>> ledger.add(Income("2026-06-01", 1000, "이자"))
        >>> len(ledger.transactions)
        1
        """
        # 문자열·숫자 등 거래가 아닌 값이 장부에 섞이는 것을 막는다
        if not isinstance(transaction, Transaction):
            raise TypeError("Transaction 인스턴스만 추가할 수 있습니다.")
        self.transactions.append(transaction)

    def total_income(self):
        """전체 수입 합계를 반환한다.

        :return: 수입 합계 (0 이상의 숫자)

        >>> ledger = Ledger()
        >>> ledger.add(Income("2026-06-01", 300000, "용돈"))
        >>> ledger.total_income()
        300000
        """
        income, expense = self._signed_totals(self.transactions)
        return income

    def total_expense(self):
        """전체 지출 합계를 양수로 반환한다.

        :return: 지출 합계 (0 이상의 숫자)

        >>> ledger = Ledger()
        >>> ledger.add(Expense("2026-06-02", 50000, "장보기", "식비"))
        >>> ledger.total_expense()
        50000
        """
        income, expense = self._signed_totals(self.transactions)
        return expense

    def balance(self):
        """전체 잔액(수입 - 지출)을 반환한다.

        :return: 잔액 (음수일 수도 있음)

        >>> ledger = Ledger()
        >>> ledger.add(Income("2026-06-01", 300000, "용돈"))
        >>> ledger.add(Expense("2026-06-02", 50000, "장보기", "식비"))
        >>> ledger.balance()
        250000
        """
        income, expense = self._signed_totals(self.transactions)
        return income - expense

    def totals_by_category(self):
        """지출을 카테고리별로 합산한 딕셔너리를 반환한다.

        :return: {카테고리: 지출 합계} 형태의 딕셔너리

        >>> ledger = Ledger()
        >>> ledger.add(Expense("2026-06-02", 9000, "점심", "식비"))
        >>> ledger.add(Expense("2026-06-03", 1500, "버스", "교통"))
        >>> ledger.totals_by_category()
        {'식비': 9000, '교통': 1500}
        """
        # defaultdict(int): 처음 보는 카테고리는 자동으로 0부터 시작
        totals = defaultdict(int)
        for transaction in self.transactions:
            if isinstance(transaction, Expense):
                totals[transaction.category] += transaction.amount
        return dict(totals)

    def monthly_report(self, month):
        """특정 달의 수입/지출/잔액 요약 문자열을 반환한다.

        :param month: 'YYYY-MM' 형식의 달
        :return: 해당 달의 요약 문자열

        >>> ledger = Ledger()
        >>> ledger.add(Income("2026-06-01", 300000, "용돈"))
        >>> ledger.add(Expense("2026-06-02", 50000, "장보기", "식비"))
        >>> ledger.monthly_report("2026-06")
        '[2026-06] 수입 300,000원 | 지출 50,000원 | 잔액 250,000원'
        """
        monthly = self._filter_by_month(month)
        income, expense = self._signed_totals(monthly)
        balance = income - expense
        return (f"[{month}] 수입 {format_amount(income)}원 | "
                f"지출 {format_amount(expense)}원 | "
                f"잔액 {format_amount(balance)}원")

    def _filter_by_month(self, month):
        """특정 달에 속한 거래만 골라 리스트로 반환한다.

        :param month: 'YYYY-MM' 형식의 달
        :return: 해당 달의 거래 리스트
        """
        return [transaction for transaction in self.transactions
                if transaction.month() == month]

    def _signed_totals(self, transactions):
        """거래 목록의 수입 합계와 지출 합계를 함께 계산한다.

        :param transactions: 합산할 거래 리스트
        :return: (수입 합계, 지출 합계) 튜플
        """
        income = 0
        expense = 0
        for transaction in transactions:
            # signed_amount(): 수입은 양수, 지출은 음수를 반환 (다형성)
            signed = transaction.signed_amount()
            if signed > 0:
                income += signed
            else:
                expense -= signed  # 음수를 빼서 지출 합계를 양수로 만든다
        return income, expense
