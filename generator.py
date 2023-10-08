import random
import os


def random_():
    list_of_alpha = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"

    star_length = 1 # integer for "for loop" , Feel free to modify it
    end_length = 12  # integer for "for loop" , Feel free to modify it

    for _ in range(star_length, end_length): # Length of pass
        with open('pass.txt', 'a') as f:
            f.writelines(random.choice(list_of_alpha))
        with open('pass.txt','r') as file:
            p = file.read()
    sym = "#@$&"
    
    p = f'{random.choice(sym)}{random.choice(sym)}{p}{random.choice(sym)}{random.choice(sym)}'


    os.remove('pass.txt')
    return p



# if __name__ == '__main__':
#     random_()
    
    
    


    

    
    
    

