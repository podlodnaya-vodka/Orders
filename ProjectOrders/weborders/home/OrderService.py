import copy
import json
from operator import attrgetter
import datetime
class Order():
    def __init__(self, git, dept, count, price, dateb, datef, correct, delete):
        self.git = git
        self.dept = dept
        self.count = count
        self.price = price
        self.dateb = dateb
        self.datef = datef
        self.correct = correct
        self.delete = delete

    def serializer(self):
        return {
            'git': self.git,
            'dept': self.dept,
            'count': self.count,
            'price': self.price,
            'dateb': self.dateb,
            'datef': self.datef,
            'correct': self.correct,
            'delete': self.delete
        }




listOrders = [
    Order(11111, 'рик',  5,30, datetime.date(2024,2,3),datetime.date(2024,8,6),0,0),
    Order(11111, 'орм',  2,50, datetime.date(2024,1,1),datetime.date(2024,8,1),1,0),
    Order(11111, 'орип', 8,25, datetime.date(2024,2,2),datetime.date(2024,8,6),0,0),
    Order(33333, 'рик', 8,25, datetime.date(2024,2,2),datetime.date(2024,8,6),0,0),
    Order(55555, 'рик',  5,300,datetime.date(2024,2,3),datetime.date(2024,8,6),0,1),
    Order(55555, 'рик',  8,200,datetime.date(2024,7,8),datetime.date(2024,12,6),0,0)
]

def getAllOrders():
    list = sorted(listOrders, key=attrgetter("delete"))
    list = sorted(list, key=attrgetter("git"))

    git = 0
    obj = ''
    listRes = []
    for order in list:
        if (order.delete == 0 and git != order.git):
            git = order.git
            if (obj != ''):
                listRes.append(obj)
            obj = copy.deepcopy(order)
            obj.sum = 1
        elif (order.delete == 0 and git == order.git):
            obj.sum += 1
            if (obj.dateb > order.dateb):
                obj.dateb = order.dateb
            if (obj.datef < order.datef):
                obj.datef = order.datef
            if (order.correct == 1):
                obj.correct = 1
            obj.count += order.count
            obj.price += order.price
            obj.dept += f", {order.dept}"
        elif (order.delete == 1 and git == order.git):
            obj.delete = 1
    if (obj != ''):
        listRes.append(obj)
    return listRes

def getOrdersByGit(git):
    list = sorted(listOrders, key=attrgetter("datef"))
    list = sorted(list, key=attrgetter("dateb"))

    listRes = []
    for order in list:
        if (order.git == git):
            listRes.append(order.serializer())
    return listRes
