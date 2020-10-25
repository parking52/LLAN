from deck import Deck
from player import Player


def resolve_action(action, active_player, passive_player):
    if action:
        if not passive_player.protected:

            if action == 'reveal':
                active_player.knowledge_opponent = passive_player.card1
            if action == 'compare':

                active_player.knowledge_opponent = passive_player.card1
                passive_player.knowledge_opponent = active_player.card1
            if action == 'exchange':
                active_player.card1, passive_player.card1 = passive_player.card1, active_player.card1
                active_player.knowledge_opponent = passive_player.card1
                passive_player.knowledge_opponent = active_player.card1


def play_game():
    deck = Deck()
    deck.shuffle()
    print(deck.deck)

    player1 = Player(1)
    player2 = Player(-1)
    players = {1: player1,
               -1: player2}

    player1.draw(deck.deck.pop())
    player2.draw(deck.deck.pop())

    player_turn = 1
    player_lost = 0

    played_card = []

    while len(deck.deck) > 1:
        player, passive_player = players[player_turn], players[player_turn*-1]
        player.draw(deck.deck.pop())
        card, player_lost, action = player.play()
        resolve_action(action, player, passive_player)
        played_card.append(card)
        player_turn *= -1

        if player_lost != 0:
            print(f'player_lost: {player_lost}')
            return -1*player_lost

    if player_lost == 0:
        if player1.card1 > player2.card1:
            print('player 1 won')
            return 1

        if player1.card1 < player2.card1:
            print('player 2 won')
            return -1

        if player1.card1 == player2.card1:
            print('Draw!')
            return 0

    print(deck.deck)


if __name__ == "__main__":

    n = 1
    results = []
    for i in range(n):
        results.append(play_game())
    print(sum(results))


