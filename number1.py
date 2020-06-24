repeat = 901

def m(i):
    data = 0;
    list = []

    for k in range(1, i + 1):
        data += (-1)**(k+1) / (2 *k - 1)
        list.append(data * 4)

    return list

m_data = m(repeat)

print("i\t\tm(i)")
for i in range(repeat):
    if i % 100 == 0:
        print(str(i + 1) + "\t\t" + str(round(m_data[i], 4)))
