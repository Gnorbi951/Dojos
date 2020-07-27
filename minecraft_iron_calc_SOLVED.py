def calc_fuel(n):
    result = {"lava": 0, "blaze rod": 0, "coal": 0, "wood": 0, "stick": 0}

    # n is for iron ingot number, each takes 11 seconds to make

    time_needed = n * 11

    while time_needed != 0:
        if time_needed >= 800:
            time_needed -= 800
            result["lava"] += 1
            continue
        if time_needed >= 120:
            time_needed -= 120
            result["blaze rod"] += 1
            continue
        if time_needed >= 80:
            time_needed -= 80
            result["coal"] += 1
            continue
        if time_needed >= 15:
            time_needed -= 15
            result["wood"] += 1
            continue
        if time_needed >= 1:
            time_needed -= 1
            result["stick"] += 1

    return result


calc_fuel(145)
