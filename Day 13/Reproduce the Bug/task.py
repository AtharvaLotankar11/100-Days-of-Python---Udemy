from random import randint

# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])


"""
This will Reproduce Bug because Array starts from 0 to n-1
two_coins = ["[H][H]", "[H][T]", "[T][H]", "[T][T]"]
total_outcome = randint(1, 4)
print(two_coins[total_outcome])

"""



two_coins = ["[H][H]", "[H][T]", "[T][H]", "[T][T]"]
total_outcome = randint(0, 3)
print(two_coins[total_outcome])
