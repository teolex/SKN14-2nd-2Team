import streamlit as st
import time
import numpy as np

# Disable Streamlit's default re-rendering behavior
st.set_page_config(page_title="고객 정보를 입력해주세요", layout="centered")

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

h2 {
    animation: fadeIn 1.5s ease-in;
    margin-bottom: 2rem;
}

/* Style the button container */
.button-container {
    margin-top: 2rem;
    padding: 1rem;
    text-align: center;
}

/* Make the button more prominent */
button[kind="primary"] {
    font-size: 1.2rem;
    padding: 0.5rem 2rem;
    margin-top: 1rem;
}

/* Add some space between sections */
.input-section {
    margin-bottom: 2rem;
}

/* Override Streamlit's default styles */
.stSelectbox {
    opacity: 1 !important;
}

.stSelectbox > div {
    opacity: 1 !important;
}

.stSelectbox > div > div {
    opacity: 1 !important;
}

.stNumberInput {
    opacity: 1 !important;
}

.stNumberInput > div {
    opacity: 1 !important;
}

.stNumberInput > div > div {
    opacity: 1 !important;
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
st.markdown("## 고객 정보를 입력해주세요")
st.markdown("</div>", unsafe_allow_html=True)

# Initialize session state for form data if not exists
if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'age': 38,
        'is_active': 'O',
        'geography': 'France',
        'num_products': 4,
        'gender': 'Male',
        'balance': 100000
    }

# Input fields section
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("나이", min_value=18, max_value=92, value=st.session_state.form_data['age'], key="age")
    is_active = st.selectbox("활성 고객 여부", ["O", "X"], index=0 if st.session_state.form_data['is_active'] == 'O' else 1, key="is_active")
    geography = st.selectbox("국가", ["France", "Germany", "Spain"], index=["France", "Germany", "Spain"].index(st.session_state.form_data['geography']), key="geography")
with col2:
    num_products = st.number_input(
        "금융 상품 수", min_value=0, value=st.session_state.form_data['num_products'], key="num_products"
    )
    gender = st.selectbox("성별", ["Male", "Female"], index=0 if st.session_state.form_data['gender'] == 'Male' else 1, key="gender")
    balance = st.number_input(
        "계좌 잔액", min_value=0, value=st.session_state.form_data['balance'], step=1000, key="balance"
    )

# Update session state with current values
st.session_state.form_data.update({
    'age': age,
    'is_active': is_active,
    'geography': geography,
    'num_products': num_products,
    'gender': gender,
    'balance': balance
})

# Separate button section
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("다음 단계로", type="primary", use_container_width=True):
    # Store the form data in session state
    st.session_state.customer_info = {
        "LogAge": np.log(age),  # Transform age to log scale
        "NumOfProducts": num_products,
        "IsActiveMember": 1 if is_active == "O" else 0,
        "Geography": geography,
        "Gender": gender,
        "Balance": np.log(balance +1) # added 1 to the balance before taking the log to avoid issues with a balance of zero.
    }
    # Navigate to the model selection page
    st.switch_page("pages/2_모델_선택.py")
st.markdown("</div>", unsafe_allow_html=True)
