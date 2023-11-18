# TO be able to add stuff that i wanna do tomorrow or today or later in a while 
number_of_stuff = input("How many items you have to do later or tomorrow?\n--> ")
def number_of_stuff_want_to_do():

    ls =  []

    for _ in range(0, int(number_of_stuff)):

        ls = ls + [input("What would you like to add?\n--> ")]

    return ls

if __name__ == '__main__':
    
    with open('To do list.txt', 'w') as f:
        
        for i in number_of_stuff_want_to_do():
            f.write(f'{i}\n')