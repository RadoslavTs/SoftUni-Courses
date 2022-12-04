message_capacity = int(input())
command = input()
people_dict = {}
while command != "Statistics":
    command_split = command.split("=")
    action = command_split[0]
    if action == "Add":
        username = command_split[1]
        sent_quantity = int(command_split[2])
        received_quantity = int(command_split[3])
        if username not in people_dict.keys():
            people_dict[username] = [sent_quantity, received_quantity]
    elif action == "Message":
        sender = command_split[1]
        receiver = command_split[2]
        if sender in people_dict.keys() and receiver in people_dict.keys():
            people_dict[sender][0] += 1
            people_dict[receiver][1] += 1
            sender_capacity = people_dict[sender][0] + people_dict[sender][1]
            receiver_capacity = people_dict[receiver][0] + people_dict[receiver][1]
            if sender_capacity >= message_capacity:
                print(f"{sender} reached the capacity!")
                del people_dict[sender]
            if receiver_capacity >= message_capacity:
                print(f"{receiver} reached the capacity!")
                del people_dict[receiver]
    elif action == "Empty":
        user = command_split[1]
        if user == "All":
            people_dict.clear()
        else:
            if user in people_dict:
                del people_dict[user]
    command = input()

print(f"Users count: {len(people_dict)}")
if len(people_dict) > 0:
    for user in people_dict:
        user_messages = people_dict[user][0] + people_dict[user][1]
        print(f"{user} - {user_messages}")
