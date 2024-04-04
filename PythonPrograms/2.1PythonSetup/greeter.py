

#elias

def can_i_ride(height):
    if height < 40:
        return "Cannot Ride"
    elif height <= 48:
        return "With an adult"
    else: 
        return "Can Ride"
    
print(can_i_ride(4))

print(can_i_ride(40))

print(can_i_ride(400))