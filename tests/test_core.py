"""Transaction, Income, Expense 클래스 테스트."""

from budget_tracker import Expense, Income, Transaction


def test_income_creation():
    income = Income("2026-06-01", 300000, "6월 용돈", "부모님")
    assert income.date == "2026-06-01"
    assert income.amount == 300000
    assert income.description == "6월 용돈"
    assert income.source == "부모님"


def test_expense_signed_amount_negative():
    expense = Expense("2026-06-11", 9000, "점심", "식비")
    assert expense.signed_amount() == -9000


def test_income_summary_contains_source():
    income = Income("2026-06-01", 300000, "용돈", "부모님")
    assert income.summary() == "2026-06-01 | 300,000원 | 용돈 [출처: 부모님]"


def test_transaction_month():
    transaction = Transaction("2026-06-11", 9000, "점심")
    assert transaction.month() == "2026-06"


def test_transaction_negative_amount_raises():
    # 예외가 나면 except로 빠져 raised가 True가 되는 패턴 (이하 동일)
    try:
        Expense("2026-06-11", -500, "점심", "식비")
        raised = False
    except ValueError:
        raised = True
    assert raised


def test_transaction_wrong_amount_type_raises():
    try:
        Income("2026-06-01", "삼만원", "용돈")
        raised = False
    except TypeError:
        raised = True
    assert raised


def test_transaction_invalid_date_raises():
    try:
        Expense("2026/06/11", 9000, "점심", "식비")
        raised = False
    except ValueError:
        raised = True
    assert raised
