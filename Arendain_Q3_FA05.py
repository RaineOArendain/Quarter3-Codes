Name = ["Serval", "Lynx", "Gepard"]
Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

total_daily = []

for i in range(len(Day)):
    total = 0
    for j in range(len(Steps)):
        total += Steps[j][i]
    total_daily.append(total)

for t in enumerate(total_daily):
    print(f"{Day[t[0]]}: {t[1]}")

active = total_daily.index(max(total_daily))
print("The most active day was", Day[active], "with", total_daily[active], "steps")