"""
Bo Chen (10190141)
CISC 121 Assignment #4: Binary Search Trees
August 12, 2017

This is a Python version 3.6 of the Binary Search Trees Assignment.
This program simulates grades in a Binary Search Tree.  
It reads in class data, adds grades, find averages,count number of 
students which failed the exam, and look up specific students.
Detailed explination can be found here: https://goo.gl/QEvQWk
"""
import urllib.request     

"""
The add() function adds a value to a BST and returns a pointer to the 
modified BST. This function is from Professor Powley:
https://onq.queensu.ca/d2l/le/content/94519/viewContent/805358/View 
"""
def add(tree, value):
    if tree == None: 
        return {'data':value, 'left':None, 'right':None}
    elif value < tree['data']:
        tree['left'] = add(tree['left'],value)
        return tree
    elif value > tree['data']:
        tree['right'] = add(tree['right'],value)
        return tree
    else: # value == tree['data']
        return tree # ignore duplicate
    return tree

"""
The readClass() function reads in students information from marks.txt (online) into 
a binary search tree. The function strips all '\n' and splits at all ','.
readClass takes a binary search tree, and retunrs a modified binary search tree  
"""
def readClass(myTree):
    response = urllib.request.urlopen("http://www.cs.queensu.ca/home/cords2/marks.txt")
    for line in response:
        job = line.decode('utf-8').strip('\n').split(",")
        job = list(map(float, job))
        myTree = add(myTree, job)
    return myTree

"""
The count() function counts the number of nodes in a binary search tree. 
(this is later used to determine the average)
count() takes a binary search tree and return a integer. 
"""
def count(tree):
    if tree is None:
        return 0
    n = (1) + (count(tree['left'])) + (count(tree['right']))
    return (n)
        
"""
The total() function sums up the marks of a specific assignment(assesment). 
(this is later used to determine the average)
total() takes a binary search tree and a specific assesment and returns a integer.
"""
def total(tree, assesment):
    if tree is None:
        return 0
    n = (tree['data'][assesment]) + (total(tree['left'],assesment)) + (total(tree['right'],assesment))
    return (n)

"""
The failedExam() function counts the number of students which failed (<32.5) the final exam.
failedExam() takes a binary search tree and returns a integer.
"""
def failedExam(tree):
    n = 0
    if tree is None:
        return 0
    elif tree['data'][7] < 32.5:
        n = 1 + (failedExam(tree['left'])) + (failedExam(tree['right']))
        return n
    else:
        n = (failedExam(tree['left'])) + (failedExam(tree['right']))
        return n

"""
The search() function finds a specific student and displays their grades.
search() takes a binary search tree and integer and prints the student's grades .
"""
def search(tree, value, myTree):
    if tree is None:
        print ("Student does not exist")
        userInterface(myTree) 
    if tree['data'][0] == value:
        print ("   Marks for student number:",tree['data'][0],
            "\n     Assignment 1:", tree['data'][1],
            "\n     Assignment 2:", tree['data'][2],
            "\n     Assignment 3:", tree['data'][3],
            "\n     Assignment 4:", tree['data'][4],
            "\n     Assignment 5:", tree['data'][5],
            "\n     Midterm:", tree['data'][6],
            "\n     Final Exam:", tree['data'][7])
        userInterface(myTree)
    if tree['data'][0] < value:
        search(tree['right'], value, myTree)
    if tree['data'][0] > value:
        search(tree['left'], value, myTree)

"""
The userInterface() function provides the user with a text based interface.
It takes user input, verifies if it is valid, and runs approperate functions based on the input.
"""
def userInterface(myTree):
    print('\n' * 5)
    print("CISC 525 Marks")
    try:
        function = int(input("""
What would you like to do? 

    1. Add new student profile.
    2. Find the average of a mark.
    3. Find the number of students which recieved less than 50% on the exam.
    4. Find a specific student's profile.
    5. Exit 
        
    Please enter 1, 2, 3, 4, or 5.\n"""))
    except:
        print('\n' * 50)
        print(" --- Please enter a valid option --- \n")
        userInterface(myTree)
    if function < 1 or function > 5:
        print('\n' * 50)
        print(" --- Please enter a valid option --- \n")
        userInterface(myTree)
    # Question 1) add a new node to the tree.
    elif function == 1:
        print("Selected: Add new student profile.\n")
        try:
            s = float(input("   Please enter the student number: "))
            a1 = float(input("  Please enter the mark for assignment 1: "))
            a2 = float(input("  Please enter the mark for assignment 2: "))
            a3 = float(input("  Please enter the mark for assignment 3: "))
            a4 = float(input("  Please enter the mark for assignment 4: "))
            a5 = float(input("  Please enter the mark for assignment 5: "))
            m = float(input("  Please enter the mark for the midterm: "))
            f = float(input("  Please enter the mark for the final exam: "))
        except:
            print('\n' * 50)
            print(" --- Please enter a valid number --- \n")
            userInterface(myTree)
        myTree = add(myTree, [s,a1,a2,a3,a4,a5,m,f])
        print("Profile for student number", s,"sucessfully created")
        userInterface(myTree)
    # Question 2) find the average of any one of the marks.    
    elif function == 2:
        print("Selected: Find the average of a mark.\n")
        try:
            assesment = int(input("""
    Which average would you like to see?: 
        1. Assignment 1
        2. Assignment 2
        3. Assignment 3
        4. Assignment 4
        5. Assignment 5
        6. Midterm
        7. Final Exam
        Please enter 1, 2, 3, 4, 5, 6, or 7.\n"""))
        except:
            print('\n' * 50)
            print(" --- Please enter a valid number --- \n")
            userInterface(myTree)
        if assesment < 1 or assesment > 7:
            print('\n' * 50)
            print(" --- Please enter a valid option --- \n")
            userInterface(myTree)
        else:
            print ("The average is {:0.2f} marks\n".format(total(myTree,assesment)/count(myTree)))
            userInterface(myTree)
    # Question 3) count the number of students who got less than 50% on the final exam.
    elif function == 3:
        print("Selected: Find the number of students which recieved less than 50% on the exam.\n")
        print ("There are:",failedExam(myTree),"student(s) which failed the final exam.\n")
        userInterface(myTree)
    # Question 4) look up the marks for a particular student.
    elif function == 4:
        print ("Selected: Find a specific student's profile.\n")
        try:
            num = float(input("   Please enter the student number: "))
        except:
            print('\n' * 50)
            print(" --- Please enter a valid number --- \n")
            userInterface(myTree)
        search(myTree, num, myTree)
    #Exit
    elif function == 5:
        print ("Good Bye")
        quit()

"""
The main() fuction initates the program. 
"""
def main():
    myTree = None  #create an empty tree
    myTree = readClass(myTree) #reads in CISC 525
    userInterface(myTree) 
main()