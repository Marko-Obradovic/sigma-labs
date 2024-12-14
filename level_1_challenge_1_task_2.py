def get_name():
    name = input("What's your first name?: ")
    return name.title().strip()


def get_greeting(name):
    if name in {"Alice", "Bob"}:
        return(f"Hello {name}!")
    else:
        return("Sorry... You're not authorised to be greeted!")


def main(name):
    greeting_string = name
    print(greeting_string)

if __name__ == "__main__":
    main(get_greeting(get_name()))


