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
    # 천 단위 구분 기호(,) 포맷 지정자 사용 (Python 공식 문서 참고)
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
    # '-' 기준으로 잘랐을 때 연/월/일 세 부분이 나와야 한다
    parts = text.split("-")
    if len(parts) != DATE_PART_COUNT:
        return False
    # 각 부분의 자릿수 검사 (연 4자리, 월/일 2자리)
    year, month, day = parts
    if len(year) != YEAR_LENGTH or len(month) != MONTH_LENGTH:
        return False
    if len(day) != DAY_LENGTH:
        return False
    # 세 부분 모두 숫자로만 이루어져야 한다
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    # 월은 1~12, 일은 1~31 범위 안이어야 한다
    if not MIN_MONTH <= int(month) <= MAX_MONTH:
        return False
    if not MIN_DAY <= int(day) <= MAX_DAY:
        return False
    return True
