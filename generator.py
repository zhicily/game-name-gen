from names import nameGen

if __name__ == '__main__':
    f = open('names.txt', 'w')

    for i in range(1, 5001):
        name = nameGen()
        # name = nameGen(numbers=True)

        f.write(name + '\n') 
    
    f.close()