def is_power_of(number, base):
    if number == 1:
        return True
    elif number < base:
        return False
    return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False