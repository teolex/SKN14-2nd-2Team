import streamlit as st
from utils.data_preprocessing import preprocess_data

st.set_page_config(page_title="About This Project", layout="wide")
st.title("About This Project")

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
