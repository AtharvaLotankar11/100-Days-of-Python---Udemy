class User:
    def __init__(self, user_id, username): #accessing constructor - initialise
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "AtharvaLotankar11")
user_2 = User("002", "Jack1209")

user_1.follow(user_2)
print("Details of User 1 and 2: ")
print(f"User 1: Followers = {user_1.followers} and Following = {user_1.following}")
print(f"User 2: Followers = {user_2.followers} and Following = {user_2.following}")
