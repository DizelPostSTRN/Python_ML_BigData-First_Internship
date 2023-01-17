#Task1
def transport_hub(schedule, days):
    schedule_list = [list(map(int, i.split())) for i in schedule]
    max_day_load = []
    hub = 0

    for i in range(days):
        day_load = [v for [x, v] in schedule_list if (i + 1) % x == 0]
        max_day_load.append(hub + sum(x for x in day_load if x > 0))
        hub = max(sum(day_load) + hub, 0)
    return max(max_day_load)


print(transport_hub(["2 -2", "3 3"], 7))