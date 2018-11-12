from math import gcd as bltin_gcd
import random


def isPrime2(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False

    return True


def calculate_M_number():
    q = (int)(random.uniform(2 ** 10, 2 ** 16))
    p = (int)(random.uniform((2 ** 10) + 1, (2 ** 16) + 1))
    if (p == q):
        p = p - 1

    check = True
    while check:
        if isPrime2(p) == False or (p % 4 != 3):
            p = p - 1
        elif isPrime2(q) == False or (p % 4 != 3):
            q = q - 1
        else:
            check = False
    return p * q


def coprime(a, b):
    return bltin_gcd(a, b) == 1


def calculate_first_x(M):
    x = (int)(random.uniform(2, 100))
    check = True
    while check:
        if coprime(x, M):
            check = False
        else:
            x = +1
    return x


def generate_nums(x, M, iter):
    nums = []
    while iter != 0:
        next_num = (x ** 2) % M
        x = next_num
        nums.append(next_num)
        iter = iter - 1
    return nums


def get_bits_from_nums_array(nums):
    bits = []
    for num in nums:
        bits.append(bin(num)[-1])

    return bits


def proportional_test(bits):
    """Returns the number of bits with value of 0"""
    zero_counter = 0
    for b in bits:
        if b == '0':
            zero_counter += 1
    return zero_counter


def series_test(bits):
    counter = 0
    len_1 = 0
    len_2 = 0
    len_3 = 0
    len_4 = 0
    len_5 = 0
    len_long = 0
    len_toolong = 0
    previous_bit = bits[0]
    for b in bits:
        if b == previous_bit:
            counter += 1
        else:
            if counter == 1:
                len_1 += 1
            if counter == 2:
                len_2 += 1
            if counter == 3:
                len_3 += 1
            if counter == 4:
                len_4 += 1
            if counter == 5:
                len_5 += 1
            if counter >= 6:
                len_long += 1
                if counter >= 26:
                    len_toolong += 1
            counter = 0
        previous_bit = b
    return [len_1, len_2, len_3, len_4, len_5, len_long, len_toolong]


def poker_test(bits):
    combination_counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i=0
    while i<=(len(bits)-3):
        combination = [bits[i], bits[i + 1], bits[i + 2], bits[i + 3]]
        if combination == ['0', '0', '0', '0']:
            combination_counter[0]+=1
        if combination == ['0', '0', '0', '1']:
            combination_counter[1]+=1
        if combination == ['0', '0', '1', '0']:
            combination_counter[2]+=1
        if combination == ['0', '0','1', '1']:
            combination_counter[3] += 1
        if combination == ['0', '1', '0', '0']:
            combination_counter[4] += 1
        if combination == ['0', '1', '0', '1']:
            combination_counter[5] += 1
        if combination == ['0', '1', '1', '0']:
            combination_counter[6] += 1
        if combination == ['0', '1', '1', '1']:
            combination_counter[7] += 1
        if combination == ['1', '0', '0', '0']:
            combination_counter[8] += 1
        if combination == ['1', '0', '0', '1']:
            combination_counter[9] += 1
        if combination == ['1', '0', '1', '0']:
            combination_counter[10] += 1
        if combination == ['1', '0', '1', '1']:
            combination_counter[11] += 1
        if combination == ['1', '1', '0', '0']:
            combination_counter[12] += 1
        if combination == ['1', '1', '0', '1']:
            combination_counter[13] += 1
        if combination == ['1', '1', '1', '0']:
            combination_counter[14] += 1
        if combination == ['1','1', '1', '1']:
            combination_counter[15] += 1
        i=i+4
    return combination_counter

passed_ctr = 0
propotional_pass_ctr=0
series_pass_ctr=0
long_series_pass_ctr=0
poker_pass_ctr=0
for a in range(0, 1000):
    M = calculate_M_number()
    x = calculate_first_x(M)
    a = generate_nums(x, M, 20000)
    b = get_bits_from_nums_array(a)
    prop = proportional_test(b)
    serie = series_test(b)
    poker= poker_test(b)
    poker_sum=0
    for index in poker:
        poker_sum=poker_sum+index**2
    poker_value = ((16*poker_sum)/5000)-5000

    if (prop > 9725 and prop < 10275):
        propotional_pass_ctr+=1

    if ((serie[0] > 2315 and serie[0] < 2685) and
            (serie[1] > 1114 and serie[1] < 1386) and
            (serie[2] > 537 and serie[2] < 723) and
            (serie[3] > 240 and serie[3] < 384) and
            (serie[4] > 103 and serie[4] < 209) and
            (serie[5] > 103 and serie[5] < 209)):
        series_pass_ctr+=1
    if serie[6] == 0:
        long_series_pass_ctr+=1
    if ((poker_value>2.16) and (poker_value<46.17)):
        poker_pass_ctr+=1


print(propotional_pass_ctr)
print(series_pass_ctr)
print(long_series_pass_ctr)
print(poker_pass_ctr)
