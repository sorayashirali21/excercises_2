#pr 3

file_path = 'email-Eu-core.txt'
def calculate_degrees(file_path):
    in_degrees = {}
    out_degrees = {}
    degrees = {}

    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            out_degrees[sender] = out_degrees.get(sender, 0) + 1
            in_degrees[receiver] = in_degrees.get(receiver, 0) + 1

    for node in in_degrees:
        degrees[node] = in_degrees[node] + out_degrees.get(node, 0)

    return in_degrees, out_degrees, degrees


in_degrees, out_degrees, degrees = calculate_degrees(file_path)

for node in list(in_degrees.keys())[:5]:
    print('Result Question 3: ')
    print('Node:', node)
    print('In_degree:', in_degrees.get(node, 0))
    print('Out_degree:', out_degrees.get(node, 0))
    print('Degree:', degrees.get(node, 0))
    print()

#===============================================
'''output pr 3:

گره: 1
درجه ی ورودی: 51
درجه ی خروجی: 1
درجه : 52

گره: 3
درجه ی ورودی: 62
درجه ی خروجی: 56
درجه : 118

گره: 4
درجه ی ورودی: 74
درجه ی خروجی: 89
درجه : 163

گره: 6
درجه ی ورودی: 93
درجه ی خروجی: 109
درجه : 202

گره: 7
درجه ی ورودی: 49
درجه ی خروجی: 67
درجه: 116