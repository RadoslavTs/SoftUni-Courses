input_list = list(map(int, input().split(", ")))
minimum_wealth = int(input())
balanced = True
for person in range(len(input_list)):
    if input_list[person] < minimum_wealth:
        needed = minimum_wealth - input_list[person]
        for sequence in range(len(input_list)-1, -1, -1):
            wealthiest_value = max(input_list)
            wealthiest_index = input_list.index(wealthiest_value)
            current_last = input_list[wealthiest_index]
            if current_last > minimum_wealth:
                available = input_list[wealthiest_index] - minimum_wealth
                if available > needed:
                    given = needed
                    needed = 0
                    input_list[person] = minimum_wealth
                    input_list[wealthiest_index] = current_last - given
                else:
                    given = available
                    needed -= given
                    input_list[person] += given
                    input_list[wealthiest_index] = current_last - given

            else:
                continue
    else:
        continue
for balance in input_list:
    if balance < minimum_wealth:
        balanced = False
        break
    else:
        continue
if balanced:
    print(input_list)
else:
    print("No equal distribution possible")