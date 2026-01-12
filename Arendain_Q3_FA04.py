Name = ["Serval", "Lynx", "Gepard"]
Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

total = [sum(i) for i in Steps]

most = total.index(max(total))

Highest = max(total)
Lowest = min(total)

Difference = Highest - Lowest
print("The person with the most steps is", Name[most], "with", Highest, "steps.")
print("The difference between the most and least steps is", Difference)
