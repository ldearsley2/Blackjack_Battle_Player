from typing import Final

ACE: Final[str] = "A"


def get_total(hand: list[str]) -> list[int]:
    totals = [0]
    for card in hand:
        totals = _add_multiple(get_score(card), totals)

    totals = list(set(totals))
    totals.sort()
    return totals


def _add_single(amount: int, totals: list[int]) -> list[int]:
    return [t + amount for t in totals]


def _add_multiple(amounts: list[int], totals: list[int]) -> list[int]:
    result: list[int] = []
    for a in amounts:
        result.extend(_add_single(a, totals))

    return result


def get_score(card: str) -> list[int]:
    value = card[:-1]

    if value == ACE:
        return [1, 11]
    elif value.isdigit():
        return [int(value)]

    return [10]
