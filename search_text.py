"""Functions for searching for text within other text.
"""


def search_text(text_to_search: str, sub_text: str):
    """Return the character positions of all occurrences of the sub text in the text.

    Args:
        text_to_search: The text to search within
        sub_text: The text to search for

    Returns:
        A comma separated list of the character positions
        '<No Output>' if sub_text does not occur within text_to_search
    """

    found = []
    range_to_check = range(len(text_to_search) - len(sub_text) + 1)

    for i in range_to_check:
        sub_text_end = i + len(sub_text)
        text_to_check = text_to_search[i: sub_text_end]
        if text_to_check.lower() == sub_text.lower():
            found.append(i)

    if found:
        # Add one because we want the position rather than the index
        found_positions = [str(i+1) for i in found]
        return _join(found_positions, ', ')

    return '<No Output>'


def _join(items: list, join_with: str):
    """Return a string representation of items, separated by another string

    This can be replaced by join_with.join(items) if such methods are allowed.

    Args:
        items: a list of strings
        join_with:

    Returns:
        A string of items, where each item is separated by the join with string
    """
    joined = ''
    for item in items:
        joined += item
        if item is not items[-1]:
            joined += join_with
    return joined
