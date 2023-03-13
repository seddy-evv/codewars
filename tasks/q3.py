"""
Write a method that takes a field for well-known board game "Battleship" as an
argument and returns true if it has
a valid disposition of ships, false otherwise. Argument is guaranteed to be
10*10 two-dimension array.
Elements in the array are numbers, 0 if the cell is free and 1 if occupied
by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing
several "ships" and objective is to destroy enemy's forces by targetting
individual cells on his field.
The ship occupies one or more cells in the grid. Size and number of ships
may differ from version to version.
In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships
accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3),
3 destroyers (size 2) and 4 submarines (size 1).
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just
single cell.

The ship cannot overlap or be in contact with any other ship, neither by
edge nor by corner.
"""


def validate_battlefield(field):
    i = 10
    j = 10
    n = 0
    value = True
    ships = []
    coord = {}
    while n < i:
        k = 0
        while k < j:
            if field[n][k]:
                if n - 1 >= 0 and k - 1 >= 0 and n + 1 < 10 and k + 1 < 10:
                    value = field[n-1][k-1] == 0 and field[n-1][k+1] == 0 and \
                            field[n+1][k-1] == 0 and field[n+1][k+1] == 0
                elif n - 1 >= 0 and n + 1 < 10 and k + 1 < 10:
                    value = field[n - 1][k + 1] == 0 and field[n + 1][k + 1] == 0
                elif k - 1 >= 0 and n + 1 < 10 and k + 1 < 10:
                    value = field[n + 1][k - 1] == 0 and field[n + 1][k + 1] == 0
                elif n + 1 < 10 and k + 1 < 10:
                    value = field[n + 1][k + 1] == 0
                if not value:
                    return value
                p = n + 1
                s = k + 1
                coord[(n, k)] = coord.get((n, k), 0) + 1
                if coord[(n, k)] == 1:
                    ship = [(n, k)]
                    while p < i and field[p][k]:
                        coord[(p, k)] = coord.get((p, k), 0) + 1
                        ship.append((p, k))
                        p = p + 1
                    while s < j and field[n][s]:
                        coord[(n, s)] = coord.get((n, s), 0) + 1
                        ship.append((n, s))
                        s = s + 1
                    ships.append(ship)
            k = k + 1
        n = n + 1
    if len(ships) != 10:
        return False
    ships_length = {}
    for ship in ships:
        ships_length[len(ship)] = ships_length.get(len(ship), 0) + 1
    for ship_length in ships_length:
        if ship_length == 4 and ships_length[ship_length] != 1:
            return False
        elif ship_length == 3 and ships_length[ship_length] != 2:
            return False
        elif ship_length == 2 and ships_length[ship_length] != 3:
            return False
        elif ship_length == 1 and ships_length[ship_length] != 4:
            return False
    return True


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


if __name__ == '__main__':
    print(validate_battlefield(battleField))
