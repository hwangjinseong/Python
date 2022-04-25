day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
dday = 0
monthInput, dayInput = map(int, input().split())

for i in range(monthInput-1):
    dday = dday + day[i]
dday = (dday + dayInput) % 7
print(week[dday])