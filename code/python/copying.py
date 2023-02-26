
class TestDeepcopy:
    def __deepcopy__(self, memo: dict[int, object]) -> MissileBasic:
        """Returns a copy of itself.

        https://stackoverflow.com/questions/1500718/how-to-override-the-copy-deepcopy-operations-for-a-python-object
        """
        missile = MissileBasic(*self.get_copy_tuple())
        memo[id(self)] = missile
        return missile
