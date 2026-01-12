
Name = ["Serval", "Lynx", "Gepard"]
Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

for i in range(len(Steps)):
    total = 0
    Highest = Steps[i][0]
    Lowest = Steps[i][0]

    for j in range(len(Steps[i])):
        total += Steps[i][j]
        if Steps[i][j] > Highest:
            Highest = Steps[i][j]
        if Steps[i][j] < Lowest:
            Lowest = Steps[i][j]

    average = total / len(Steps[i])

    print(
        Name[i],
        "| Total Steps: ", total,
        "| Average: ", average,
        "| Min: ", Lowest,
        "| Max: ", Highest
    )