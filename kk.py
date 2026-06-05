import random
relic = None
hops = 0
multiplier = 1
if relic ==True:
    multiplier *= 2
    print(f"you got a relic")
for i in range(100):
    hops += multiplier
    chance = random.randint(1,2)
    if chance <= 1:
        relic = True
    else:
        relic = None

    print(f"multiplyer {multiplier}")
    print(hops)
        
