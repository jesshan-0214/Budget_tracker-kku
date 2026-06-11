"""금액과 날짜를 다루는 도우미 함수 모듈."""

DATE_PART_COUNT = 3
YEAR_LENGTH = 4
MONTH_LENGTH = 2
DAY_LENGTH = 2
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31


def format_amount(amount):
    """금액을 천 단위 콤마가 있는 문자열로 바꾼다.

    :param amount: 변환할 금액(숫자)
    :return: 콤마가 포함된 금액 문자열

    >>> format_amount(1234567)
    '1,234,567'
    """
    return f"{amount:,}"


def is_valid_date(text):
    """문자열이 'YYYY-MM-DD' 형식의 날짜인지 검사한다.

    :param text: 검사할 값
    :return: 형식이 올바르면 True, 아니면 False

    >>> is_valid_date("2026-06-11")
    True
    >>> is_valid_date("2026/06/11")
    False
    """
    if not isinstance(text, str):
        return False
    parts = text.split("-")
    if len(parts) != DATE_PART_COUNT:
        return False
    year, month, day = parts
    if len(year) != YEAR_LENGTH or len(month) != MONTH_LENGTH:
        return False
    if len(day) != DAY_LENGTH:
        return False
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    if not MIN_MONTH <= int(month) <= MAX_MONTH:
        return False
    if not MIN_DAY <= int(day) <= MAX_DAY:
        return False
    return True
