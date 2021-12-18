INPUT = "inputs/input16.txt"
VERSIONS_SUM = 0
BITS = ''

def add_to_version(add_ver):
    global VERSIONS_SUM
    VERSIONS_SUM += add_ver
    return VERSIONS_SUM

def initialize_bits():
    global BITS
    hex = open(INPUT).readline().strip()
    hex_len = len(hex)*4
    BITS = bin(int(hex, 16))[2:].rjust(hex_len, '0')
    return BITS

def has_BITS_left() -> bool:
    return int(BITS, 2) != 0

def trim_bits(new_start):
    global BITS
    BITS = BITS[new_start:]
    return BITS

def compute_values(type_id: int, values: [int]) -> int:
    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        product = 1
        for value in values:
            product *= value
        return product
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)
    elif type_id == 5:
        return 1 if values[0] > values[1] else 0
    elif type_id == 6:
        return 1 if values[0] < values[1] else 0
    elif type_id == 7:
        return 1 if values[0] == values[1] else 0

def decode_operator_0(type_id: int) -> int: #length of bits of subpackets
    bits_to_process = int(BITS[:15], 2)
    trim_bits(15)
    bits_length_at_start = len(BITS)
    values = []
    while bits_length_at_start - len(BITS) < bits_to_process and has_BITS_left():
        values.append(decode())
    return compute_values(type_id, values)

def decode_operator_1(type_id: int) -> int: #number of subpackets
    num_subpackets = int(BITS[:11], 2)
    trim_bits(11)
    values = []
    for packet in range(num_subpackets):
        if not has_BITS_left():
            return
        values.append(decode())
    return compute_values(type_id, values)

def decode_operator(type_id: int) -> int:
    length_type_id = BITS[0]
    trim_bits(1)
    if length_type_id == '0':
        return decode_operator_0(type_id)
    else:
        return decode_operator_1(type_id)

def decode_type4() -> int:
    literal_val = ''
    group = BITS[:5]
    trim_bits(5)
    while True:
        literal_val += group[1:]
        # all 5-bit groups of the literal start with a 1
        # except the last group
        if group[0] == '0':
            break
        else:
            group = BITS[:5]
            trim_bits(5)
    return int(literal_val, 2)

def decode() -> int:
    type_id = decode_verAndTypeID()
    if type_id == 4:
        return decode_type4()
    else:
        return decode_operator(type_id)

def decode_verAndTypeID() -> int:
    add_to_version(int(BITS[:3], 2))
    type_id = int(BITS[3:6], 2)
    trim_bits(6)
    return type_id

if __name__ == '__main__':
    initialize_bits()
    final_value = decode()

    print(f'part 1: {VERSIONS_SUM}') #1002
    print(f'part 2: {final_value}') #1673210814091