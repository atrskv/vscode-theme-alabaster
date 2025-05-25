import random


class User:
    '''Class for creating user objects with name and random ID.'''

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = random.randint(1000, 9999)

    @property
    def name_length(self) -> int:
        return len(self.name)

    def greet(self) -> None:
        print(f'Hello, {self.name}! Your ID is {self.id}.')

    # TODO: ...


def main() -> None:
    names = ['Alice', 'Bob', 'Charlie']
    users = [User(name) for name in names]

    for user in users:
        user.greet()


if __name__ == '__main__':
    main()
