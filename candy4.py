import streamlit as st

def calculate_geometric_term(first_term, common_ratio, n_th_term):
    """
    등비수열의 n번째 항을 계산하는 함수.
    공식: a * r^(n-1)
    """
    if n_th_term <= 0:
        return "오류: 항의 번호는 1 이상의 정수여야 합니다."
    
    term_value = first_term * (common_ratio ** (n_th_term - 1))
    return term_value

def calculate_geometric_sum(first_term, common_ratio, n_th_sum):
    """
    등비수열의 첫째항부터 n번째 항까지의 합을 계산하는 함수.
    공식: Sn = a * (1 - r^n) / (1 - r) (r != 1)
    공식: Sn = n * a (r == 1)
    """
    if n_th_sum <= 0:
        return "오류: 합을 구할 항의 개수는 1 이상의 정수여야 합니다."

    if common_ratio == 1:
        # 공비가 1인 경우: a + a + ... + a (n번) = n * a
        total_sum = n_th_sum * first_term
    else:
        # 공비가 1이 아닌 경우
        total_sum = first_term * (1 - (common_ratio ** n_th_sum)) / (1 - common_ratio)
    
    return total_sum

# --- Streamlit 앱 인터페이스 설정 ---
st.set_page_config(
    page_title="등비수열 계산기",
    page_icon="✨",
    layout="centered" # 페이지 레이아웃을 중앙으로 설정
)

st.title("🌟 등비수열의 n번째 항 및 합 계산기")
st.write("첫째항과 공비를 입력하고, 알고 싶은 항의 번호 또는 합을 구할 항의 개수를 입력하세요.")

# --- 사용자 입력 위젯 ---
st.header("입력 값")

# 첫째항 입력
first_term = st.number_input(
    "**첫째항 (a)을 입력하세요:**",
    value=1.0,
    step=0.1,
    format="%.2f",
    help="등비수열의 첫 번째 항의 값입니다."
)

# 공비 입력
common_ratio = st.number_input(
    "**공비 (r)를 입력하세요:**",
    value=1.0,
    step=0.1,
    format="%.2f",
    help="각 항에 곱해지는 일정한 비율입니다."
)

# 몇 번째 항인지 입력 (항의 값 계산용)
n_th_term_input = st.number_input(
    "**알고 싶은 항의 번호 (n)를 입력하세요:**",
    min_value=1,
    value=1,
    step=1,
    help="값을 알고 싶은 항의 순서 (예: 1, 2, 3...)"
)

# 몇 번째 항까지의 합인지 입력 (합 계산용)
n_th_sum_input = st.number_input(
    "**합을 구할 마지막 항의 번호 (N)를 입력하세요:**",
    min_value=1,
    value=1,
    step=1,
    help="첫째항부터 합을 구할 마지막 항의 순서"
)

# --- 계산 및 결과 출력 ---
st.header("계산 결과")

# '계산하기' 버튼이 클릭될 때만 결과 표시
if st.button("🚀 계산하기"):
    # n번째 항의 값 계산
    term_result = calculate_geometric_term(first_term, common_ratio, n_th_term_input)
    
    # 항의 합 계산
    sum_result = calculate_geometric_sum(first_term, common_ratio, n_th_sum_input)
    
    # n번째 항의 값 출력
    if isinstance(term_result, str) and "오류" in term_result:
        st.error(f"**n번째 항 계산 오류:** {term_result}")
    else:
        st.success(f"입력하신 등비수열의 **{int(n_th_term_input)}번째 항**의 값은: **{term_result:.4f}** 입니다.")
        st.info(f"💡 등비수열의 n번째 항 공식: $a \\cdot r^{{n-1}}$")

    st.markdown("---") # 구분선 추가

    # 항의 합 출력
    if isinstance(sum_result, str) and "오류" in sum_result:
        st.error(f"**합 계산 오류:** {sum_result}")
    else:
        st.success(f"입력하신 등비수열의 **첫째항부터 {int(n_th_sum_input)}번째 항까지의 합**은: **{sum_result:.4f}** 입니다.")
        st.info(f"💡 등비수열의 합 공식: $S_n = a \\frac{{1-r^n}}{{1-r}}$ (단, $r \\ne 1$), $S_n = na$ (단, $r = 1$)")

    st.balloons() # 계산 성공 시 풍선 애니메이션

st.markdown("---")
st.caption("© 2025 등비수열 계산기 by Gemini")
