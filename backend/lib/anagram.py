def are_anagrams(*words: str) -> bool:
    """
    Checks whether all words passed are anagrams of each other

    This will return True for the cases where less than 2 words are passed.
    i.e. Nothing and a single word are considered anagrams of themselves

    :param words: The words to compare against each other
    :returns: True if all words are anagrams of each other; False otherwise
    """
    return len({''.join(sorted(word)) for word in words}) < 2
