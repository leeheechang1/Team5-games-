from games.thief_card.play import start_game as start_old_maid
from games.stock_fake_news.play import start_game as start_stock_fake_news


def main():
    user_name = input("플레이어 이름을 입력하세요: ").strip()
    if not user_name:
        user_name = "Player 1"

    player_info = {"name": user_name, "chips": 100}

    while True:
        print("\n1. 도둑잡기")
        print("2. 주식 가짜 뉴스 판별게임")
        print("0. 종료")

        choice = input("게임을 선택하세요: ").strip()

        if choice == "1":
            player_info = start_old_maid(player_info)
        elif choice == "2":
            player_info = start_stock_fake_news(player_info)
        elif choice == "0":
            break
        else:
            print("잘못된 선택입니다.")

    print(f"\n게임 종료! 최종 보유 칩: {player_info['chips']}개")


if __name__ == "__main__":
    main()
