def main():
    import json
    import random

    from utils import Player, get_word, word_check, winner, record_in_json

    with open('words_for_game.json', encoding='utf-8') as f:
        words_for_game = json.load(f)

    with open('russian_nouns.txt', 'r', encoding='utf-8') as f:
        dictionary = [line.rstrip('\n') for line in f]

    print('Добро пожаловать в игру!')

    nam_player = {'1': 'первого', '2': 'второго', '3': 'третьего', '4': 'четвёртого', '5': 'пятого'}
    # Словарь с ключами возможного количества игроков, значениями для удобночитаемости при запросе ввода имён
    number_of_players = ''
    correct = False
    while not correct:
        # цикл работает пока не введут количество игроков в диапазоне 1-5
        number_of_players = input('Введите количество игроков цифрой, от одного до пяти\n')
        correct = number_of_players in nam_player.keys()

    players = []
    for i in range(int(number_of_players)):
        player = Player(input(f'Введите имя {nam_player[str(i + 1)]} игрока\n'), str(i + 1))
        players.append(player)

    opponents = [player.name for player in players]
    # Список для вывода имён всех игроков
    print(f'\n{" vs ".join(opponents).upper()}, игра начинается!')
    word_for_game = get_word(words_for_game, random)
    print(f'Ваше слово на эту игру: {word_for_game}\nЕсли захотите завершить игру, напишите stop или стоп')

    go_game = True
    while go_game:
        # цикл работает пока один из игроков не введёт стоп, раунд продолжается до последнего игрока
        print(f'======\nНачало раунда.\n{word_for_game}')
        for player in players:
            word_player = input(f'Ходит игрок {player.name.upper()}\n').strip().lower()
            if word_player not in ['stop', 'стоп']:
                text, check = word_check(word_player, word_for_game, dictionary, players)
                print(text)
                if check:
                    player.words.append(word_player)
            else:
                go_game = False

    print('Игра окончена\n======')
    for player in players:
        player.calculating_points_from_words()
        print(f"{player} - {player.points}")

    print(f'======\nПобедил игрок {", игрок ".join(winner(players))}')
    record_in_json(players, word_for_game)
    print('======\nДанные записаны в файл')


if __name__ == '__main__':
    main()

print("ok")