# from .cars import Car
class Family:
    member_list = []
    j = 0
    """This is one family class which will have many relatives
    and which will have many family members."""
    def __init__(self, family_name, number_of_members, family_located):
        self.family_name = family_name
        self.number_of_members = number_of_members
        self.family_located = family_located

    def __str__(self):
        return f"{self.family_name} has {self.number_of_members} members."

