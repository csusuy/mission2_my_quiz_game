from quiz import Quiz


class QuizGame:
    def __init__(self):
        # 기본 퀴즈 5개
        self.quizzes = [
            Quiz(
                "사람의 심장은 일반적으로 몇 개의 방으로 이루어져 있을까요?",
                ["2개", "3개", "4개", "5개"],
                3
            ),
            Quiz(
                "문어의 심장은 모두 몇 개일까요?",
                ["1개", "2개", "3개", "4개"],
                3
            ),
            Quiz(
                "태양계에서 가장 큰 행성은 무엇일까요?",
                ["지구", "목성", "화성", "금성"],
                2
            ),
            Quiz(
                "물은 일반적인 대기압에서 몇 도에 얼까요?",
                ["0도", "10도", "50도", "100도"],
                1
            ),
            Quiz(
                "번개가 친 뒤 천둥소리가 들리는 이유는 무엇일까요?",
                [
                    "구름이 서로 부딪혀서",
                    "빛이 소리보다 느려서",
                    "빛이 소리보다 빨라서",
                    "바람이 소리를 만들어서"
                ],
                3
            )
        ]

        # 최고 점수
        self.best_score = 0

    def show_menu(self):
        print("\n========================================")
        print("          🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

     # 숫자를 안전하게 입력받는 기능
    def get_valid_number(self, prompt, min_value, max_value):
        while True:
            user_input = input(prompt).strip()

            if user_input == "":
                print("⚠️ 빈 입력입니다. 다시 입력해 주세요.")
                continue

            try:
                number = int(user_input)

                if min_value <= number <= max_value:
                    return number

                print(
                    f"⚠️ {min_value}~{max_value} 사이의 숫자를 입력하세요."
                )

            except ValueError:
                print("⚠️ 숫자만 입력해 주세요.")

    # 퀴즈를 진행하는 기능
    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for index, quiz in enumerate(self.quizzes, start=1):
            print("\n----------------------------------------")
            print(f"[문제 {index}]")

            quiz.display()

            answer = self.get_valid_number(
                "정답 입력 (1~4): ", 1, 4
            )

            if quiz.is_correct(answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        percentage = round(score / total * 100)

        print("\n========================================")
        print(f"🏆 결과: {total}문제 중 {score}문제 정답!")
        print(f"점수: {percentage}점")

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")

        print("========================================")
    
    # 게임 전체 실행 기능
    def run(self):
        while True:
            self.show_menu()

            choice = self.get_valid_number(
                "선택: ", 1, 5
            )

            if choice == 1:
                self.play_quiz()

            elif choice == 2:
                self.add_quiz()

            elif choice == 3:
                self.show_quizzes()

            elif choice == 4:
                self.show_best_score()

            elif choice == 5:
                print("게임을 종료합니다. 감사합니다!")
                break    

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = input("문제를 입력하세요: ").strip()

        while not question:
            print("⚠️ 문제를 비워둘 수 없습니다.")
            question = input("문제를 입력하세요: ").strip()

        choices = []

        for number in range(1, 5):
            choice = input(
                f"선택지 {number}: "
            ).strip()

            while not choice:
                print("⚠️ 선택지를 비워둘 수 없습니다.")
                choice = input(
                    f"선택지 {number}: "
                ).strip()

            choices.append(choice)

        answer = self.get_valid_number(
            "정답 번호 (1~4): ", 1, 4
        )

        new_quiz = Quiz(question, choices, answer)

        self.quizzes.append(new_quiz)

        print("\n✅ 새로운 퀴즈가 추가되었습니다!")
    
    # 등록된 퀴즈 목록을 보여주는 기능
    def show_quizzes(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print(
            f"\n📋 등록된 퀴즈 목록 "
            f"(총 {len(self.quizzes)}개)"
        )

        print("----------------------------------------")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

        print("----------------------------------------")
    
     # 최고 점수를 확인하는 기능
    def show_best_score(self):
        print("\n========================================")

        if self.best_score == 0:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"🏆 최고 점수: {self.best_score}점")

        print("========================================")