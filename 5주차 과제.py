
array=list(map(int, input().split()))
print(array)

commands=[]
for i in range(3):
    commands.append(list(map(int, input().split())))
    
print(commands)

def solution(array, commands):
    
    for j in range(3):
        tmp=array[commands[j][0]-1 : commands[j][1]]
        tmp.sort()
        print(tmp[commands[j][2]-1])

solution(array, commands)
    
