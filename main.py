from games.thief_card.play import start_game


def main():
    user_name = input("플레이어 이름을 입력하세요: ").strip()
    if not user_name:
        user_name = "Player 1"

    player_info = {"name": user_name, "chips": 100}
    player_info = start_game(player_info)

    print(f"\n게임 종료! 최종 보유 칩: {player_info['chips']}개")


if __name__ == "__main__":
    main()
