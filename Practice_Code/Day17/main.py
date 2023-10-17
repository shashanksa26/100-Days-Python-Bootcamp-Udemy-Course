# # passing the class function with nothing inside
# class User:
#     pass
#
#
# # defining obj for a class
# user_obj = User()
# # adding attributes in the class without constructor
# user_obj.id = "1"
# user_obj.username = "angela"
# print(user_obj.id)


# with constructor adding attributes
class Account:
    def __init__(self, account_id, account_name):
        self.id = account_id
        self.name = account_name
        self.followers = 0  # default value doesn't need parameter
        self.following = 0

    def follow(self, account):
        account.followers += 1
        self.following += 1


account1 = Account("001", "Shashank")
account2 = Account("002", "Anand")

account1.follow(account2)

print(f"{account1.id}, {account1.name}")
print(f"{account2.id}, {account2.name}")
print(account1.followers)
print(account1.following)
print(account2.followers)
print(account2.following)
