import operator
from collections import defaultdict
from typing import Iterable, List, Tuple


class AnagramSubmissionsDatabase:

    def __init__(self):
        """
        Singleton. Use the get_instance method
        """
        self._anagram_submissions = defaultdict(int)

    @classmethod
    def get_instance(cls):
        """
        Handles access to the current instance of the singleton datastore

        :returns: The current instance of the datastore
        """
        if not hasattr(cls, '_instance'):
            cls._instance = cls()

        return cls._instance

    def record_anagram_submission(self, anagram: Iterable[str]) -> None:
        """
        Records the count of unique anagram submissions

        :param anagram: The anagram to record
        """

        # This is thread-safe due to the python Global Interpreter Lock (https://wiki.python.org/moin/GlobalInterpreterLock)
        # This does however restrict us to only ever using Python implementations which use GIL
        self._anagram_submissions[tuple(sorted(anagram))] += 1

    def get_top_anagram_submissions(self, max_results: int) -> List[Tuple[Tuple[str, ...], int]]:
        """
        Retrieves the x most popular anagram submissions

        Note: When 2 submissions have the same count the submission which was encountered first will be considered
        to be a higher rank than those first submitted later.

        :param max_results: The maximum number of results to pull
        :returns: An ordered list of anagram submissions and their counts from position 0 (most popular) to position n (least popular)
        """
        # sorted uses a stable sorting algorithm so the original ordering of the dict (i.e. insertion order) is
        # preserved for items with equal counts. https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
        return sorted(self._anagram_submissions.items(), key=operator.itemgetter(1), reverse=True)[:max_results]
