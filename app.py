
import tkinter as tk
import random

# 화학 물질 목록
chemicals = [
    ["물", {"H": 2, "O": 1}],
    ["이산화 탄소", {"C": 1, "O": 2}],
    ["암모니아", {"N": 1, "H": 3}],
    ["메테인", {"C": 1, "H": 4}],
    ["염화 나트륨", {"Na": 1, "Cl": 1}],
    ["황산", {"H": 2, "S": 1, "O": 4}],
    ["포도당", {"C": 6, "H": 12, "O": 6}]
]

# 주기율표 원소 목록 (기호, 행, 열)
elements = [
    ("H", 0, 0), ("He", 0, 17),
    ("Li", 1, 0), ("Be", 1, 1),
    ("B", 1, 12), ("C", 1, 13), ("N", 1, 14),
    ("O", 1, 15), ("F", 1, 16), ("Ne", 1, 17),
    ("Na", 2, 0), ("Mg", 2, 1),
    ("Al", 2, 12), ("Si", 2, 13), ("P", 2, 14),
    ("S", 2, 15), ("Cl", 2, 16), ("Ar", 2, 17),
    ("K", 3, 0), ("Ca", 3, 1), ("Sc", 3, 2),
    ("Ti", 3, 3), ("V", 3, 4), ("Cr", 3, 5),
    ("Mn", 3, 6), ("Fe", 3, 7), ("Co", 3, 8),
    ("Ni", 3, 9), ("Cu", 3, 10), ("Zn", 3, 11),
    ("Ga", 3, 12), ("Ge", 3, 13), ("As", 3, 14),
    ("Se", 3, 15), ("Br", 3, 16), ("Kr", 3, 17),
    ("Rb", 4, 0), ("Sr", 4, 1), ("Y", 4, 2),
    ("Zr", 4, 3), ("Nb", 4, 4), ("Mo", 4, 5),
    ("Tc", 4, 6), ("Ru", 4, 7), ("Rh", 4, 8),
    ("Pd", 4, 9), ("Ag", 4, 10), ("Cd", 4, 11),
    ("In", 4, 12), ("Sn", 4, 13), ("Sb", 4, 14),
    ("Te", 4, 15), ("I", 4, 16), ("Xe", 4, 17),
    ("Cs", 5, 0), ("Ba", 5, 1), ("La", 5, 2),
    ("Hf", 5, 3), ("Ta", 5, 4), ("W", 5, 5),
    ("Re", 5, 6), ("Os", 5, 7), ("Ir", 5, 8),
    ("Pt", 5, 9), ("Au", 5, 10), ("Hg", 5, 11),
    ("Tl", 5, 12), ("Pb", 5, 13), ("Bi", 5, 14),
    ("Po", 5, 15), ("At", 5, 16), ("Rn", 5, 17),
    ("Fr", 6, 0), ("Ra", 6, 1), ("Ac", 6, 2),
    ("Rf", 6, 3), ("Db", 6, 4), ("Sg", 6, 5),
    ("Bh", 6, 6), ("Hs", 6, 7), ("Mt", 6, 8),
    ("Ds", 6, 9), ("Rg", 6, 10), ("Cn", 6, 11),
    ("Nh", 6, 12), ("Fl", 6, 13), ("Mc", 6, 14),
    ("Lv", 6, 15), ("Ts", 6, 16), ("Og", 6, 17),
    ("Ce", 7, 3), ("Pr", 7, 4), ("Nd", 7, 5),
    ("Pm", 7, 6), ("Sm", 7, 7), ("Eu", 7, 8),
    ("Gd", 7, 9), ("Tb", 7, 10), ("Dy", 7, 11),
    ("Ho", 7, 12), ("Er", 7, 13), ("Tm", 7, 14),
    ("Yb", 7, 15), ("Lu", 7, 16),
    ("Th", 8, 3), ("Pa", 8, 4), ("U", 8, 5),
    ("Np", 8, 6), ("Pu", 8, 7), ("Am", 8, 8),
    ("Cm", 8, 9), ("Bk", 8, 10), ("Cf", 8, 11),
    ("Es", 8, 12), ("Fm", 8, 13), ("Md", 8, 14),
    ("No", 8, 15), ("Lr", 8, 16)
]

