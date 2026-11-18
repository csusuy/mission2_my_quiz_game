from quiz import Quiz


class QuizGame:
    def __init__(self):
        # 퀴즈 목록을 저장합니다.
        self.quizzes = []

        # 최고 점수를 저장합니다.
        self.best_score = 0

    # 게임 메뉴를 화면에 출력합니다.
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