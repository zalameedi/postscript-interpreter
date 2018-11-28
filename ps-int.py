# Zeid Al-Ameedi
# 10-25-2018
# HWK4 Part 1 is meant to mimic the ghost interpreter (postscript) style
# For details on each function please see attached file containing requirements in the repository

# HWK4 Part 2 is meant to implement additional ghost script features to be specific 
# parsing, if, ifelse, for, forall, interpreter and  testcases following each of them
import re #Given as help code. module

opstack = [] #operand stack
dictstack = [] #dictionary stack

psFunctions = ['def', 'push', 'pop', 'add', 'sub', 'mul', 'div', 'eq', 'gt', 'lt',
                'length', 'get', 'and', 'or', 'not', 'dup', 'exch', 'copy', 'clear',
                'stack', 'dict', 'begin', 'end', 'if', 'ifelse', 'for', 'forall']

#operand's methods first

#Pops a value off the operand stack and returns the number
def opPop():
    try:
        return opstack.pop()
    except:
        return
       # print("Operand stack is empty.")

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

#Each function does the corresponding action that it is named after
#Before being pushed back onto the stack (The Answer)

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

#Exchanges multiple values in their spots within the stack
def exch():
        if(len(opstack) > 1):
                temp1 = opPop()
                temp2 = opPop()
                opPush(temp1)
                opPush(temp2)
        else:
                print("Stack doesn't have enough values")

# duplicates the last item on the stack and pushes it back on
def dup():
        if(len(opstack) > 0):
                temp1 = opPop()
                opPush(temp1)
                opPush(temp1)
        else:
                print("Stack doesn't have enough values")

#Completely just deletes all entries from the stack, points new reference to a empty stack
def clear():
    opstack[:] = [] #Courtesy of stackoverflow 
    

#Misc functions I missed

#Copies and appends back onto a list
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

# Returns a certain position within a list
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
        
#Returns the length of the list popped out of the stack
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

#Dictionary operations, pops a dict then pushes an empty one
def psDict():
        if len(opstack) > 0:
                opPop()
                opPush({})
        else:
                print("Stack is empty.")
#puts the dict out of opstack and into the dictstack
def begin():
        myDict = {}
        if len(opstack) > 0:
                myDict = opPop()
                dictPush(myDict)
        else:
                print("Stack is empty")
#ends a dictionaries recent entry on the dictstack
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

#PART 2 SHALL BEGIN HERE

def psIf():
        if(len(opstack) > 1):
                fn = opPop()
                bVar = opPop()
                if isinstance(bVar, bool):
                        if bVar == True:
                                interpretSPS(fn)
                        else:
                                pass
                               # print("The operation will not be continued")
                else:
                        print("Error, value is not eligible for operation")
                        opPush(bVar)
                        opPush(fn)
        else:
                print("Stack doesn't have enough values.")
def psIfElse():
        if (len(opstack) > 1):
                elseStatement = opPop()
                ifStatement = opPop()
                bVar = opPop()
                if isinstance(bVar, bool):
                        if(bVar == True):
                                interpretSPS(ifStatement)
                        else:
                                interpretSPS(elseStatement)
                else:
                        print("Operations not consistent with If-Else format")
                        opPush(bVar)
                        opPush(ifStatement)
                        opPush(elseStatement)
        else:
                print("Stack doesn't have enough values.")
#ERROR will reverse engineer to rewrite
# def psFor():
#         if (len(opstack) > 2):
#                 exe = opPop() 
#                 end = opPop() 
#                 increment = opPop()
#                 initial = opPop()

#                 if initial < 0:
#                         print("Error. for loop cannot work given arguments")
#                         return False
#                 if initial > end:
#                         print("Error. for loop cannot work given arguments")
#                         return False 
#                 for i in range(4):
#                         opPop()
#                 if initial < end:
#                         while initial <= end:
#                                 opPush(initial)
#                                 interpretSPS(exe)
#                                 initial += increment
#                 elif initial == end:
#                         opPush(initial)
#                         interpretSPS(exe)
#                 else:
#                         while initial >= end:
#                                 opPush(initial)
#                                 interpretSPS(exe)
#                                 initial += increment
#                 return 

def psFor():
    exe = opPop()
    end = opPop()
    increment = opPop()
    initial = opPop()
    if initial < end:
        while initial <= end:
            opPush(initial)
            interpretSPS(exe)
            initial += increment
    elif initial == end:
        opPush(initial)
        interpretSPS(exe)
    else:
        while initial >= end:
            opPush(initial)
            interpretSPS(exe)
            initial += increment
    return

