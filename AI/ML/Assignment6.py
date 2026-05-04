data = True
word = 'This'

with open("/Users/saurabhvalunjkar/Python/PythonProgramming/AI/ML/sample.txt","r") as f:
    line=1
    while data:
        data=f.readline()
        if(word in data):
            print(f"{word} found at line {line} !!")
            break
        line+=1

