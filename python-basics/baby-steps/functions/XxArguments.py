def save_user(**user):
    print(f'user saved: {user}', type(user))


save_user(id=1, name='admin')

def save_user_id(**user):
    print(f"id saved: {user['id']}", type(user))


save_user_id(id=2, name="user2")
