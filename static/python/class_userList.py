import class_user

#ユーザリストを表すクラス
class UserList():
    # ユーザリストの初期化
    user_list = []

    def __init__(self):
        # ユーザの作成とリストへの追加
        user1 = class_user.User(1, "user1", 0, None, None)
        UserList.user_list += [user1]
        user2 = class_user.User(2, "user2", 0, None, None)
        UserList.user_list += [user2]
        user3 = class_user.User(3, "user3", 0, None, None)
        UserList.user_list += [user3]
    
    def search_user(self,key):
        for u in UserList.user_list:
            if u.get_id() == key:
                   print(u.get_name())
                   return u


#for u in user_list:
#   if u.get_id() == key_id:
#       print(u.get_name())
