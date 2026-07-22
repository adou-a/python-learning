import random

def main():
    n = get_level()
    i = 0
    count = 0
    while i < 10:
        x = generate_integer(n)
        y = generate_integer(n)
        no = 0

        while no < 3:
            try:
                print(x,'+',y,end='')
                answer = int(input(' '))
            except ValueError:
                print('EEE')
                no = no + 1
                continue
            if answer != x + y:
                print('EEE')
                no = no + 1
            else:
                i = i + 1
                count = count + 1
                break

        if no == 3:
            i = i + 1
            print(x,'+',y,x+y)

    print(count)
                
            
        



    


def get_level():
    while True:
        try:
            n = int(input('Level:'))
        except ValueError:
            continue
        if not( n == 1 or n == 2 or n ==3):
            continue

        return n






def generate_integer(level):
    if level == 1 :
        number = random.randint(1,9)
    elif level ==2 :
        number = random.randint(1,99)
    else:
        number = random.randint(1,999)
   
    return number


if __name__ =='__main__':


    main()