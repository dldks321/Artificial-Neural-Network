#input number patterns 0~9
'''
The stronger the orthogonality between patterns,
the easier it is to recognize patterns.
so it is recommended to include fewer patterns.
'''
def input_patterns():
    data = []
    
    data.append(list(map(int,"00111100010000101000000110000001100000011000000110000001100000010100001000111100")))
    data.append(list(map(int,"00011000001110000001100000011000000110000001100000011000000110000001100000111100")))
    #data.append(list(map(int,"00111100010000101000000100000010000001000000100000010000001000000100000011111111")))
    #data.append(list(map(int,"00111100110000100000000100000001111111101111111000000001000000011100001000111100")))
    #data.append(list(map(int,"00000100000011000001010000100100010001001111111100000100000001000000010000000100")))
    #data.append(list(map(int,"11111111100000001000000010000000100000001111111000000001000000011100001000111100")))
    #data.append(list(map(int,"00111100010000101000000110000000101111001100001010000001100000010100001000111100")))
    #data.append(list(map(int,"11111111000000010000001000000010000001000000010000001000000010000001000000010000")))
    #data.append(list(map(int,"00111100010000101000000101000010001111000011110001000010100000010100001000111100")))
    #data.append(list(map(int,"00111100010000101000000101000011001111010000000100000001100000010100001000111100")))

    return data

#change data binary to bipolar
def change_bipolar(data):
    for x in range(len(data)) :
        for y in range(len(data[x])):           
            if(data[x][y] == 0):
                data[x][y] = -1

    return data

#get weights
def get_weights(data):
    weights = [[0]*80 for _ in range(80)]

    for num_data in data:
        for x in range(len(num_data)):
            for y in range(len(num_data)):
                weights[x][y] += num_data[x]*num_data[y]

    for x in range(len(weights)):
        weights[x][x] = 0

    return weights

#get thetas
def get_thetas(weights):
    thetas = []
    for w in weights:
        thetas.append((-0.5)*sum(w))

    return thetas

#starting (parallel) hopfield network model
def hopfield_network():
    print("weights and thetas calculate start.")
    
    num_pattern = change_bipolar(input_patterns())

    weights = get_weights(num_pattern)
    thetas = get_thetas(weights)


    print("calculate finished.")
    print("you can use this model.")

    while(True):
        test_data = input("input 8*10 number testing data or input \"exit\" to end program :\n")

        if(test_data == "exit"):
            break

        try:
            test_data = list(map(int,test_data))
        except:
            print("worng data inputed, try again!")
            continue

        execution_num = int(input("and input number of excutions. :"))

        for _ in range(execution_num):
            #parallel hopfield network
            next_test_data = []
            
            for i in range(len(test_data)):
                comparing_num = sum([weights[i][j]*test_data[j] for j in range(len(test_data))]) + thetas[i]
                if(comparing_num > 0):
                    next_test_data.append(1)
                elif(comparing_num < 0):
                    next_test_data.append(0)
                else:
                    next_test_data.append(test_data[i])

            test_data = next_test_data

            #nomal hopfield network
            '''
            for i in range(len(test_data)):
                comparing_num = sum([weights[i][j]*test_data[j] for j in range(len(test_data))]) + thetas[i]
                if(comparing_num > 0):
                    test_data[i] = 1
                elif(comparing_num < 0):
                    test_data[i] = 0
            '''

        print("the result is...\n")
        for x in range(len(test_data)):
            print(test_data[x],end="")
            if(x % 8 == 7):
                print("")
        print("")

        print("test is complete!\n")
            
if __name__ == "__main__":
    hopfield_network()
