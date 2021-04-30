def funcHello():
    print('안녕하세요')
    return 100 #반환값
def funcGoodBye():
    print('안녕히 가세요')
    return 10
def funcGreeting():
    funcHello()
    funcGoodBye()

funcGreeting()
print(funcHello())
print(funcGoodBye())
print(funcGreeting())