def forAll():
        #if (len(opstack) > 1):
        exe = opPop()
        arr = opPop()
        temp1 = opPop()
        temp2 = opPop()
        for index in arr:
                opPush(index)
                interpretSPS(exe)


# def forAll():

#     global opstack


#     code = opstack[-1]
#     arrayBlock = opstack[-2]

#     temp1 = opPop()
#     temp2 = opPop()

#     for i in arrayBlock:
#         opPush(i)
#         interpretSPS(code)



def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


def isInt(n): #Courtesy of https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
        try:
                int(n)
                return True
        except ValueError:
                return False
        # num = int(n)
        # if type(num) is int:
        #         return True
        # else:
        #         return False
def parseHelper(tokens):
        res=[]
        index = 0 # To keep track of each variable that demands typecast
        # it = iter(tokens)
        for i in tokens:
                if "." in i and isInt(i):
                        tokens[index] = float(tokens[index]) #Typecasted
                elif isInt(i):
                        tokens[index] = int(tokens[index])
                elif i[0] == "[": #Integer list only in str format
                        #Delete brackets so we don't make a 2D array then -> typecast to list
                        myLst = i.strip("[")
                        myLst = myLst.strip("]")

                        myLst2 = myLst.split(" ") #Extract every variable
                        for temp in myLst2:
                                if isInt(temp):
                                        res.append(int(temp))
                        tokens[index] = res
                index = index+1
        
        return tokens

def parse(tokens):
        res = parseHelper(tokens)
        tokenLst = []
        index = 0
        it = iter(res)

        for c in it:
                if c == '{':
                        temp = groupMatching(it)
                        tokenLst.append(temp)
                else:
                        tokenLst.append(c)
        return tokenLst
               
                
def groupMatching(it):
        res = []
        for c in it:
                if c == '}':
                        return res
                elif c == '{':
                        res.append(groupMatching(it))
                else:
                        res.append(c)
        return False

# def groupMatching2(it): #renamed to parse
#         res = []
#         for c in it:
#                 if c == '}':
#                         return res
#                 elif c == '{':
#                         res.append(groupMatching2(it))
#                 else:
#                         res.append(c)
#         return False

def group(s):
        res = []
        it = iter(s)
        for c in it:
                if c=='}':
                        return False
                else:
                        res.append(groupMatching(it))
        return res

def group2(L):
        res = []
        it = iter(L)
        for c in it:
                if c=='}':
                        return False
                elif c =='{':
                        res.append(groupMatching2(it))
                else:
                        res.append(c)
        return res


def psFunctionCall(var):
        if var == 'def':
                psDef()
        elif var == 'push':
                opPush()
        elif var == 'pop':
                opPop()
        elif var == 'add':
                add()
        elif var == 'sub':
                sub()
        elif var == 'mul':
                mul()
        elif var == 'div':
                div()
        elif var == 'eq':
                eq()
        elif var == 'gt':
                gt()
        elif var == 'lt':
                lt()
        elif var == 'length':
                length()
        elif var == 'get':
                get()
        elif var == 'and':
                psAnd()
        elif var == 'or':
                psOr()
        elif var == 'not':
                psNot()
        elif var == 'dup':
                dup()
        elif var == 'exch':
                exch()
        elif var == 'copy':
                copy()
        elif var == 'clear':
                clear()
        elif var == 'stack':
                stack()
        elif var == 'dict':
                psDict()
        elif var == 'begin':
                begin()
        elif var == 'end':
                end()
        elif var == 'if':
                psIf()
        elif var == 'ifelse':
                psIfElse()
        elif var == 'forall' or var == 'Forall' or var == 'forAll':
                forAll()
        elif var == 'for' or var == 'For':
                psFor()
        elif var == 'stack':
                stack()
        else:
                print("Not a function. Shouldn't really be touched.")

testcase5 = """
     1 2 3
     2 copy
     2 /x exch def
     div
     x
     add
     3 mul /y exch def
     pop
     y
     stack
    """
