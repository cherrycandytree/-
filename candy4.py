import streamlit as st

def calculate_geometric_term(first_term, common_ratio, n_th_term):
    """
    등비수열의 n번째 항을 계산하는 함수.
    공식: a * r^(n-1)
    """
    # 항의 번호는 1 이상이어야 함
    if n_th_term <= 0:
        return "오류: 항의 번호는 1 이상의 정수여야 합니다."
    
    # 등비수열의 n번째 항 계산
    term_value = first_term * (common_ratio ** (n_th_term - 1))
    return term_value

# --- Streamlit 앱 인터페이스 설정 ---
st.set_page_config(
    page_title="등비수열 계산기",
    page_icon="✨",
    layout="centered" # 페이지 레이아웃을 중앙으로 설정
)

st.title("🌟 등비수열의 n번째 항 계산기")
st.write("첫째항과 공비를 입력하고, 알고 싶은 항의 번호를 입력하면 해당 항의 값을 알려드립니다.")

# --- 사용자 입력 위젯 ---
st.header("입력 값")

# 첫째항 입력 (기본값 1.0, 소수점 두 자리까지 표시)
first_term = st.number_input(
    "**첫째항 (a)을 입력하세요:**",
    value=1.0,
    step=0.1,
    format="%.2f",
    help="등비수열의 첫 번째 항의 값입니다."
)

# 공비 입력 (기본값 1.0, 소수점 두 자리까지 표시)
common_ratio = st.number_input(
    "**공비 (r)를 입력하세요:**",
    value=1.0,
    step=0.1,
    format="%.2f",
    help="각 항에 곱해지는 일정한 비율입니다."
)

# 몇 번째 항인지 입력 (최소값 1, 정수 단위)
n_th_term = st.number_input(
    "**알고 싶은 항의 번호 (n)를 입력하세요:**",
    min_value=1,
    value=1,
    step=1,
    help="알고 싶은 항의 순서 (예: 1, 2, 3...)"
)

# --- 계산 및 결과 출력 ---
st.header("계산 결과")

# '계산하기' 버튼이 클릭될 때만 결과 표시
if st.button("🚀 계산하기"):
    result = calculate_geometric_term(first_term, common_ratio, n_th_term)
    
    # 결과가 오류 메시지인 경우
    if isinstance(result, str) and "오류" in result:
        st.error(result) # 빨간색 오류 메시지 출력
    else:
        # 정상적인 결과인 경우
        st.success(f"입력하신 등비수열의 **{int(n_th_term)}번째 항**의 값은: **{result:.4f}** 입니다.")
        st.balloons() # 계산 성공 시 풍선 애니메이션
        st.info("💡 공식을 잊으셨나요? 등비수열의 n번째 항은 $a \\cdot r^{n-1}$ 입니다.")

st.markdown("---")
st.caption("© 2025 등비수열 계산기 by Gemini")
