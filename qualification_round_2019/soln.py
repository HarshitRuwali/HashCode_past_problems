from sys import argv

max_vert = 1000
max_all = 1000

with open(cur_dir+'.txt', 'r') as f_in:
    photo_count = int(f_in.readline())
    all = []
    vert = []
    i = 0
    for i in range(photo_count):
        photo = f_in.readline().rstrip().split(" ")
        if photo[0] == "H":
            all.append([int(photo[1]), [x for x in photo[2:]], (i,)])
        else:
            vert.append([int(photo[1]), [x for x in photo[2:]], (i,)])
        i += 1
f_in.close()

#print(all)
#print(vert)


#vert = []


while len(vert) > 1:
    max_tags, id = 0, 0
    for i in range(1, min(max_vert, len(vert))):
        union = list(set(vert[0][1]+vert[id][1]))
        num_tags = len(union)
        if num_tags > max_tags:
            max_tags = num_tags
            id = i
    all.append([max_tags, union, (vert[0][2][0], vert[id][2][0])])
    vert.pop(id)
    vert.pop(0)

#print(all)

def score(id0, id1):
    x = len(set(all[id0][1]) & set(all[id1][1]))
    y = len(set(all[id0][1]) - set(all[id1][1]))
    z = len(set(all[id1][1]) - set(all[id0][1]))
    return min(x, y, z)

def write_out(id):
    if len(all[id][2]) == 1:
        f_out.write('%d\n' % (all[id][2][0]))
    else:
        f_out.write('%d %d\n' % (all[id][2][0], all[id][2][1]))

#f_out = open(str(argv[1])+'.out', 'w+')
#f_out.write(str(len(all))+'\n')

write_out(0)

counter = 0
for i in range(1,len(all)-1): #len(all)-2 times
    max_score, id = 0, 1
    for i in range(1, min(max_all, len(all))):
        curr_score = score(0, i)
        if curr_score > max_score:
            max_score = curr_score
            id = i
    write_out(id)
    counter += 1
    if counter % 10000 == 0:
        print(counter)
    all[0], all[id] = all[id], all[0]
    all.pop(id)

#print(all)
write_out(1)

f_out.close()

def process(fileName):

    print("######")
    print(fileName)
    print("######")

    inputFile = open(fileName + ".txt", "rt")

    #  Reading file
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()

    print("INPUT")
    print(firstLine)
    print(secondLine)

    #  Assigning parameters
    MAX, NUM = list(map(int, firstLine.split()))

    #  Creating the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))

    outputList = solve(MAX, inputList)
       
    print("")
    print("OUTPUT")
    print(len(outputList))

    outputString = ""
    for l in outputList:
        outputString = outputString + str(l) + " "
    print(outputString)

    #os.mkdir(outputFile) 
    outputFilesDirectory = "Output/"

    outputFile = open(outputFilesDirectory + fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()

    inputFilesDirectory = "Input/"  
   

fileNames = ["a_example", "b_lovely_landscapes", "c_memorable_moments",
             "d_pet_pictures", "e_shiny_selfies"]  

for fileName in fileNames:  
    process(fileName)
