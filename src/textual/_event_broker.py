from __future__ import annotations

from typing import Any, NamedTuple


class NoHandler(Exception):
    """Raised when handler isn't found in the meta."""


class HandlerArguments(NamedTuple):
    """Information for event handler."""

    modifiers: set[str]
    action: Any


def extract_handler_actions(event_name: str, meta: dict[str, Any]) -> HandlerArguments:
    """Extract action from meta dict.

    Args:
        event_name: Event to check from.
        meta: Meta information (stored in Rich Style)

    Raises:
        NoHandler: If no handler is found.

    Returns:
        Action information.
    """
    event_path = event_name.split(".")
    event_path_len = len(event_path)
    prefix = "@" + ".".join(event_path)
    prefix_len = len(prefix)

    for key, value in meta.items():
        # Fastest pre-filter: must start with "@"
        if not key.startswith("@"):
            continue

        # Only process further if enough length
        if len(key) < prefix_len or key[1:prefix_len] != prefix[1:]:
            continue

        # Split only once, and only if prefix matches
        name_args = key[1:].split(".")
        if name_args[:event_path_len] == event_path:
            modifiers = name_args[event_path_len:]
            return HandlerArguments(set(modifiers), value)

    raise NoHandler(f"No handler for {event_name!r}")
