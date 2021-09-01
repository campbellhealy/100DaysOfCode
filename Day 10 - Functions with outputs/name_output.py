# name_output.py


def format_name(first, surname):
    if first == "" or surname == "":
        return print(
            print("Looks like you missed something. \n"),
            format_name(
                input("What is your first name? "), input("What is your surname?")
            ),
        )
    full_name = first.title() + " " + surname.title()
    return f"Your name is {full_name}"


print(format_name("vince", "healy"))
print(format_name("VINCE", "HEALY"))
print(format_name("viNce", "hEaly"))
format_name("Vince", "")
