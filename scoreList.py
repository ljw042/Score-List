print('1. Show ranking & mean of scores')
print('2. Add scores')
print('3. Delete a score')
n = int(input('4. Exit'))
L=[]
if n == 1:
    if len(L) == 0:
        print('리스트가 비어있습니다.')
    else:
        L.sort(reverse = True)
        print('='*20)
        for i in range(0, len(L)):
            print('i   L(i)')
            
if n == 2:
    if True:
        print('Enter score (0. .100) (otherwise exit)')
        score = int(input('score: '))
        L.append(score)
        print(L)
    
