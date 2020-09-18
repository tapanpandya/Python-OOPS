from OOPS.family import Family

# Child class
# Accessing parent property
class member_details(Family):

    def addMember(self, name, age, hobby):
        i = self.number_of_members
        if self.j < i:
            self.member_list.append([name, age, hobby])
            self.j += 1
            i -= 1
        else:
            print("You have added all your members")

    def member(self):
        print("Family members: ")
        for m in self.member_list:
            print(m)

# Main starts here
family1 = member_details("Pandya", 4, "Karamsad")

# members1 = family1(Family)

family1.addMember("Hiteshbhai", 58, "Helping")
family1.addMember("Alkaben", 50, "Cooking")
family1.addMember("Hinal", 28, "Eating")
family1.addMember("Tapan", 26, "Coding")

print(family1.member())
print(family1.family_name)