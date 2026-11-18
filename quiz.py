class Quiz:
    # 퀴즈를 만들 때 필요한 정보를 저장합니다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 퀴즈 문제와 선택지를 화면에 출력합니다.
    def display(self):
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    # 사용자가 입력한 답이 정답인지 확인합니다.
    def is_correct(self, user_answer):
        return user_answer == self.answer