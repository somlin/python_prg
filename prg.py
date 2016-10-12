# Enter your code here. Read input from STDIN. Print output to STDOUT



list=[]
dos= int(input())
while(dos>0):
    command = input()
    do = command.split()
    if len(do)<=0:
        continue
#    com = do[0]
    if do[0] == 'insert':
        list.insert(int(do[1]),int(do[2]))
    elif do[0] == 'append':
        list.append(int(do[1]))
    elif do[0] == 'remove':
        list.remove(int(do[1]))
    elif do[0] == 'pop':
        x = list.pop()
    elif do[0] == 'reverse':
        list.reverse()
    elif do[0] == 'sort':
        list.sort()
    elif do[0] == 'print':
        print(list)
    else:
        print('Not able to understand the command')
    dos = dos-1
