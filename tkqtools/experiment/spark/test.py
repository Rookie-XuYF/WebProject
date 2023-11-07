input_file = "/home/nukeexplode/Desktop/tkqtools/test.txt"
output_file = "/home/nukeexplode/Desktop/tkqtools/output.txt"
with open(input_file, 'r', encoding='UTF-8') as fr:
    lines = fr.readlines()
    for line in lines:
        print(line.split('\t'))