def opcode1(arr,current_pos):
    pos1 = arr[current_pos+1]
    pos2 = arr[current_pos+2]
    pos3 = arr[current_pos+3]
    arr[pos3] = arr[pos1] + arr[pos2]
    #print(f'opcode1({current_pos}):{arr[current_pos+3]}')

def opcode2(arr,current_pos):
    pos1 = arr[current_pos+1]
    pos2 = arr[current_pos+2]
    pos3 = arr[current_pos+3]
    arr[pos3] = arr[pos1] * arr[pos2]
    #print(f'opcode2({current_pos}): {arr[current_pos+3]}')

def run(arr,current_pos):
    #print(f'current_pos: {current_pos}')
    current = arr[current_pos]
    if current == 1:
        opcode1(arr,current_pos)
        return run(arr,current_pos+4)
    elif current == 2:
        opcode2(arr,current_pos)
        return run(arr,current_pos+4)
    elif current == 99:
        return arr[0]

def main():
    input = ""
    filename = 'input.txt'
    with open(filename, 'r') as file:
        input = file.read().replace('\n', '')

    array = input.split(',')
    array = [ int(x) for x in array ]
    original_array = array.copy() #keep a copy of the original array
    maximum = len(array)
    goal = 19690720
    for i in range(0,maximum):
        for j in range(0,maximum):
            array[1] = i
            array[2] = j
            result = run(array,0)
            if result == goal:
                print(f'noun: {i}')
                print(f'verb: {j}')
                print(f'answer: {100*i + j}')
                return
            array = original_array.copy()
    return

if __name__ == '__main__':
    main()