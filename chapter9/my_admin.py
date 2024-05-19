# from user import User
from admin import Admin

user_1 = Admin('Nandhini', 'Nallusamy', 26, 'Chennai')
user_1.describe_user()
user_1.privilege.show_privileges()

# user_3 = User('Rajeswari', 'Nallusamy', 49, 'Dindigul')
# user_3.describe_user()
# user_3.greet_user()
# user_3.increment_login_attempts()
# user_3.increment_login_attempts()
# user_3.increment_login_attempts()
# print(f"User 3 login attempts: {user_3.login_attempts}")
#
# user_3.reset_login_attempts()
# print(f"User 3 login attempt reset: {user_3.login_attempts}")