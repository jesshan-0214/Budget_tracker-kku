"""Ledger 클래스 테스트."""

from budget_tracker import Expense, Income, Ledger


def make_sample_ledger():
    """테스트용 거래 4건이 담긴 Ledger를 만든다.

    :return: 수입 1건과 지출 3건이 등록된 Ledger
    """
    ledger = Ledger()
    ledger.add(Income("2026-06-01", 300000, "용돈", "부모님"))
    ledger.add(Expense("2026-06-02", 50000, "장보기", "식비"))
    ledger.add(Expense("2026-06-03", 1500, "버스", "교통"))
    ledger.add(Expense("2026-07-01", 12000, "영화", "여가"))
    return ledger


def test_ledger_balance():
    ledger = make_sample_ledger()
    assert ledger.balance() == 300000 - 50000 - 1500 - 12000


def test_total_income_and_expense():
    ledger = make_sample_ledger()
    assert ledger.total_income() == 300000
    assert ledger.total_expense() == 63500


def test_totals_by_category():
    ledger = make_sample_ledger()
    totals = ledger.totals_by_category()
    assert totals["식비"] == 50000
    assert totals["교통"] == 1500
    assert totals["여가"] == 12000


def test_monthly_report_contains_totals():
    ledger = make_sample_ledger()
    report = ledger.monthly_report("2026-06")
    assert "300,000" in report
    assert "51,500" in report
    assert "248,500" in report


def test_empty_ledger_balance_zero():
    ledger = Ledger()
    assert ledger.balance() == 0


def test_ledger_add_wrong_type_raises():
    # 거래 객체가 아닌 문자열을 넣으면 TypeError가 나야 한다
    ledger = Ledger()
    try:
        ledger.add("점심 9000원")
        raised = False
    except TypeError:
        raised = True
    assert raised
