# 실행 결과 요약 (results.md)

실행 일자: 2026-06-11 / 환경: macOS, Python 3.9.6

## 1. pycodestyle 실행 결과 (경고 0건)

```
$ pycodestyle budget_tracker/ tests/ setup.py
$ echo $?
0
```

(출력 없음 = PEP 8 경고 0건)

## 2. pytest 실행 결과 (19개 전체 통과)

```
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/jesshan0214/Downloads/test/budget-tracker
collected 19 items

tests/test_core.py .......                                               [ 36%]
tests/test_ledger.py ......                                              [ 68%]
tests/test_utils.py ......                                               [100%]

============================== 19 passed in 0.01s ==============================
```

## 3. 새 가상환경에서 pip install . 결과 (성공)

```
$ python3 -m venv /tmp/bt_final_venv
$ /tmp/bt_final_venv/bin/pip install .
$ /tmp/bt_final_venv/bin/pip show budget_tracker
Name: budget-tracker
Version: 1.0.0
Summary: 일별 수입/지출을 기록하고 카테고리별 통계와 월간 리포트를 만드는 가계부 패키지
Author: Kim Hangyul
```

설치 후 README의 빠른 시작 코드를 그대로 실행한 출력:

```
248500
{'식비': 50000, '교통': 1500}
[2026-06] 수입 300,000원 | 지출 51,500원 | 잔액 248,500원
```

## 4. doctest 실행 결과 (40개 전체 통과)

```
budget_tracker.utils -> TestResults(failed=0, attempted=3)
budget_tracker.core -> TestResults(failed=0, attempted=4)
budget_tracker.transactions -> TestResults(failed=0, attempted=8)
budget_tracker.ledger -> TestResults(failed=0, attempted=25)
TOTAL FAILED: 0
```
