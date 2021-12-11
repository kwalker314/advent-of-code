import os
from datetime import date

if __name__ == '__main__':
    runall = True
    if runall:
        for filename in os.listdir():
            if filename != "main.py" and filename.endswith('.py'):
                print(f'============={filename}=============')
                exec(open(filename).read())
    else:
        day = date.today().strftime('%d')
        day = "11"
        filename = "day" + day + ".py"
        exec(open(filename).read())
