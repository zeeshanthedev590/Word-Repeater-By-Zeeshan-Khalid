i = 0
print('___________Welcome To Word Repeater ________________')
letter = input('Enter A Word/Letter You Want To Write : ')
times = int(input('Enter How Many Times You Want To Write This : '))
file = input('Choose A File Name : ')

for i in range(times):
    print(letter,end='        ')

f = open(file,'w+')
f.writelines(times*letter)