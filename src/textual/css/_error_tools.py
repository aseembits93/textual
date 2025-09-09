from __future__ import annotations

from typing import Iterable


def friendly_list(
    words: Iterable[str], joiner: str = "or", omit_empty: bool = True
) -> str:
    """Generate a list of words as readable prose.

    >>> friendly_list(["foo", "bar", "baz"])
    "'foo', 'bar', or 'baz'"

    Args:
        words: A list of words.
        joiner: The last joiner word.

    Returns:
        List as prose.
    """
    # Materialize and filter once, to avoid extra sorting/comprehension steps
    filtered = []
    add_word = filtered.append
    for word in words:
        if word or not omit_empty:
            add_word(word)
    if not filtered:
        return ""
    # If only one or two items, avoid the sort/repr round-trip
    if len(filtered) == 1:
        return repr(filtered[0])
    elif len(filtered) == 2:
        return f"{repr(filtered[0])} {joiner} {repr(filtered[1])}"
    # Sort only as needed for more than 2 items
    filtered.sort(key=str.lower)
    words_repr = [repr(word) for word in filtered]
    return f'{", ".join(words_repr[:-1])}, {joiner} {words_repr[-1]}'
