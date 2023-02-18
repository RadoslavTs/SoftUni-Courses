def flights(*flight_plans):
    flight_dict = {}
    for i in range(0, len(flight_plans), 2):
        if flight_plans[i] == "Finish":
            break
        if flight_plans[i] not in flight_dict.keys():
            flight_dict[flight_plans[i]] = flight_plans[i+1]
        else:
            flight_dict[flight_plans[i]] += flight_plans[i+1]

    return flight_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))