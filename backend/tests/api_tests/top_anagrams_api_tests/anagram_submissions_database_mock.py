from dal.anagram_submissions_database import AnagramSubmissionsDatabase


class AnagramSubmissionsDatabaseMock(AnagramSubmissionsDatabase):

    def __init__(self):
        super().__init__()
        self._anagram_submissions = {
            ('', ''): 1,
            tuple('artist'): 2,
            ('beat', 'beta'): 2,
            ('abut', 'tuba'): 3,
            ('acre', 'race'): 4,
            ('dart', 'rate'): 5,
            ('mane', 'mean'): 5,
            ('anew', 'wane'): 6,
            ('arts', 'rats'): 7,
            ('baste', 'beast'): 8,
            ('canter', 'nectar'): 9,
            ('caller', 'cellar'): 10,
            ('hardest', 'threads'): 11,
            ('claimed', 'decimal'): 12,
            ('actress', 'casters', 'recasts'): 13
        }
