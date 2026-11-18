from quiz import Quiz


class QuizGame:
    def __init__(self):
        # 기본 퀴즈 5개
        self.quizzes = [
            Quiz(
                "영화 '기생충'의 감독은 누구일까요?",
                ["박찬욱", "봉준호", "김기덕", "이창동"],
                2
            ),
            Quiz(
                "영화 '인터스텔라'의 감독은 누구일까요?",
                ["크리스토퍼 놀란", "스티븐 스필버그",
                 "제임스 카메론", "리들리 스콧"],
                1
            ),
            Quiz(
                "드라마 '오징어 게임'에서 성기훈 역을 맡은 배우는?",
                ["공유", "박해수", "이정재", "이병헌"],
                3
            ),
            Quiz(
                "애니메이션 '겨울왕국'에 등장하는 눈사람의 이름은?",
                ["크리스토프", "엘사", "안나", "올라프"],
                4
            ),
            Quiz(
                "마블 영화에서 타노스가 모은 인피니티 스톤은 몇 개일까요?",
                ["4개", "5개", "6개", "7개"],
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