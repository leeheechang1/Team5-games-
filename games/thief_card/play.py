import random

from core.card import Deck


class ThiefCard:
    rank = "THIEF"

    def __str__(self):
        return "도둑"


def make_old_maid_deck():
    deck = Deck()
    cards = [deck.draw() for _ in range(len(deck))]
    cards.append(ThiefCard())
    random.shuffle(cards)
    return cards


def card_rank(card):
    return card.rank


def remove_pairs(hand):
    rank_groups = {}
    remaining_hand = []
    removed_count = 0

    for card in hand:
        rank_groups.setdefault(card_rank(card), []).append(card)

    for rank, cards in rank_groups.items():
        if rank == "THIEF":
            remaining_hand.extend(cards)
            continue

        pair_count = len(cards) // 2
        removed_count += pair_count * 2
        remaining_hand.extend(cards[pair_count * 2 :])

    random.shuffle(remaining_hand)
    return remaining_hand, removed_count


def deal_cards(cards):
    player_hand = []
    computer_hand = []

    for index, card in enumerate(cards):
        if index % 2 == 0:
            player_hand.append(card)
        else:
            computer_hand.append(card)

    return player_hand, computer_hand


def display_player_hand(hand):
    print("\n--- 나의 카드 ---")
    for index, card in enumerate(hand, start=1):
        print(f"{index}. {card}")
    print("----------------")


def draw_from_computer(player_hand, computer_hand):
    print(f"\n컴퓨터 카드 수: {len(computer_hand)}장")

    while True:
        try:
            choice = int(input(f"뽑을 카드 번호를 선택하세요 (1~{len(computer_hand)}): "))
            if 1 <= choice <= len(computer_hand):
                break
            print("범위 안의 숫자를 입력해 주세요.")
        except ValueError:
            print("숫자로 입력해 주세요.")

    picked_card = computer_hand.pop(choice - 1)
    player_hand.append(picked_card)
    print(f"뽑은 카드: {picked_card}")


def draw_from_player(computer_hand, player_hand):
    picked_index = random.randrange(len(player_hand))
    picked_card = player_hand.pop(picked_index)
    computer_hand.append(picked_card)
    print("\n컴퓨터가 내 카드 중 한 장을 뽑았습니다.")


def check_winner(player_hand, computer_hand):
    if len(player_hand) == 0:
        return "player"
    if len(computer_hand) == 0:
        return "computer"
    return None


def play_round():
    cards = make_old_maid_deck()
    player_hand, computer_hand = deal_cards(cards)

    player_hand, player_removed = remove_pairs(player_hand)
    computer_hand, computer_removed = remove_pairs(computer_hand)

    print("\n♣ 도둑잡기 게임을 시작합니다! ♣")
    print("공용 카드 덱(core.card.Deck)을 사용해서 카드를 나눴습니다.")
    print(f"처음에 버린 짝 카드: 나 {player_removed}장, 컴퓨터 {computer_removed}장")

    turn = "player"

    while True:
        winner = check_winner(player_hand, computer_hand)
        if winner:
            return winner

        if turn == "player":
            display_player_hand(player_hand)
            draw_from_computer(player_hand, computer_hand)
            player_hand, removed_count = remove_pairs(player_hand)
            if removed_count:
                print(f"같은 숫자 카드 {removed_count}장을 버렸습니다.")
            turn = "computer"
        else:
            draw_from_player(computer_hand, player_hand)
            computer_hand, removed_count = remove_pairs(computer_hand)
            if removed_count:
                print(f"컴퓨터가 같은 숫자 카드 {removed_count}장을 버렸습니다.")
            turn = "player"


def start_game(player_info):
    print(f"\n{player_info['name']}님, 도둑잡기 게임을 시작합니다.")

    winner = play_round()

    if winner == "player":
        print("\n승리! 내 카드가 먼저 없어졌습니다.")
        player_info["chips"] += 20
        print("보상으로 칩 20개를 얻었습니다.")
    else:
        print("\n패배! 컴퓨터 카드가 먼저 없어졌습니다.")
        player_info["chips"] = max(0, player_info["chips"] - 10)
        print("칩 10개를 잃었습니다.")

    print(f"현재 보유 칩: {player_info['chips']}개")
    input("\n[Enter]를 누르면 메인 로비로 돌아갑니다...")
    return player_info


if __name__ == "__main__":
    test_player = {"name": "Player 1", "chips": 100}
    start_game(test_player)
