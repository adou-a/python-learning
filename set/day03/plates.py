def main():
    plate = input('plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
#字符串长度
    if not (2 <= len(s) <=6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    #6个字符只能是字母和数字
    for le in s:
        if not (le.isalpha() or le.isdigit()):
            return False
    number_start = False
    for le in s:
        if le.isdigit():
            if not number_start and le =='0':
                return False
            number_start = True
        elif le.isalpha(): 
            if number_start:
                return False




    
    return True

main()                  


