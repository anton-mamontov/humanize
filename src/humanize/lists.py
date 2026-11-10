"""Lists related humanization."""

from __future__ import annotations

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any

__all__ = ["natural_list"]


def natural_list(
    items: Iterable[Any],
    conjunction: str = "and",
    oxford_comma: bool = False,
    max_items: int | None = None,
) -> str:
    """Natural list.

    Convert an iterable of items into a human-readable string with commas and 'and'.

    Examples:
        >>> natural_list(["one", "two", "three"])
        'one, two and three'
        >>> natural_list(["one", "two"])
        'one and two'
        >>> natural_list(["one"])
        'one'
        >>> natural_list(["one", "two", "three"], conjunction="or")
        'one, two or three'
        >>> natural_list(["one", "two", "three"], oxford_comma=True)
        'one, two, and three'
        >>> natural_list(["a", "b", "c", "d", "e"], max_items=2)
        'a, b and 3 others'

    Args:
        items (Iterable): An iterable of items.
        conjunction (str): Word used to join the last item. Defaults to "and".
        oxford_comma (bool): Put a comma before the conjunction.
        max_items (int, optional): Show at most this many items, summarising the
            rest as "N others".

    Returns:
        str: A string with commas and the conjunction in the right places.
    """
    item_list = [str(item) for item in items]
    if not item_list:
        return ""
    if max_items is not None and len(item_list) > max_items:
        hidden = len(item_list) - max_items
        item_list = item_list[:max_items] + [f"{hidden} others"]
    if len(item_list) == 1:
        return item_list[0]
    separator = ", " if oxford_comma else " "
    if len(item_list) == 2:
        return f"{item_list[0]}{separator.rstrip()} {conjunction} {item_list[1]}"
    return ", ".join(item_list[:-1]) + f"{separator.rstrip()} {conjunction} {item_list[-1]}"
