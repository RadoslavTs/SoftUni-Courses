interviews = input().split(":")
interviews_dictionary = {}
submissions_dictionary = {}

while len(interviews) > 1:
    contest, password = interviews[0], interviews[1]
    interviews_dictionary[contest] = password
    interviews = input().split(":")

submission = input().split("=>")
while len(submission) > 1:
    user_contest_in = False
    contest, password, username, points = submission[0], submission[1], submission[2], int(submission[3])
    if contest not in interviews_dictionary:
        submission = input().split("=>")
        continue
    if password != interviews_dictionary[contest]:
        submission = input().split("=>")
        continue
    if username not in submissions_dictionary:
        submissions_dictionary[username] = []
    else:
        for submis in submissions_dictionary[username]:
            if submis[0] == contest:
                user_contest_in = True
                if submis[1] < points:
                    submis[1] = points
    if not user_contest_in:
        submission = [contest, points]
        submissions_dictionary[username].append(submission)
    submission = input().split("=>")

best_score = 0
best_participant = ""
for element in submissions_dictionary:
    total_score = 0
    for participating in submissions_dictionary[element]:
        current_score = participating[1]
        total_score += current_score
    if total_score > best_score:
        best_score = total_score
        best_participant = element

print(f"Best candidate is {best_participant} with total {best_score} points.")
print("Ranking:")

for element in sorted(submissions_dictionary):
    print(element)
    for contest, points in sorted(submissions_dictionary[element], key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")


# contests, users = {}, {}
# contest_data = input()
#
# while contest_data != "end of contests":
#     contest, password = contest_data.split(":")
#     contests[contest] = password
#     contest_data = input()
#
# submission_data = input()
#
# while submission_data != "end of submissions":
#     contest, password, username, points = [int(x) if x.isdigit() else x for x in submission_data.split("=>")]
#     if contests.get(contest) == password:
#         users[username] = users.get(username, {})
#         users[username][contest] = users[username].get(contest, 0)
#         if users[username][contest] < points:
#             users[username][contest] = points
#     submission_data = input()
#
#
# candidates = {name: sum(users[name].values()) for name in users}
# best_candidate = max(candidates, key=candidates.get)
# print(f"Best candidate is {best_candidate} with total {candidates[best_candidate]} points."
#       f"\nRanking:")
#
# for name in sorted(users):
#     print(name)
#     for contest, points in sorted(users[name].items(), key=lambda item: -item[1]):
#         print(f"#  {contest} -> {points}")
