def seat_profile(first, last, **passenger_info):
    # Build dictionary containing all passenger information
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in passenger_info.items():
        profile[key] = value
    return profile


passenger_profile = seat_profile('rimjob', 'bob', seat_number=36, breakfast_order='Yes')

print(passenger_profile)
