from operator import itemgetter
import subprocess as sp
import math  

def dataInit(fileName):
    tasks = []
    with open (fileName, "r") as myfile:     #Reading text file
        data = myfile.readlines()
        for l in data:
            temp = l.split()
            if temp[0] == '1':
                prev = None
            else:   
                prev = int(temp[-1])
                temp.pop(-1)
            temp.remove(';')
            stage = {
                'number' : int(temp[0]),
                'time' : int(temp[1]),
                'prev' : prev,
                'nex' : list(int(n) for n in temp[2:]),
                'per' : [0, 0]}
            tasks.append(stage)
    return tasks


def grab(data, element):
    for task in data:
        if task['number'] == element:
            return task
    return None


def folow(data, parm, task):
    T = task[parm]
    next_task = task['nex']
    while len(next_task) == 1:
        task = grab(data, next_task[0])
        T += task[parm]
        next_task = task['nex']
    if len(next_task) > 1:
        for item in next_task:
            T += folow(data, parm, grab(data, item))
    return T


def rpw(data):
    order_rpw = []
    for task in data:
        T = folow(data, 'time', task)
        order_rpw.append([task['number'], T])
    order_rpw = sorted(order_rpw, key = itemgetter(1), reverse = True)
    return order_rpw


def nextask(data, order):
    elements = []
    for el in order:
        elements.append(el[0])
    temp = []
    for item in data:
        if item['prev'] in elements:
            temp.append(item)
    temp = sorted(temp, key = lambda i: i['time'], reverse = True)
    return temp[0]


def wet(data):
    order = sorted(data, key = lambda i: i['time'], reverse = True)
    order_wet = []
    for item in order:
        if item['prev'] == None:
            task = item
            order.remove(task)
    order_wet.append([task['number'], task['time']])
    flag = True
    while flag:
        task = nextask(order, order_wet)
        order.remove(task)
        order_wet.append([task['number'], task['time']])
        if len(order) == 0:
            flag = False
    return order_wet


def solve(data, order, k, offset):
    Et = int(sum(i['time'] for i in data))
    c = round(Et/k) + offset
    wT = c * k
    wLE = (Et/wT)*100
    line = []
    count = 1
    for i in range(k):
        flag = True
        stage = []
        ussed = []
        T = i
        T = 0
        while flag:
            task = grab(data, order[0][0])
            task['per'][0] = T
            T += int(task['time'])
            task['per'][1] = T
            stage.append(task)
            ussed.append(task)
            order.pop(0)
            if count == len(data) or len(order) <= 0:
                flag = False
                line.append(stage)
                continue
            elif T + grab(data, order[0][0])['time'] > c:
                rT = c - T
                possible = []
                for item in data:
                    if item not in ussed and item['time'] <= rT:
                        possible.append(item)
                for item in possible:
                    if grab(data, item['prev']) in ussed:
                        item['per'][0] = T
                        T += int(item['time'])
                        item['per'][1] = T
                        stage.append(item)
                        ussed.append(item)
                        for n in range(len(order)):
                            if order[n][0] == item['number']:
                                order.pop(n)
                                break
                        break
                flag = False
                line.append(stage)
            count += 1
            coef = [wLE, wT]
    return [line, order, c , coef]


def solution(data):
    for i in range(len(data[0])):
        lin = '     ST' + str(i + 1) + '  '
        for item in data[0][i]:   
            lin += str(item['number']) + '(' + str(item['per'][1]) + ')  '
        print(lin)
    if len(data[1]) != 0:
        unussed = 'Nie uszeregowane: '
        for i in data[1]:
            unussed += str(i[0]) + ' '
        print(unussed)
    SI = 0
    line = data[0]
    for i in line:
        SI += (data[2] - i[-1]['per'][1])**2
    SI = math.sqrt(SI)
    print("LE = " + str(data[3][0]) + '%')
    print("SI = " + str(SI))
    print("T = " + str(data[3][1]))



print('Podaj nazwe pliku:')
fileName = input()
tasks = dataInit(fileName)

print('Podaj liczbę stacji:')
k = int(input())
print('Podaj dodatkowy czas dla każdej stacji:')
print('//0 - jak bez dodatkowego//')
offset = int(input())

sp.call('cls',shell=True)

RPW = solve(tasks, rpw(tasks), k, offset)
print('RPW,     c = ' + str(RPW[2]))
solution(RPW)
print('')
WET = solve(tasks, wet(tasks), k, offset)
print('WET,     c = ' + str(WET[2]))
solution(WET)
