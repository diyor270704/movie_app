from register_and_login import login, register, is_admin
from movies_functions import get_like_to_movie, delete_movie, add_movie


k = int(input("enter 0 to register /n enter 1 to login\nenter 3 if you are admin\n"))
is_registered = False
user_id = 0
if k == 0:
    is_registered = register()
if (k == 0 and is_registered) or k == 1:
    user_id = login()
    if user_id != 0:
        p = int(input("0 = show movies\n1 = exit"))
        if p == 0:
           get_like_to_movie(user_id)


if k == 3:
    user_id = login()
    if is_admin(user_id):
        check_d = int(input("1 = to add movie\n2 = to delete movies\n3 = to change features of the movie\n"))
        if check_d == 1:
            add_movie()  # adds movie to movies json
        elif check_d == 2:
            delete_movie()  # deletes movie from movies json
        elif check_d == 3:
            pass
    else:
        print("make sure you are admin")



