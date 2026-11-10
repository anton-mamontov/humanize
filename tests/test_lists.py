from __future__ import annotations

from collections.abc import Iterable
from typing import Any

import pytest

import humanize


@pytest.mark.parametrize(
    "test_args, expected",
    [
        ([["1", "2", "3"]], "1, 2 and 3"),
        ([["one", "two", "three"]], "one, two and three"),
        ([["one", "two"]], "one and two"),
        ([["one"]], "one"),
        ([[]], ""),
        ([[""]], ""),
        ([[1, 2, 3]], "1, 2 and 3"),
        ([[1, "two"]], "1 and two"),
        ([("one", "two", "three")], "one, two and three"),
        ([("one", "two")], "one and two"),
        ([("one",)], "one"),
        ([{"one": 1, "two": 2}.keys()], "one and two"),
        ([(x for x in ["one", "two", "three"])], "one, two and three"),
        ([range(1, 4)], "1, 2 and 3"),
    ],
)
def test_natural_list(test_args: Iterable[Any], expected: str) -> None:
    assert humanize.natural_list(*test_args) == expected


@pytest.mark.parametrize(
    "kwargs, expected",
    [
        ({"conjunction": "or"}, "one, two or three"),
        ({"oxford_comma": True}, "one, two, and three"),
        ({"conjunction": "or", "oxford_comma": True}, "one, two, or three"),
    ],
)
def test_natural_list_options(kwargs: dict[str, Any], expected: str) -> None:
    assert humanize.natural_list(["one", "two", "three"], **kwargs) == expected


def test_natural_list_max_items() -> None:
    items = ["a", "b", "c", "d", "e"]
    assert humanize.natural_list(items, max_items=2) == "a, b and 3 others"
    assert humanize.natural_list(items, max_items=5) == "a, b, c, d and e"
