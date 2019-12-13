

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


def printLineNo():
    return str(format(sys.exc_info()[-1].tb_lineno))


def isnull(variable):
    if not variable or variable == '':
        return True
    else:
        return False
