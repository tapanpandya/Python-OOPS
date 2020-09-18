# Python-OOPS

**Classes:** A class is a blueprint for how something should be defined. It doesn’t actually contain any data. The Dog class specifies that a name and an age are necessary for defining a dog, but it doesn’t contain the name or age of any specific dog.
**Instances:** While the class is the blueprint, an instance is an object that is built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.
- Parent class example
  >class Family:
    >def __init__(self, family_name, number_of_members, location):
        >self.family_name = family_name
        >self.number_of_members = number_of_members
        >self.family_located = family_located
- Parent instance example
  > family1 = Family("Family Name", 4, "Location One")
- Child class example
  >class member_details(Family):
- Child instance example
  > family1 = member_details("Family Name", 4, "Location One")

**Note:** Put another way, a class is like a form or questionnaire. An instance is like a form that has been filled out with information. Just like many people can fill out the same form with their own unique information, many instances can be created from a single class.
