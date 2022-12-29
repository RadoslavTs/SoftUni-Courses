n_number = int(input())
m_number = int(input())
s_number = int(input())
for sequence in range(m_number, n_number - 1, -1):
    if sequence % 2 == 0 and sequence % 3 == 0:
        if sequence == s_number:
            break
        print(sequence, end = " ")