# 게임 변수
stage = 1
user_formula = {}
current_chemical = None
answer = {}
correct_answer = {}


# 화면 만들기
root = tk.Tk()
root.title("분자식 만들기 게임")
root.geometry("1200x800")

# 제목
title_label = tk.Label(
    root,
    text="분자식 만들기 게임",
    font=("Arial", 25, "bold")
)
title_label.pack(pady=10)

# 단계 표시
stage_label = tk.Label(root, font=("Arial", 16))
stage_label.pack()

# 화학 물질 표시
chemical_label = tk.Label(
    root,
    font=("Arial", 22, "bold"),
    fg="blue"
)
chemical_label.pack(pady=10)

# 분자식 표시
formula_label = tk.Label(
    root,
    text="현재 분자식: ",
    font=("Arial", 22)
)
formula_label.pack(pady=10)

# 결과 표시
result_label = tk.Label(
    root,
    font=("Arial", 20, "bold")
)
result_label.pack(pady=5)

# 원소 버튼 저장
element_buttons = {}


# 분자식 표시 함수
def update_formula():

    result = ""

    for element, count in user_formula.items():

        result += element

        if count > 1:
            result += str(count)

    formula_label.config(text="현재 분자식: " + result)


# 원소 버튼 클릭 함수
def add_element(element):

    if element in user_formula:
        user_formula[element] += 1

    else:
        user_formula[element] = 1

    update_formula()


# 정답 확인 함수
def check_right():

    global answer, correct_answer

    answer = user_formula.copy()
    correct_answer = current_chemical[1]

    if answer == correct_answer:

        result_label.config(
            text="정답입니다!",
            fg="green"
        )

        # 다음 단계 버튼 표시
        next_button.config(
            text="다음 단계",
            command=next_stage
        )

    else:

        result_label.config(
            text="오답입니다...",
            fg="red"
        )

        # 처음 단계로 돌아가기 버튼 표시
        next_button.config(
            text="처음 단계로 돌아가기",
            command=restart_game
        )

    # 결과에 맞는 버튼 표시
    next_button.pack(pady=10)

    # 원소 버튼 비활성화
    for button in element_buttons.values():
        button.config(state="disabled")

    complete_button.config(state="disabled")


# 새로운 문제 출제 함수
def new_question():

    global user_formula, current_chemical

    user_formula = {}

    current_chemical = random.choice(chemicals)

    stage_label.config(
        text=str(stage) + "단계 / 5단계"
    )

    chemical_label.config(
        text="화학 물질: " + current_chemical[0]
    )

    formula_label.config(text="현재 분자식: ")

    result_label.config(text="")

    next_button.pack_forget()

    complete_button.config(state="normal")

    for button in element_buttons.values():
        button.config(state="normal")


# 다음 단계 함수
def next_stage():

    global stage

    if stage == 5:

        result_label.config(
            text="축하합니다!!",
            fg="green"
        )

        next_button.config(
            text="처음으로 돌아가기",
            command=restart_game
        )

        return

    stage += 1

    new_question()


# 처음으로 돌아가기 함수
def restart_game():

    global stage

    stage = 1

    new_question()


# 주기율표 만들기
periodic_frame = tk.Frame(root)
periodic_frame.pack(pady=15)

for element, row, col in elements:

    button = tk.Button(
        periodic_frame,
        text=element,
        width=4,
        height=2,
        font=("Arial", 10, "bold"),
        bg="lightblue",
        command=lambda e=element: add_element(e)
    )

    button.grid(
        row=row,
        column=col,
        padx=2,
        pady=2
    )

    element_buttons[element] = button


# 입력 완료 버튼
complete_button = tk.Button(
    root,
    text="입력 완료",
    font=("Arial", 15, "bold"),
    bg="lightgreen",
    command=check_right
)
complete_button.pack(pady=10)


# 다음 단계 버튼
next_button = tk.Button(
    root,
    font=("Arial", 15, "bold")
)


# 첫 문제 시작
new_question()

# 프로그램 실행
root.mainloop()
