def flatten_2d(l):
    """
    Returns the flattened list, given a list of lists.

    Args:
        l (list): A 2-D list.

    Returns:
        list: Flattened list.

    """
    return [item for sublist in l for item in sublist]

def depth(l):
    """
    Returns the depth of a nested list.

    Args:
        l (list): A nested list.

    Returns:
        int: Depth of the nested list.

    """
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0