def main():
    #write your code below this line
    
    year = int(input("Give a year:"))
    
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print("The year is a leap year.")
#     else:
#         print("The year is not a leap year.")

    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            leap = False
        leap = True
        
    if leap:
        print('The year is a leap year.')
    else:
        print('The year is not a leap year.')
                
        
if __name__ == '__main__':
    main()
