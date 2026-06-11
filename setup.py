"""budget_tracker 패키지 설치 스크립트."""

from setuptools import setup

setup(
    name="budget_tracker",
    version="1.0.0",
    description="일별 수입/지출을 기록하고 카테고리별 통계와 "
                "월간 리포트를 만드는 가계부 패키지",
    author="Kim Hangyul",
    author_email="jesshan0214@naver.com",
    packages=["budget_tracker"],
    install_requires=[],
)
