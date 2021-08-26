import class_liveList
import class_live
import class_userList
import class_user

# ユーザリストのテスト
uList = class_userList.UserList()
user = class_user.User(None, None, None, None, None)
user = uList.search_user(2)
print(user.get_name())

# ライブリストのテスト
lList = class_liveList.LiveList()
live = class_live.Live(None, None, None, None, None,None)
live = lList.search_live(2)
print(live.get_name())
