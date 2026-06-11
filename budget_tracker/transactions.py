"""Transaction을 상속하는 Income, Expense 클래스를 정의하는 모듈."""

from .core import Transaction


class Income(Transaction):
    """수입 거래를 표현하는 클래스.

    :ivar source: 수입 출처 (예: 월급, 용돈)

    >>> allowance = Income("2026-06-01", 300000, "6월 용돈", "부모님")
    >>> allowance.source
    '부모님'
    """

    def __init__(self, date, amount, description, source="기타"):
        """Income 인스턴스를 만든다.

        :param date: 'YYYY-MM-DD' 형식의 거래 날짜
        :param amount: 0보다 큰 수입 금액
        :param description: 거래 내용 설명
        :param source: 수입 출처 (기본값 '기타')
        """
        # 날짜·금액 검증은 부모 Transaction의 __init__이 담당한다
        super().__init__(date, amount, description)
        self.source = source

    def signed_amount(self):
        """잔액 계산에 쓰이는 부호 있는 금액을 반환한다.

        수입은 잔액을 늘리므로 양수를 반환한다.

        :return: 양수 금액

        >>> Income("2026-06-01", 300000, "용돈").signed_amount()
        300000
        """
        return self.amount

    def summary(self):
        """출처를 포함한 한 줄 요약을 반환한다.

        :return: '날짜 | 금액원 | 설명 [출처: ...]' 문자열

        >>> Income("2026-06-01", 300000, "용돈", "부모님").summary()
        '2026-06-01 | 300,000원 | 용돈 [출처: 부모님]'
        """
        return f"{super().summary()} [출처: {self.source}]"


class Expense(Transaction):
    """지출 거래를 표현하는 클래스.

    :ivar category: 지출 카테고리 (예: 식비, 교통)

    >>> lunch = Expense("2026-06-11", 9000, "점심", "식비")
    >>> lunch.category
    '식비'
    """

    def __init__(self, date, amount, description, category="기타"):
        """Expense 인스턴스를 만든다.

        :param date: 'YYYY-MM-DD' 형식의 거래 날짜
        :param amount: 0보다 큰 지출 금액
        :param description: 거래 내용 설명
        :param category: 지출 카테고리 (기본값 '기타')
        """
        # 날짜·금액 검증은 부모 Transaction의 __init__이 담당한다
        super().__init__(date, amount, description)
        self.category = category

    def signed_amount(self):
        """잔액 계산에 쓰이는 부호 있는 금액을 반환한다.

        지출은 잔액을 줄이므로 음수를 반환한다.

        :return: 음수 금액

        >>> Expense("2026-06-11", 9000, "점심").signed_amount()
        -9000
        """
        return -self.amount

    def summary(self):
        """카테고리를 포함한 한 줄 요약을 반환한다.

        :return: '날짜 | 금액원 | 설명 [카테고리: ...]' 문자열

        >>> Expense("2026-06-11", 9000, "점심", "식비").summary()
        '2026-06-11 | 9,000원 | 점심 [카테고리: 식비]'
        """
        return f"{super().summary()} [카테고리: {self.category}]"
