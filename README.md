# budget_tracker — 가계부·예산 추적기

Python 프로그래밍 기말 프로젝트 (주제 D)

GitHub 저장소: <https://github.com/jesshan-0214/Budget_tracker-kku>

## 1. 프로젝트 개요

`budget_tracker`는 일별 수입과 지출을 기록하고 통계를 내는 Python 패키지입니다.
공통 부모 클래스 `Transaction`이 날짜·금액 검증을 담당하고, 이를 상속한
`Income`(수입)과 `Expense`(지출) 클래스가 거래 한 건을 표현합니다.
`Ledger` 클래스에 거래를 등록하면 잔액, 카테고리별 지출 통계,
월간 리포트를 얻을 수 있습니다.

## 2. 설치 방법

### macOS / Linux

```bash
git clone https://github.com/jesshan-0214/Budget_tracker-kku.git
cd Budget_tracker-kku
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

### Windows (PowerShell)

```powershell
git clone https://github.com/jesshan-0214/Budget_tracker-kku.git
cd Budget_tracker-kku
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install .
```

## 3. 빠른 시작 (Quick Start)

먼저 터미널에 `python`(Windows는 `python`, macOS/Linux는 `python3`)을
입력해 대화형 인터프리터를 실행하면 `>>>` 프롬프트가 나타납니다.
이 프롬프트에 아래 코드를 입력합니다. (끝낼 때는 `exit()` 입력)

```python
>>> from budget_tracker import Expense, Income, Ledger
>>> ledger = Ledger()
>>> ledger.add(Income("2026-06-01", 300000, "6월 용돈", "부모님"))
>>> ledger.add(Expense("2026-06-02", 50000, "장보기", "식비"))
>>> ledger.add(Expense("2026-06-03", 1500, "버스", "교통"))
>>> ledger.balance()
248500
>>> ledger.totals_by_category()
{'식비': 50000, '교통': 1500}
>>> print(ledger.monthly_report("2026-06"))
[2026-06] 수입 300,000원 | 지출 51,500원 | 잔액 248,500원
```

또는 위 코드를 `example.py` 같은 파일로 저장한 뒤
`python example.py`로 한 번에 실행할 수도 있습니다.

<details>
<summary>참고: 파일로 실행할 때의 전체 코드</summary>

```python
from budget_tracker import Expense, Income, Ledger

ledger = Ledger()
ledger.add(Income("2026-06-01", 300000, "6월 용돈", "부모님"))
ledger.add(Expense("2026-06-02", 50000, "장보기", "식비"))
ledger.add(Expense("2026-06-03", 1500, "버스", "교통"))

print(ledger.balance())                 # 248500
print(ledger.totals_by_category())      # {'식비': 50000, '교통': 1500}
print(ledger.monthly_report("2026-06"))
# [2026-06] 수입 300,000원 | 지출 51,500원 | 잔액 248,500원
```

</details>

## 4. 주요 기능

1. **거래 기록** — `Income`/`Expense` 인스턴스를 `Ledger.add()`로 등록
2. **잔액·합계 계산** — `balance()`, `total_income()`, `total_expense()`
3. **카테고리별 지출 통계** — `totals_by_category()`
4. **월간 리포트** — `monthly_report("YYYY-MM")` 한 줄 요약
5. **입력 검증** — 0 이하 금액(`ValueError`), 숫자가 아닌 금액(`TypeError`),
   잘못된 날짜 형식(`ValueError`)을 생성 시점에 거부

## 5. 테스트 실행 방법

```bash
pip install -r requirements.txt
pytest
```

실행 결과:

```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/jesshan0214/Downloads/test/budget-tracker
collected 19 items

tests/test_core.py .......                                               [ 36%]
tests/test_ledger.py ......                                              [ 68%]
tests/test_utils.py ......                                               [100%]

============================== 19 passed in 0.01s ==============================
```

## 6. 작성자 정보

- 이름: 김한결(KIM HANGYUL)
- 학번: 202620855
- 이메일: jesshan0214@naver.com
