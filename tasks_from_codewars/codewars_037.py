"""
Santa puts all the presents into the huge sack. In order to let his reindeers rest a bit, he only takes as many reindeers with him as he is required to do. The others may take a nap.

Two reindeers are always required for the sleigh and Santa himself. Additionally he needs 1 reindeer per 30 presents. As you know, Santa has 8 reindeers in total, so he can deliver up to 180 presents at once (2 reindeers for Santa and the sleigh + 6 reindeers with 30 presents each).

Complete the function reindeers(), which takes a number of presents and returns the minimum numbers of required reindeers. If the number of presents is too high, throw an error.

Examples (input -> output / error)
0 -> 2
1 -> 3
30 -> 3
200 -> throws an error

"""


def reindeer(presents):
    if presents / 30 > 6:
        return 'Error'
    elif presents % 30:
        return presents // 30 + 3
    else:
        return presents // 30 + 2


print(reindeer(presents=200))