def interpretSPS(code): # code is a code array
        for var in code:
                if isinstance(var, int) or isinstance(var, bool) or isinstance(var, float):
                        opPush(var) #If it's a bool or int just push it onto our stack
                #Now if it's a string we have to check if it's a variable/string/function
                # elif var[0] == "/":
                #         opPush(var)
                
                elif isinstance(var, str):
                        if(var[0] == '/') or (var[0] == '('):
                                opPush(var)
                        # elif(var[0] == '('):
                        #         opPush(var)
                        elif var in psFunctions:
                                psFunctionCall(var)
                        elif var[0] == '[':
                                myLst = list(var)
                                opPush(myLst)
                        else:
                                psVar = lookup(var)
                                if ((isinstance(psVar, int)) or (isinstance(psVar, bool)) or (isinstance(psVar, float))):
                                        opPush(psVar)
                                elif isinstance(psVar, list):
                                        interpretSPS(psVar)
                elif (isinstance, list):
                        opPush(var)
                else:
                        print("Post script could not identify the variable")
                                                        
def interpreter(s): # s is a string

        tokens = parse(tokenize(s))
        interpretSPS(parse(tokenize(s))) 



##### TEST ZONE #########~~~!!!!!!!!!!!1

def test_parse():
        print("\n")
        test = ['/x', ['dup', 'add'], 'def', 21, 'x', 'exch', 'add']
        test2 = parse(tokenize("/x {dup add} def 21 x exch add"))
        if test2 == test:
                print("test_parse [1] success.")
        else:
                print(False)
        test = ['/x', 21, 12, 'gt', ['add'], ['sub'], 'if']
        test2 = parse(tokenize("""/x 21 12 gt {add} {sub} if"""))
        if test2 == test:
                print("test_parse [2] success.")
        else:
                print(False)
        test=[1, 2, 3, 4, ['add'], 'for']
        test2=parse(tokenize("""1 2 3 4 {add} for"""))
        if test == test2:
                print("test_parse [3] success.")
        else:
                print(False)
        
        
        print("\n")
def testpsFor():
        clear() 
        interpreter("1 1 10 {1 add}")
        expected = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        psFor()

        #Test Case 1
        if opstack == expected:
                print("PsFor() Test [1] success.")
        else:
                print(False)
        
        #Test Case 2
        clear()
        interpreter("1 1 5 {2 mul}")
        expected = [2, 4 , 6, 8, 10]
        psFor()
        if opstack == expected:
                print("PsFor() Test [2] success.")
        else:
                print(False)

        #Test Case 3
        clear()
        interpreter("1 1 5 {2 div}")
        expected = [.5, 1 , 1.5, 2, 2.5]
        psFor()
        if opstack != expected:
                print("PsFor() Test [3] success.")
        else:
                print(False)

def testpsIf():
        print("\n")
        clear()
        interpreter("""/var1 10 def 10 var1 eq { 10 var1 add } if """)
        expected=[20]
        if opstack == expected:
                print("PsIf() Test [1] success")
        else:
                print(False)
        
        #Test 2
        clear()
        interpreter("""/x 21 def 10 x lt {2 x mul} if""")
        expected=[42]
        if opstack == expected:
                print("PsIf() Test [2] success")
        else:
                print(False)
        
        #Test 3
        clear()
        interpreter("""/x 100 def 1337 x gt { pop } if""")
        if (opstack == []):
                print("PsIf() Test [3] success")
        else:
                print(False)

def testpsIfelse():
        print("\n")
        clear()
        interpreter("""/x 100 def 1337 x gt {2 x mul} {2 x div} ifelse""")
        expected = [200]
        if (opstack == expected):
                print("PsIfelse() Test [1] success")
        else:
                print(False)
        
        clear()
        interpreter("""/x 100 def 1337 x lt {2 x mul} {1000 x div} ifelse""")
        expected = [10]
        if (opstack == expected):
                print("PsIfelse() Test [2] success")
        else:
                print(False)
        
        clear()
        interpreter("""/x 100 def 100 x eq {1 x add} {2 x div} ifelse""")
        expected = [101]
        if (opstack == expected):
                print("PsIfelse() Test [3] success")
        else:
                print(False)


def testpsForAll():
        clear()
        expected = [101, 65]
        interpreter("""[ 10 101 65 42 20] {dup 50 lt {pop} if} forall""")
        if (opstack == expected):
                print("testpsForAll [1] success.")
        else:
                print(False)
        

        clear()
        expected = [2, 4, 6, 8, 10]
        interpreter(""" [1 2 3 4 5] {dup 0 gt {2 mul} if} forall""")
        if opstack == expected:
                print("testpsForAll [2] success.")
        
        clear()
        
        interpreter("""[1 2 3 4 5] {dup 3 eq {pop} if} forall""")
        expected = [1, 2, 4, 5]
        if (opstack == expected):
                print("testpsForAll [3] success.")
        else:
                print(False)
        

