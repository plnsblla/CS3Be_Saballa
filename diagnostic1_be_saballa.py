def calculate_space_weight(earth_weight, destination):
    if destination == "Mars":
        space_weight = earth_weight*0.38
        return space_weight
    elif destination=="Jupiter":
        space_weight = earth_weight*2.34
        return space_weight
    elif destination=="The Moon":
        space_weight = earth_weight*0.16
        return space_weight
    else:
        print("Error: invalid destination")
        space_weight = 0
        return space_weight

earth_weight = float(input("Earth weight: "))
destination = str(input("Destination: "))
space_weight=calculate_space_weight(earth_weight, destination)
print("Space weight =", space_weight)

