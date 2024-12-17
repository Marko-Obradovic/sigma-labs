'''
A program that asks the user for their name and either:

1. Greets them with their name in the console if authorised
2. Rejects authorisation if name is not authorised'''

def get_name() -> str:
    name: str = input("What's your first name?: ")
    return name.title().strip()


def get_greeting(name: str) -> str:
    if name in {"Alice", "Bob"}:
        return f"Hello {name}!"
    return "Sorry... You're not authorised to be greeted!"


def main(greeting: str) -> str:
    print(greeting)

if __name__ == "__main__":
    main(get_greeting(get_name()))
