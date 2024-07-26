class User:
    counter = 1

    def __init__(self):
        self.id = f"00{self.counter}"

    def update(self):
        self.counter += 1
        self.id = f"00{self.counter}"


user_1 = User()

print(f"\n>>>> {user_1.id}")

user_1.update()

print(f"\n>>>> {user_1.id}")

user_1.update()

print(f"\n>>>> {user_1.id}")
