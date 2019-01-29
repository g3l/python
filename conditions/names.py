people = ["Akshay Patel", "Bez Maluk", "Chris Campbell", "Chris Rushton", "Asega Lemi"]

people.append("Godfrey Lemi")
for user in people:
    if user.startswith("A") or user.endswith("n"):
        print(user)
