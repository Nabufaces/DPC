f = open('./dataSet/D31.txt', 'r')
f_ = open('./dataSet/D31_.txt', 'w+')

lines = f.readlines()

for line in lines:
    item = line.split(',')
    f_.write(item[0] + '\t' + item[1] + '\n')

f.close()
f_.close()