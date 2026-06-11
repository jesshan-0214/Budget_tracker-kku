"""utils 모듈의 도우미 함수 테스트."""

from budget_tracker.utils import format_amount, is_valid_date


def test_format_amount_comma():
    assert format_amount(1234567) == "1,234,567"


def test_format_amount_small_number():
    assert format_amount(900) == "900"


def test_is_valid_date_true():
    assert is_valid_date("2026-06-11") is True


def test_is_valid_date_wrong_separator():
    assert is_valid_date("2026/06/11") is False


def test_is_valid_date_out_of_range_month():
    assert is_valid_date("2026-13-01") is False


def test_is_valid_date_not_a_string():
    assert is_valid_date(20260611) is False
