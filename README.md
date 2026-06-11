# budget_tracker — 가계부·예산 추적기

Python 프로그래밍 기말 프로젝트 (주제 D)

GitHub 저장소: <https://github.com/jesshan-0214/budget-tracker>

## 1. 프로젝트 개요

`budget_tracker`는 일별 수입과 지출을 기록하고 통계를 내는 Python 패키지입니다.
공통 부모 클래스 `Transaction`을 상속한 `Income`(수입)과 `Expense`(지출)
클래스로 거래 한 건을 표현하고, `Ledger` 클래스로 잔액 계산, 카테고리별
지출 통계, 월간 리포트 기능을 제공할 예정입니다.

## 2. 설치 방법

```bash
git clone https://github.com/jesshan-0214/budget-tracker.git
cd budget-tracker
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

## 3. 빠른 시작 (Quick Start)

(클래스 구현 후 추가 예정)

## 4. 주요 기능 (계획)

1. 거래 기록 — `Income`/`Expense` 인스턴스를 `Ledger.add()`로 등록
2. 잔액·합계 계산
3. 카테고리별 지출 통계
4. 월간 리포트
5. 입력 검증 (잘못된 금액·날짜 거부)

## 5. 테스트 실행 방법

```bash
pip install -r requirements.txt
pytest
```

## 6. 작성자 정보

- 이름: (이름을 입력하세요)
- 학번: (학번을 입력하세요)
- 이메일: jesshan0214@gmail.com
