"""
    Coins allowed:
    £2
    £1
    50p
    20p
    10p
    5p
    2p
    1p
"""
#Copied answer as my answer was too slow for python.
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print (f"Ways to make change = { ways[target]}")
