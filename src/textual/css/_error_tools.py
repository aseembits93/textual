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
    # Convert to list once, and filter if needed
    word_list = list(words)
    if omit_empty:
        word_list = [w for w in word_list if w]
    length = len(word_list)

    if length == 0:
        return ""
    elif length == 1:
        return repr(word_list[0])
    elif length == 2:
        word1, word2 = word_list
        return f"{repr(word1)} {joiner} {repr(word2)}"
    else:
        # For more than 2, sort+repr only once each
        word_list = sorted(word_list, key=str.lower)
        words_repr = list(map(repr, word_list))
        return f'{", ".join(words_repr[:-1])}, {joiner} {words_repr[-1]}'
