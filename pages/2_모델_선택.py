import streamlit as st
import time

st.set_page_config(page_title="예측에 사용할 모델을 선택하세요", layout="centered")

# Add custom CSS for fade-in animation and centering
st.markdown(
    """
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.animate-fade-in {
    animation: fadeIn 1.5s ease-in;
}

div[data-testid="stMarkdownContainer"] {
    text-align: center;
}

h1 {
    animation: fadeIn 1.5s ease-in;
    margin-bottom: 1rem;
    text-align: center;
}

/* Style the model selection container */
.model-container {
    display: flex;
    flex-direction: row;
    gap: 3rem; /* Increased gap between columns */
    justify-content: center;
    align-items: center;
    margin: 1rem 0;
}

/* Style the model buttons */
button[kind="primary"] {
    /* Removed fixed width */
    font-size: 1rem !important;
    padding: 0.3rem 1rem !important;
    margin-top: 0.5rem !important; /* Add space between image and button */
    /* Removed manual margin-left */
    margin-left: 0 !important;
    margin-right: 0 !important;
    display: block !important; /* Ensure it takes full width of container */
}

/* Remove direct column content centering CSS */
/* div[data-testid="stVerticalBlock"] { */
/*     display: flex; */
/*     flex-direction: column; */
/*     align-items: center; */
/* } */

/* Style the navigation buttons container */
.nav-buttons {
    margin-top: 1rem;
    display: flex;
    justify-content: space-between;
    gap: 1rem;
}

/* Disable all transitions */
* {
    transition: none !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# Center the title with fade-in
st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
st.markdown("# 예측에 사용할 모델을 선택하세요")
st.markdown("</div>", unsafe_allow_html=True)

# Wait for animation (simulate delay)
time.sleep(1.5)

# Check if customer info exists in session state
if "customer_info" not in st.session_state:
    st.warning("고객 정보를 먼저 입력해주세요.")
    st.switch_page("pages/1_고객_정보_입력.py")

# Model selection
st.markdown('<div class="model-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.image("pages/catboost_logo.png", use_container_width=True)
    # Removed nested columns
    if st.button("CatBoost", type="primary", key="catboost", use_container_width=True):
        st.session_state.selected_model = "CatBoost"
        st.switch_page("pages/3_예측_결과.py")
with col2:
    st.image("pages/Scikit_learn.png", use_container_width=True)
    # Removed nested columns
    if st.button("HistGBM", type="primary", key="histgbm", use_container_width=True):
        st.session_state.selected_model = "HistGBM"
        st.switch_page("pages/3_예측_결과.py")
with col3:
    st.image("pages/LightGBM.png", use_container_width=True)
    # Removed nested columns
    if st.button("LightGBM", type="primary", key="lightgbm", use_container_width=True):
        st.session_state.selected_model = "LightGBM"
        st.switch_page("pages/3_예측_결과.py")
st.markdown("</div>", unsafe_allow_html=True)

# Navigation buttons
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    if st.button("이전 단계"):
        st.switch_page("pages/1_고객_정보_입력.py")
st.markdown("</div>", unsafe_allow_html=True)
