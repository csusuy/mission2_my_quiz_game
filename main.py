from quiz_game import QuizGame


def main():
    game = QuizGame()

    try:
        game.run()

    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램이 종료 요청을 받았습니다.")
        game.save_data()
        print("안전하게 종료합니다.")


if __name__ == "__main__":
    main()