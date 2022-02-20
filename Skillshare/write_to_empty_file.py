## 14 de febrero 2022
## how to write files in python or write IN files n python

## first you need to activate the write function inside the calling

filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("Hi this is Alfredo writing on a file using python")


## then i read the file to see if the text was written in the file. 
with open(filename) as file_object:
    content = file_object.read()
    print(content)


## now we will write a new line to have separated lines added to the file. 

 s