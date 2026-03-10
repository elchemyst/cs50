due = 50
print('Amount Due:', due)
while True:
    coin = int(input('Insert Coin:'))
    if not coin in [5, 10, 25]:
        print('Amount Due:', due)
    elif coin in [5, 10, 25]:
        due = due - coin
        if not due <= 0:
            print('Amount Due:', due)
    if due <= 0:
        print('Change Owed:', -due)
        break
