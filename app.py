# app.py
import streamlit as st
from utils.data_preprocessing import preprocess_data

# ---------------------- 페이지 설정 ----------------------
st.set_page_config(page_title="이탈률 예측 대시보드", layout="wide")

# ---------------------- 메인 ----------------------
st.sidebar.markdown("### 신용카드 고객 이탈률 예측 대시보드")

st.markdown(
    """
    <h2>대시보드 홈</h2>
    <hr style='margin-top:0'>
""",
    unsafe_allow_html=True,
)

with st.expander("프로젝트 소개", expanded=True):
    st.markdown(
        """
    - **목표**: 은행 고객 신용카드 계좌해지 가능성 예측
    - **활용 분야**: 고객 유지 전략, 맞춤형 금용상품 제공 전략 수립
    - **데이터 출처**: Kaggle - [Credit Card Customer Churn Prediction](https://www.kaggle.com/datasets/rjmanoj/credit-card-customer-churn-prediction)
    """
    )

with st.expander("데이터 소개", expanded=True):
    st.dataframe(preprocess_data(), use_container_width=True)

with st.expander("예측 모델 개요 (사용한 알고리즘, 주요 변수 등)", expanded=True):
    st.markdown(
        """
    - 사용 알고리즘: XGBoost, Random Forest, Logistic Regression
    - 주요 변수: 나이, 성별, 계좌잔고 등
    - 평가 지표: Accuracy, ROC-AUC, F1-score 등
    """
    )
