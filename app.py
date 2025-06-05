# app.py
import streamlit as st
import time

# ---------------------- 페이지 설정 ----------------------
st.set_page_config(page_title="이탈률 예측 대시보드", layout="wide")

# ---------------------- 메인 ---------------------- SK Networks Family 14th Team 2 

# Fade-in animation and centering for content using HTML/CSS
st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fade-in {
    animation: fadeIn 1.5s ease-in;
}

.centered-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
    text-align: center;
}

h1 {
    margin-bottom: 1rem;
    margin-top: 0.5rem;
}

.team-name {
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 0.2rem;
}

.project-title {
    font-size: 1.4rem;
    color: #0066cc;
    font-weight: 500;
    margin-bottom: 1.5rem;
}

.button-container {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}
</style>
<div class="centered-container">
    <div class="fade-in">
        <div class="team-name">SK Networks Family 14th Team 2</div>
        <div class="project-title">Project: 은행 고객 특성에 따른 이탈률 예측</div>
        <h1>고객 이탈을 예측해드립니다</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# Wait for animation (simulate delay)
time.sleep(1.2)

# Center the buttons using columns
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("예측 시작하기", type="primary", use_container_width=True):
        st.switch_page("pages/1_고객_정보_입력.py")
    if st.button("About This Project", use_container_width=True):
        st.switch_page("pages/0_About_This_Project.py")
    st.markdown('</div>', unsafe_allow_html=True)
