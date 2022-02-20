from __future__ import all_feature_names


username = input("give your username: ")

def hello_world(username):
    """show your username"""""
    print("hello " + username.title() + " welcome to Functions")

hello_world(username)

## create a function
### 24 enero 2022
### add multiple inputs to the function such as dictionary


def book_description(title, author):
    """"always put a description of our function"""
    print("\n This book name is " + title.title() + ".")
    print("And it was written by " + author.title() + ".")

book_description('inferno', 'dan brown')

### Keyword arguments passed in the end of the function while calling it. 

def book_description(title, author):
    """"we are passing arguments at the execution of the function"""
    print("\n This book name is " + title.title() + ".")
    print("And it was written by " + author.title() + ".")

book_description(title= "the everything store", author="ashlee vance")



