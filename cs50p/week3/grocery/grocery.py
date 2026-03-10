grocery = {}
while True:
    try:
        item = input().upper()
        grocery[item] += 1
    except KeyError:
        grocery[item] = 1
    except EOFError:
        break
for item in sorted(grocery):
    print(grocery[item], item)
