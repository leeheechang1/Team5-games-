# core/card.py
import random

class Card:
    """낱장 카드를 정의하는 클래스"""
    def __init__(self, suit, rank):
        self.suit = suit  # 모양 (♠, ◆, ♥, ♣)
        self.rank = rank  # 숫자/문자 (A, 2~10, J, Q, K)

    def __str__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    """52장의 카드 덱을 관리하는 클래스"""
    def __init__(self):
        self.suits = ['♠', '◆', '♥', '♣']
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        self.reset()

    def reset(self):
        """새로운 52장 카드를 채우고 섞음"""
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def draw(self):
        """덱에서 카드 한 장을 뽑아서 반환"""
        if len(self.cards) == 0:
            print("덱에 카드가 떨어져서 새로운 덱을 섞습니다.")
            self.reset()
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)