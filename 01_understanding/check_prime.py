import math


def check_prime(num):
    sqrt_num = math.sqrt(num)
    for i in range(2, int(sqrt_num) + 1):
        if (num / i).is_integer():
            return False
    return True


print(f"check_prime(10,000,000) = {check_prime(10_000_000)}")
#return False
print(f"check_prime(10,000,019) = {check_prime(10_000_019)}")

