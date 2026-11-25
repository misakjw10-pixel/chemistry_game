
import streamlit as st
import random

# ----------------------------------
# 1. 기본 화면 설정
# ----------------------------------

st.set_page_config(
    page_title="분자식 만들기 게임",
    page_icon="🧪",
    layout="wide"
)

st.markdown("""
<style>
div[data-testid="stButton"] button {
    min-width: 38px;
    height: 42px;
    padding: 0px 2px;
    font-size: 13px;
    font-weight: bold;
    white-space: nowrap;
}

div[data-testid="stHorizontalBlock"] {
    gap: 4px;
}

.formula {
    font-size: 30px;
    font-weight: bold;
}

.formula sub {
    font-size: 17px;
    vertical-align: sub;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------
# 2. 화학 물질 목록
# ----------------------------------

chemicals = [
    ["물", {"H": 2, "O": 1}],
    ["이산화 탄소", {"C": 1, "O": 2}],
    ["암모니아", {"N": 1, "H": 3}],
    ["메테인", {"C": 1, "H": 4}],
    ["염화 나트륨", {"Na": 1, "Cl": 1}],
    ["황산", {"H": 2, "S": 1, "O": 4}],
    ["포도당", {"C": 6, "H": 12, "O": 6}]
]


# ----------------------------------
# 3. 주기율표 118개 원소
# (원소 기호, 행, 열)
# ----------------------------------

elements = [
    ("H",0,0), ("He",0,17),

    ("Li",1,0), ("Be",1,1),
    ("B",1,12), ("C",1,13), ("N",1,14),
    ("O",1,15), ("F",1,16), ("Ne",1,17),

    ("Na",2,0), ("Mg",2,1),
    ("Al",2,12), ("Si",2,13), ("P",2,14),
    ("S",2,15), ("Cl",2,16), ("Ar",2,17),

    ("K",3,0), ("Ca",3,1), ("Sc",3,2),
    ("Ti",3,3), ("V",3,4), ("Cr",3,5),
    ("Mn",3,6), ("Fe",3,7), ("Co",3,8),
    ("Ni",3,9), ("Cu",3,10), ("Zn",3,11),
    ("Ga",3,12), ("Ge",3,13), ("As",3,14),
    ("Se",3,15), ("Br",3,16), ("Kr",3,17),

    ("Rb",4,0), ("Sr",4,1), ("Y",4,2),
    ("Zr",4,3), ("Nb",4,4), ("Mo",4,5),
    ("Tc",4,6), ("Ru",4,7), ("Rh",4,8),
    ("Pd",4,9), ("Ag",4,10), ("Cd",4,11),
    ("In",4,12), ("Sn",4,13), ("Sb",4,14),
    ("Te",4,15), ("I",4,16), ("Xe",4,17),

    ("Cs",5,0), ("Ba",5,1), ("La",5,2),
    ("Hf",5,3), ("Ta",5,4), ("W",5,5),
    ("Re",5,6), ("Os",5,7), ("Ir",5,8),
    ("Pt",5,9), ("Au",5,10), ("Hg",5,11),
    ("Tl",5,12), ("Pb",5,13), ("Bi",5,14),
    ("Po",5,15), ("At",5,16), ("Rn",5,17),

    ("Fr",6,0), ("Ra",6,1), ("Ac",6,2),
    ("Rf",6,3), ("Db",6,4), ("Sg",6,5),
    ("Bh",6,6), ("Hs",6,7), ("Mt",6,8),
    ("Ds",6,9), ("Rg",6,10), ("Cn",6,11),
    ("Nh",6,12), ("Fl",6,13), ("Mc",6,14),
    ("Lv",6,15), ("Ts",6,16), ("Og",6,17),

    ("Ce",7,3), ("Pr",7,4), ("Nd",7,5),
    ("Pm",7,6), ("Sm",7,7), ("Eu",7,8),
    ("Gd",7,9), ("Tb",7,10), ("Dy",7,11),
    ("Ho",7,12), ("Er",7,13), ("Tm",7,14),
    ("Yb",7,15), ("Lu",7,16),

    ("Th",8,3), ("Pa",8,4), ("U",8,5),
    ("Np",8,6), ("Pu",8,7), ("Am",8,8),
    ("Cm",8,9), ("Bk",8,10), ("Cf",8,11),
    ("Es",8,12), ("Fm",8,13), ("Md",8,14),
    ("No",8,15), ("Lr",8,16)
]


# ----------------------------------
# 4. 게임 초기 상태 설정
# ----------------------------------

if "stage" not in st.session_state:
    st.session_state.stage = 1
    st.session_state.user_formula = {}
    st.session_state.chemical = random.choice(chemicals)
    st.session_state.status = "playing"


# ----------------------------------
# 5. 분자식 출력 함수
# ----------------------------------

def print_formula(formula):

    result = ""

    for element, count in formula.items():

        result += element

        if count > 1:
            result += "<sub>" + str(count) + "</sub>"

    return result


# ----------------------------------
# 6. 원소 버튼 클릭 함수
# ----------------------------------

def add_element(element):

    if element in st.session_state.user_formula:

        st.session_state.user_formula[element] += 1

    else:

        st.session_state.user_formula[element] = 1


# ----------------------------------
# 7. 정답 확인 함수
# ----------------------------------

def check_right():

    answer = st.session_state.user_formula
    correct_answer = st.session_state.chemical[1]

    if answer == correct_answer:

        st.session_state.status = "correct"

    else:

        st.session_state.status = "wrong"


# ----------------------------------
# 8. 새로운 문제 출제 함수
# ----------------------------------

def new_question():

    st.session_state.user_formula = {}
    st.session_state.chemical = random.choice(chemicals)
    st.session_state.status = "playing"


# ----------------------------------
# 9. 처음 단계로 돌아가기 함수
# ----------------------------------

def restart_game():

    st.session_state.stage = 1

    new_question()


# ----------------------------------
# 10. 다음 단계로 이동하는 함수
# ----------------------------------

def next_stage():

    if st.session_state.stage == 5:

        st.session_state.status = "finished"

    else:

        st.session_state.stage += 1

        new_question()


# ----------------------------------
# 11. 화면 제목
# ----------------------------------

st.title("🧪 분자식 만들기 게임")

st.subheader(
    str(st.session_state.stage) + "단계 / 5단계"
)

st.progress(st.session_state.stage / 5)


# ----------------------------------
# 12. 화학 물질 출력
# ----------------------------------

st.header(
    "화학 물질: " + st.session_state.chemical[0]
)

st.divider()


# ----------------------------------
# 13. 사용자가 만든 분자식 출력
# ----------------------------------

formula = print_formula(st.session_state.user_formula)

st.markdown(
    '<div class="formula">현재 분자식: '
    + formula +
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ----------------------------------
# 14. 주기율표 출력
# ----------------------------------

st.subheader("주기율표")

for row in range(9):

    cols = st.columns(18)

    for element, r, c in elements:

        if r == row:

            with cols[c]:

                if st.button(
                    element,
                    key="element_" + element,
                    disabled=(st.session_state.status != "playing"),
                    use_container_width=True
                ):

                    add_element(element)

                    st.rerun()


# ----------------------------------
# 15. 입력 완료 버튼
# ----------------------------------

st.divider()

if st.session_state.status == "playing":

    if st.button("입력 완료", use_container_width=True):

        check_right()

        st.rerun()


# ----------------------------------
# 16. 정답 / 오답 / 최종 결과
# ----------------------------------

elif st.session_state.status == "correct":

    st.success("정답입니다!")

    if st.button("다음 단계", use_container_width=True):

        next_stage()

        st.rerun()


elif st.session_state.status == "wrong":

    st.error("오답입니다...")

    if st.button("처음 단계로 돌아가기", use_container_width=True):

        restart_game()

        st.rerun()


elif st.session_state.status == "finished":

    st.balloons()

    st.success("🎉 축하합니다!!")

    if st.button("처음으로 돌아가기", use_container_width=True):

        restart_game()

        st.rerun()
