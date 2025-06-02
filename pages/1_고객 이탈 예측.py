import os
import pickle
import numpy as np
import streamlit as st
import plotly.graph_objects as go


# ------------------ 경로 설정 ------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVM_MODEL_PATH = os.path.join(ROOT_DIR, "models", "SVC.sav")
SVM_SCALER_PATH = os.path.join(ROOT_DIR, "models", "SVC.scaler")

st.set_page_config(page_title="고객 이탈 예측", layout="centered")
st.title("고객 이탈 예측 입력 폼")

st.markdown("아래 정보를 입력하면 고객 이탈 가능성을 예측할 수 있습니다.")


@st.cache_resource
def load_svc():
    with open(SVM_MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(SVM_SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
    return model, scaler


svc_model, svc_scaler = load_svc()

# ------------------ 입력 폼 ------------------
with st.form("dropout_form"):
    st.markdown("### 📋 고객 정보 입력")

    # 줄 1
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("성별 (Gender)", ["Male", "Female"])
    with col2:
        age = st.number_input("나이 (Age)", min_value=18, max_value=92, value=38)
    with col3:
        geography = st.selectbox("지역 (Geography)", ["France", "Spain", "Germany"])
    with col4:
        credit_score = st.number_input(
            "신용 점수 (CreditScore)", min_value=350, max_value=850, value=650
        )

    # 줄 2
    col6, col7, col8, col9 = st.columns(4)
    with col6:
        tenure = st.number_input("거래 기간", min_value=0, value=10)
    with col7:
        num_products = st.number_input("금융상품 수", min_value=0, value=4)
    with col8:
        has_cr_card = st.selectbox("신용카드 보유 여부", [1, 0])
    with col9:
        is_active = st.selectbox("활성 고객 여부", [1, 0])

    # 줄 3
    col5, col6 = st.columns(2)
    with col5:
        balance = st.number_input(
            "계좌 잔고", min_value=0.0, max_value=250000.00, value=75000.0, step=1000.0
        )
    with col6:
        estimated_salary = st.number_input(
            "연봉 (달러)",
            min_value=0.0,
            max_value=200000.00,
            value=100000.0,
            step=1000.0,
        )

    # Streamlit UI
    st.markdown("### 🔍 예측 모델 선택")

    submitted = st.form_submit_button("Submit")
    if submitted:
        # st.success("입력 정보가 제출되었습니다!")

        # ------------------ 전처리 ------------------
        gender_male = 1 if gender == "Male" else 0
        geography_germany = 1 if geography == "Germany" else 0
        geography_spain = 1 if geography == "Spain" else 0

        input_features = np.array(
            [
                [
                    credit_score,
                    age,
                    tenure,
                    balance,
                    num_products,
                    has_cr_card,
                    is_active,
                    estimated_salary,
                    geography_germany,
                    geography_spain,
                    gender_male,
                ]
            ]
        )

        input_features = svc_scaler.transform(input_features)

        # ------------------ 예측 ------------------
        prediction = svc_model.predict(input_features)[0]
        # print(prediction)
        prediction_proba = getattr(svc_model, "predict_proba", lambda x: None)(
            input_features
        )
        st.subheader("📈 예측 결과")
        st.success(f"✅ 예측 결과: **{'이탈' if prediction == 1 else '유지'}**")
        if prediction_proba is not None:
            st.markdown(f"**이탈 확률:** {prediction_proba[0][1]*100:.2f}%")

            # ✅ 이탈 확률 게이지 차트
            gauge_fig = go.Figure(
                go.Indicator(
                    mode="gauge+number+delta",
                    value=prediction_proba[0][1] * 100,
                    delta={"reference": 50},
                    title={"text": "이탈 확률 (%)"},
                    gauge={
                        "axis": {"range": [0, 100]},
                        "bar": {
                            "color": (
                                "crimson" if prediction_proba[0][1] > 0.5 else "green"
                            )
                        },
                        "steps": [
                            {"range": [0, 50], "color": "#9be7a6"},
                            {"range": [50, 75], "color": "#ffe066"},
                            {"range": [75, 100], "color": "#ff9999"},
                        ],
                    },
                )
            )

            st.plotly_chart(gauge_fig, use_container_width=True)
