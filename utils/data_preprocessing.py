import os
import pandas as pd

# 경로 상수 정의
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(ROOT_DIR, "data", "Churn_Modelling.csv")


def preprocess_data() -> pd.DataFrame:
    """전체 전처리 파이프라인 실행 및 결과 CSV 저장"""
    df = pd.read_csv(RAW_DATA_PATH)
    return df
