"""가계부 거래의 부모 클래스인 Transaction을 정의하는 모듈."""

from .utils import format_amount, is_valid_date


class Transaction:
    """가계부에 기록되는 거래 한 건을 표현하는 부모 클래스.

    날짜와 금액 검증 로직을 이 클래스에 모아 두어,
    Income과 Expense 자식 클래스가 중복 없이 재사용한다.

    :ivar date: 거래 날짜 ('YYYY-MM-DD' 형식 문자열)
    :ivar amount: 거래 금액 (0보다 큰 숫자)
    :ivar description: 거래 내용 설명

    >>> meal = Transaction("2026-06-11", 9000, "점심")
    >>> meal.amount
    9000
    """

    def __init__(self, date, amount, description):
        """Transaction 인스턴스를 만든다.

        :param date: 'YYYY-MM-DD' 형식의 거래 날짜
        :param amount: 0보다 큰 거래 금액
        :param description: 거래 내용 설명
        """
        # 검증을 통과한 값만 속성에 저장된다 (잘못된 값은 여기서 차단)
        self.date = self._validate_date(date)
        self.amount = self._validate_amount(amount)
        self.description = description

    def _validate_amount(self, amount):
        """금액이 0보다 큰 숫자인지 검사한다.

        :param amount: 검사할 금액
        :return: 검증을 통과한 금액
        """
        # 타입이 잘못되면 TypeError, 값이 잘못되면 ValueError로 구분
        if not isinstance(amount, (int, float)):
            raise TypeError("금액은 숫자여야 합니다.")
        if amount <= 0:
            raise ValueError("금액은 0보다 커야 합니다.")
        return amount

    def _validate_date(self, date):
        """날짜가 'YYYY-MM-DD' 형식인지 검사한다.

        :param date: 검사할 날짜 문자열
        :return: 검증을 통과한 날짜 문자열
        """
        if not is_valid_date(date):
            raise ValueError("날짜는 'YYYY-MM-DD' 형식이어야 합니다.")
        return date

    def summary(self):
        """거래 내용을 한 줄 문자열로 요약한다.

        :return: '날짜 | 금액원 | 설명' 형태의 문자열

        >>> Transaction("2026-06-11", 9000, "점심").summary()
        '2026-06-11 | 9,000원 | 점심'
        """
        amount_text = format_amount(self.amount)
        return f"{self.date} | {amount_text}원 | {self.description}"

    def month(self):
        """거래가 속한 달을 'YYYY-MM' 문자열로 반환한다.

        :return: 'YYYY-MM' 형식 문자열

        >>> Transaction("2026-06-11", 9000, "점심").month()
        '2026-06'
        """
        # 'YYYY-MM-DD'에서 연·월 부분만 다시 이어 붙인다
        parts = self.date.split("-")
        return f"{parts[0]}-{parts[1]}"
