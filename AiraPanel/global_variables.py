

'''Declaring some Global Variable'''
import sys

MESSAGE = "Message"
ERROR = "Error"
STATUS = "Status"
UPDATE_MESSAGE = "Record updated"
INSERT_MESSAGE = "Record inserted"
OPERATION = "Operation"
INFO = "info ================= "
ERROR_MSG = "error ================= "
SUCESS = "Request sucessfully completed"
CODE = "MJ Error code"
ACTION = "Action"
LINE_NO = "Line_no"
SALES = "sales"
PURCHASES = "purchases"

def generateId(key,value):
    n = value
    str = key
    id = str+f'{n:05}'
    print("Generated id : ",id)
    return  id

def printLineNo():
    return str(format(sys.exc_info()[-1].tb_lineno))


def isnull(variable):
    if not variable or variable == '':
        return True
    else:
        return False

def whoami(request):
    username = request.user.username
    userid = request.user.id

    print("username :", username)
    print("id :", userid)
    return 0

def printCreate(module):
    return print(module," : created ")

def printUpdated(module):
    return print(module," : updated ")

def printDeleted(module):
    return print(module," : deleted ")
