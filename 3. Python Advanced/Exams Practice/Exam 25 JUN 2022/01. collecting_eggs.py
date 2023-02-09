from collections import deque

eggs = deque(list(map(int, input().split(', '))))
papers = deque(list(map(int, input().split(', '))))
box = 0

while eggs and papers:
    current_egg = eggs.popleft()
    current_paper = papers.pop()

    if current_egg <= 0:
        papers.append(current_paper)
        continue

    if current_egg == 13:
        paper_to_switch = papers.popleft()
        papers.append(paper_to_switch)
        papers.appendleft(current_paper)
        continue

    if current_egg + current_paper <= 50:
        box += 1

if box >0:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print("Eggs left: ", end='')
    print(*eggs, sep=', ')
if papers:
    print("Pieces of paper left: ", end='')
    print(*papers, sep=', ')
