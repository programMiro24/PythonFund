limit_of_messages = int(input())
users = {}

def validate_users_for_send(sender_username: str, receiver_username: str, dict_users: dict) -> bool:
    return sender_username in dict_users and receiver_username in dict_users

def check_is_username_reached_capacity(username_str:  str, dict_users: dict, limit: int) -> None:
    count_of_messages = dict_users[username_str]['received'] + dict_users[username_str]['sent']
    if count_of_messages >= limit:
        dict_users.pop(username_str)
        print(f"{username_str} reached the capacity!")

while (command := input()) != 'Statistics':
    command = command.split('=')
    action = command[0]
    if action == 'Add':
        username = command[1]
        if username not in users:
            sent, received = map(int, command[2:])
            users[username] = {'sent': 0, 'received': 0}
            users[username]['sent'] += sent
            users[username]['received'] += received
    elif action == 'Message':
        sender, receiver = command[1:]
        if validate_users_for_send(sender, receiver, users):
            users[sender]['sent'] += 1
            users[receiver]['received'] += 1
            check_is_username_reached_capacity(sender, users, limit_of_messages)
            check_is_username_reached_capacity(receiver, users, limit_of_messages)
    elif action == "Empty":
        username = command[1]
        if username == "All":
            users = {}
        else:
            users.pop(username)

print(f"Users count: {len(users)}")
for user, user_data in users.items():
    all_messages = user_data['sent'] + user_data['received']
    print(f"{user} - {all_messages}")
