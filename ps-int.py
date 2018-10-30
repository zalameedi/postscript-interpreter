opstack = [] #operand stack
dictstack = [] #dictionary stack

#operand's methods first

#Pops a value off the operand stack and returns the number
def opPop():
    try:
        return opstack.pop()
    except:
        print("Operand stack is empty.")

#Pushes a value on top of the stack
def opPush(value):
    opstack.append(value)

#dictionary's methods 

#Pops a value off the dictionary stack and returns the dict
def dictPop():
    try:
        return dictstack.pop()
    except:
        print("Dictionary stack is empty.")

#pushes a dictionary onto the dict stack
def dictPush(d):
    dictstack.append(d)

#Initializes the definition of a dict
def define(name, value):
        if len(dictstack) > 0:
                dictstack[len(dictstack)-1][name]=value #Set dict
        else:
                myDict ={}
                myDict[name]=value
                dictstack.append(myDict)
        # if len(dictstack) < 1:
        #     myDict = {}
        #     temp = 0
        # else:
        #         (myDict, temp) = dictPop()
        # myDict[name] = value
        # dictPush(myDict, temp)


#Needs to be worked on in part 2
def lookup(name):
        for myDict in reversed(dictstack):
            if myDict.get('/' + name, None) != None:
                    return myDict.get('/' + name, None)
        return None

def stack():
    for i in reversed(opstack):
        print(i)


# Arithmetic operators methods will reside below #

def add():
        if(len(opstack) > 1):
                op1 = opPop()
                op2 = opPop()
                opPush(op1 + op2)
        else:
                print("Stack doesn't have enough items.")

def sub():
        if(len(opstack) > 1):
                op1 = opPop()
                op2 = opPop()
                opPush(op2 - op1)
        else:
                print("Stack doesn't have enough items.")

def mul():
        if(len(opstack) > 1):
                op1 = opPop()
                op2 = opPop()
                opPush(op1 * op2)
        else:
                print("Stack doesn't have enough items.")

def div():
        if(len(opstack) > 1):
                op1 = opPop()
                op2 = opPop()
                opPush(op2 / op1)
        else:
                print("Stack doesn't have enough items.")

def eq():
        if(len(opstack) > 1):
                op1 = opPop()
                op2 = opPop()
                opPush(op1 == op2)
        else:
                print("Stack doesn't have enough items.")

def lt():
        if(len(opstack) > 1):
                op1 = opPop()
                op2 = opPop()
                opPush(op1 > op2)
        else:
                print("Stack doesn't have enough items.")

def gt():
        if (len(opstack) > 1):
                op1=opPop()
                op2=opPop()
                opPush(op2 > op1)
        else:
                print("Stack doesn't have enough items.")
   

# *** TESTED ALL OF THE METHODS WITH GHOSTSCRIPT THE BEHAVIOR IS CORRECT *** #

def exch():
    temp1 = opPop()
    temp2 = opPop()
    opPush(temp1)
    opPush(temp2)

def dup():
    temp1 = opPop()
    opPush(temp1)
    opPush(temp1)

def clear():
    opstack[:] = [] #Courtesy of stackoverflow 
    

#Misc functions I missed

def copy():
        if (len(opstack) > 0):
                tempLst = []
                temp = opPop()
                for i in range(0, temp):
                        tempLst.append(opPop())
                for j in reversed(tempLst):
                        opPush(j)
                for j in reversed(tempLst):
                        opPush(j)
        else:
                print("Stack is empty")       


def get():
        myLst = []
        if len(opstack) > 1:
                index = opPop()
                tempList = opPop()
                if (isinstance(tempList, list) and (isinstance(index, int))):
                        x = tempList.pop(index)
                        opPush(x)
                else:
                        print("List not available. Either variables do not match the expected data type.")
        else:
                print("Stack is empty.")
        

def length():
        myLst = []
        increment = 0
        if len(opstack) > 0:
                myLst = opPop()
                for i in myLst:
                        increment += 1
                opPush(increment)
        else:
                print("Stack is empty.")

def psDict():
        if len(opstack) > 0:
                opPop()
                opPush({})
        else:
                print("Stack is empty.")

def begin():
        myDict = {}
        if len(opstack) > 0:
                myDict = opPop()
                dictPush(myDict)
        else:
                print("Stack is empty")

def end():
        dictPop()
        

def psDef():
        value = opPop()
        key = opPop()
        define(key, value)

def psAnd():
        if(len(opstack) > 1):
                op2=opPop()
                op1=opPop()
                if (((isinstance(op1,int) or (isinstance(op1,float)) and (isinstance(op2, int) or (isinstance(op2, float))))) or(isinstance(op1, bool) and isinstance(op2, bool))):
                        if(op1 == op2):
                                opPush(True)
                        else:
                                opPush(False)
                else:
                        print("None of the options were available.")
        else:
                print("Stack is empty.")

def psOr():
        if(len(opstack) > 0):
                op2=opPop()
                op1=opPop()
                if (((isinstance(op1, int) or (isinstance(op1, float)) and
            (isinstance(op2, int) or (isinstance(op2, float))))) or
                (isinstance(op1, bool) and isinstance(op2, bool))):
                        if(((op1 == True or op1 > 0)or (op2 == True or op2 > 0))):
                                opPush(True)
                        else:
                                opPush(False)
                else:
                        print("None of the options were available.")
        else:
                print("Stack is empty")

def psNot():
        if(len(opstack) > 0):
                op1=opPop()
                if isinstance(op1, bool) or isinstance(op1, int):
                        if isinstance(op1, bool):
                                opPush(not op1)
                        else:
                                opPush(op1 - (2 *op1))
                else:
                        print("None of the options were available")
        else:
                print("Stack is empty.")

        


##### TEST ZONE #########~~~!!!!!!!!!!!1


#------- Part 1 TEST CASES--------------
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True
    
#Comparison operators tests
def testEq():
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        return False
    return True

def testLt():
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        return False
    return True

def testGt():
    opPush(3)
    opPush(6)
    gt()
    if opPop() != False:
        return False
    return True

#boolean operator tests
def testPsAnd():
    opPush(True)
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsOr():
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True:
        return False
    return True

def testPsNot():
    opPush(True)
    psNot()
    if opPop() != False:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    opPop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True


def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv), \
                 ('eq',testEq),('lt',testLt),('gt', testGt), ('psAnd', testPsAnd),('psOr', testPsOr),('psNot', testPsNot), \
                 ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('copy', testCopy), \
                 ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

if __name__ == '__main__':
    print(main_part1())
