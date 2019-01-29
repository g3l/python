# Modify this function to return a list of names as defined below
def list_boys():
    return "Godfrey Lemi", "Sam Abui", "Eric Justin", "Andrew Wadok", "Francis Kale", "Declan Brooks", "Emmanuel Yoak", "Tony Lemi", "Moses Yoak"

# Modify this function to concatenate to each person - " = Gender"
def build_sentence(gender):
    return "%s = Male" % gender

def name_the_benefits_of_functions():
    list_of_boys = list_boys()
    for benefit in list_of_boys:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
