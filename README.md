# Binary-Search-Trees
CISC 121 Assignment #4

This is a Python version 3.6 of the Binary Search Trees Assignment.
This program simulates grades in a Binary Search Tree.  
It reads in class data, adds grades, find averages,count number of 
students which failed the exam, and look up specific students.

Assignment:
"You may begin this assignment with the sample BST code.

A Binary Search Tree is a data structure that provides us with a way to organize and store data for use in a program.  It is used when you need a structure that provides you efficiency for adding new information (O(log n) time to add a new node) and for searching for data (O(log n) time to search for information).   

Use a binary search tree to store information about student marks for CISC 525 (a fake course, fake marks).  You can find the data at http://www.cs.queensu.ca/home/cords2/marks.txt.   You will read this data from the web page in the same way that you did for the linked list assignment.   Read a line of the data, create a node, and add this node to your binary search tree.  Each line of data contains the following (student number, assign 1 mark/25, assign 2 mark/25, assign 3 mark/15, assign 4 mark/20, assign 5 mark/20, midterm mark/35, final exam mark/65).    

Create a user interface (text only) that will provide the following functionality:

1) add a new node to the tree (manually input the student number and all the marks).

2) find the average of any one of the marks (prompt the user for which mark to find the average of).

3) count the number of students who got less than 50% on the final exam.

4) look up the marks for a particular student (prompt the user for a student number and, if that student is found, print their marks.  If the student is not found, print "Student does not exist")."
