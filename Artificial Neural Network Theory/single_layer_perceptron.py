import random
import math
import numpy as np

#input number patterns 0~9
def input_patterns():
    data = []
    
    data.append(list(map(int,"00111100010000101000000110000001100000011000000110000001100000010100001000111100")))
    data.append(list(map(int,"00011000001110000001100000011000000110000001100000011000000110000001100000111100")))
    data.append(list(map(int,"00111100010000101000000100000010000001000000100000010000001000000100000011111111")))
    data.append(list(map(int,"00111100110000100000000100000001111111101111111000000001000000011100001000111100")))
    data.append(list(map(int,"00000100000011000001010000100100010001001111111100000100000001000000010000000100")))
    data.append(list(map(int,"11111111100000001000000010000000100000001111111000000001000000011100001000111100")))
    data.append(list(map(int,"00111100010000101000000110000000101111001100001010000001100000010100001000111100")))
    data.append(list(map(int,"11111111000000010000001000000010000001000000010000001000000010000001000000010000")))
    data.append(list(map(int,"00111100010000101000000101000010001111000011110001000010100000010100001000111100")))
    data.append(list(map(int,"00111100010000101000000101000011001111010000000100000001100000010100001000111100")))

    return data

def output_classes():
    classes = []

    classes.append([1,0,0,0,0,0,0,0,0,0])
    classes.append([0,1,0,0,0,0,0,0,0,0])
    classes.append([0,0,1,0,0,0,0,0,0,0])
    classes.append([0,0,0,1,0,0,0,0,0,0])
    classes.append([0,0,0,0,1,0,0,0,0,0])
    classes.append([0,0,0,0,0,1,0,0,0,0])
    classes.append([0,0,0,0,0,0,1,0,0,0])
    classes.append([0,0,0,0,0,0,0,1,0,0])
    classes.append([0,0,0,0,0,0,0,0,1,0])
    classes.append([0,0,0,0,0,0,0,0,0,1])

    return classes

def initalize_weights(class_num):
    return [[random.uniform(0,1) for _ in range(80)] for _ in range(class_num)]

def softmax_function(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)

    return exp_x/sum_exp_x

def single_layer_perceptron():
    learning_rate = float(input("input learning late (recommand 0.05 ~ 0.2) : "))
    repetition_num = int(input("input number of repetitions (recommand 100 ~ 1000) : "))
    number_data = input_patterns()
    classification_data = output_classes()
    weights = initalize_weights(len(number_data))

    print("learning is start!")

    for _ in range(repetition_num):
        for learning_data, output_data in zip(number_data, classification_data):
            new_weights = []
            result = []
            for weight in weights:
                result.append(sum([a * b for a, b in zip(learning_data, weight)]))
                result = list(softmax_function(result))

            for weight, real_output, desire_output in zip(weights, result, output_data):
                new_weights.append([a + learning_rate * (desire_output - real_output) * b for a, b in zip(weight, learning_data)])

            weights = new_weights
            
    print("learning is complete!")

    while(True):
        test_data = input("input 8*10 number testing data or input \"exit\" to end program :\n")

        if(test_data == "exit"):
            break

        try:
            test_data = list(map(int,test_data))
        except:
            print("worng data inputed, try again!")
            continue

        result = []
        for weight in weights:
            result.append(sum([a * b for a, b in zip(test_data, weight)]))
        print(softmax_function(result))
                
if __name__ == "__main__":
    single_layer_perceptron()
    
