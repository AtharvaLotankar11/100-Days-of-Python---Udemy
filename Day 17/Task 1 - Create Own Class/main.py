class User:
    def __init__(self, user_id, username): #accessing constructor - initialise
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "AtharvaLotankar11")
user_2 = User("002", "Jack1209")

print(user_1.followers)