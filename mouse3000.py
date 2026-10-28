#rewrite whole movement bruh
from sys import exit

WIDTH = 5
HEIGHT = 5
cheese_amount = 2

world = [
    {"name": "mouse", "x": 0, "y": 4, "emoji": "🐭"},
    {"name": "cheese", "x": 2, "y": 2, "is_eaten": False, "emoji": "🧀"},
    {"name": "cheese", "x": 4, "y": 3, "is_eaten": False, "emoji": "🧀"},
    {"name": "hunter", "x": 4, "y": 1, "emoji": "👨"},
    {"name": "door", "x": 4, "y": 4, "emoji": "🚪"}
]

moves = [
    {"key": "w", "axis": "y", "adjustment": -1},
    {"key": "s", "axis": "y", "adjustment": 1},
    {"key": "d", "axis": "x", "adjustment": 1},
    {"key": "a", "axis": "x", "adjustment": -1},
]

def render() -> str:
    for i in range(100): print('\n', end='')
    for y in range(0, HEIGHT):
        line = []
        line = ["⬜"] * WIDTH
        for item in world:
            if item["y"] == y:
                if item["name"] == 'cheese':
                    if item["is_eaten"]:
                        continue

                line[item["x"]] = item["emoji"]

        print("".join(line))
    return input()


def legal_check(new_x, new_y) -> bool:
    if new_x not in range(0, WIDTH):
        return False
    if new_y not in range(0, HEIGHT):
        return False
    return True

def actual_movement(move) -> None:
    _move = next(obj for obj in moves if obj["key"] == move)
    _mouse = next(obj for obj in world if obj["name"] == 'mouse')

    if _mouse is not None:
        if _move["axis"] == "y" and legal_check(_mouse["x"], _mouse["y"] + _move["adjustment"]):
            _mouse["y"] += _move["adjustment"]
        if _move["axis"] == "x" and legal_check(_mouse["x"] + _move["adjustment"], _mouse["y"]):
            _mouse["x"] += _move["adjustment"]

def collision_check():
    global cheese_amount
    _mouse = next(obj for obj in world if obj["name"] == 'mouse')
    for item in world:
        if item["name"] == "mouse":
            continue
        else:
            if _mouse["x"] == item["x"] and _mouse["y"] == item["y"]:
                if item["name"] == 'cheese':
                    item["is_eaten"] = True
                    cheese_amount = cheese_amount - 1
                if item["name"] == 'door' and cheese_amount == 0:
                    print("Won!")
                    exit(0)
                if item["name"] == 'hunter':
                    print("Died")
                    exit(1)

def hunter_move() -> None:
    _hunter = next(obj for obj in world if obj["name"] == 'hunter')
    _mouse = next(obj for obj in world if obj["name"] == 'mouse')

    if _hunter["x"] > _mouse["x"]:
        _hunter["x"] -= 1
    elif _hunter["x"] < _mouse["x"]:
        _hunter["x"] += 1
    else:
        if _hunter["y"] > _mouse["y"]:
            _hunter["y"] -= 1
        else:
            _hunter["y"] += 1

def main() -> None:
    while True:
        move = render().lower()
        try:
            actual_movement(move)
        except StopIteration:
            continue
        hunter_move()
        collision_check()


if __name__ == "__main__":
    main()