def testinterpreter():
        print("\n")
        clear()
        expected = [2, 3, 4]
        interpreter(""""1 1 3 {1 add} for """)
        if opstack == expected:
                print("Interpreter [1] success.")
        else:
                print(False)
        clear()
        expected = [2, 4, 6]
        interpreter(""""1 1 3 {2 mul} for """)
        if opstack == expected:
                print("Interpreter [2] success.")
        else:
                print(False)
        
        clear()
        expected = [30]
        interpreter(""""10 20 add""")
        if opstack == expected:
                print("Interpreter [3] success.")
        else:
                print(False)






def main_part1():
       print("Initating Part 2 Tests.\n\n")
       test_parse()
       testpsFor()
       testpsIf()
       testpsIfelse()
       testpsForAll()
       testinterpreter()
       print("Post script program complete.")
       


def main_part2():
    testcase1 = """
    /fact{
    0 dict
            begin
                    /n exch def
                    1
                    n -1 1 {mul} for
            end
    } def
    7
    fact
    stack
    """
    #[5040]

    testcase2 = """
    /n 6 def
    /fact {
         0 dict begin
            /n exch def
            n 2 lt { 1} {n 1 sub fact n mul } ifelse
         end } def
         n fact stack
    """
    #[720]

    testcase3 = """
     /sum { -1 1 {pop  add} for} def
     0
     [5 4 3 2 1] {2 mul} forall
     6 1 sub
     sum
     stack
    """
    #[30]

    testcase4 = """
     /comp { /x exch def /y exch def x y lt {y} {x} ifelse } def
     3 4 1 2 5  5 -1 2 {pop comp} for
     stack
    """
    #[5]

    testcase5 = """
     1 2 3
     2 copy
     2 /x exch def
     div
     x
     add
     3 mul /y exch def
     pop
     y
     stack
    """
    #[1, 2, 8.0]

    testcase6 = """
    /x 1 def
    /y 2 def
    /x 10 def
    /y 20 def
    0 x 1 y {add} for
    stack
    """
    #[165]

    testcase7 = """
    /x 1 def
    /y 2 def
    1 dict begin
    /x 10 def
    /y 20 def
    x y
    end
    x y
    stack
    """
    #[10, 20, 1, 2]

    testcase8 = """
    /x 1 def
    /y 2 def
    1 dict begin
    /x 10 def
    1 dict begin /y 3 def x y end
    /y 20 def
    x y
    end
    x y
    stack
    """
    #[10, 3, 10, 20, 1, 2]

    testcase9 = """
        /add2 {/add1 { 1 add} def add1 add1} def
        /add3 {add2 add1} def
        /add4 {add2 add2} def
        0 add4 add3 add2 add1
        stack
        """
    #10

    testcase10 = """
    /main {/sum { /sq {dup mul} def 1 5 {sq add} for} def 0 0 sum} def
    main
    stack
    """
    #55

    #------call interpret functions------
    print("----Test Case 1----")
    interpreter(testcase1)
    # output should print [5040]
    clear()  # clear the stack for next test case

    print("----Test Case 2----")
    interpreter(testcase2)
    # output should be  [720]
    clear()  # clear the stack for next test case

    print("----Test Case 3----")
    interpreter(testcase3)
    # output should be  [30]
    clear()  # clear the stack for next test case

    print("----Test Case 4----")
    interpreter(testcase4)
    # output should be [5]
    clear()  # clear the stack for next test case

    print("----Test Case 5----")
    interpreter(testcase5)
    # output should be [1, 2, 8.0]
    clear()  # clear the stack for next test case

    print("----Test Case 6----")
    interpreter(testcase6)
    # output should be [165]
    clear()  # clear the stack for next test case

    print("----Test Case 7----")
    interpreter(testcase7)
    # output should be [10, 20, 1, 2]
    clear()  # clear the stack for next test case

    print("----Test Case 8----")
    interpreter(testcase8)
    # output should be [10, 3, 10, 20, 1, 2]
    clear()  # clear the stack for next test case

    print("----Test Case 9----")
    interpreter(testcase9)
    # output should be [10]
    clear()  # clear the stack for next test case

    print("----Test Case 10----")
    interpreter(testcase10)
    # output should be [55]
    clear()  # clear the stack for next test case

    print("\n\n")

if __name__ == '__main__':
    main_part2()


     




if __name__ == '__main__':

    main_part2()
    #main_part1()