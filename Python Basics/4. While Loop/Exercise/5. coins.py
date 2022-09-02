from math import floor
initial_sum = float(input())
initial_sum = floor(initial_sum * 100)
coins_counter = int()
levas_2 = int()
levas_1 = int()
stotinki_50 = 0
stotinki_20 = 0
stotinki_10 = 0
stotinki_5 = 0
stotinki_2 = 0
stotinki_1 = 0
while initial_sum > 0:
    if initial_sum // 200 != 0:
        levas_2 = initial_sum // 200
        initial_sum -= levas_2 * 200
    if initial_sum // 100 != 0:
        levas_1 = initial_sum // 100
        initial_sum -= levas_1 * 100
    if initial_sum // 50 != 0:
        stotinki_50 = initial_sum // 50
        initial_sum -= stotinki_50 * 50
    if initial_sum // 20 != 0:
        stotinki_20 = initial_sum // 20
        initial_sum -= stotinki_20 * 20
    if initial_sum // 10 != 0:
        stotinki_10 = initial_sum // 10
        initial_sum -= stotinki_10 * 10
    if initial_sum // 5 != 0:
        stotinki_5 = initial_sum // 5
        initial_sum -= stotinki_5 * 5
    if initial_sum // 2 != 0:
        stotinki_2 = initial_sum // 2
        initial_sum -= stotinki_2 * 2
    if initial_sum == 1:
        stotinki_1 += 1
        initial_sum -= stotinki_1
total_stotinki = (levas_2 + levas_1 + stotinki_50 + stotinki_20 + stotinki_10 + stotinki_5 + stotinki_2 + stotinki_1)
print(int(total_stotinki))