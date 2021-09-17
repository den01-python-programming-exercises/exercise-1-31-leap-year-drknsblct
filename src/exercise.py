def main():
    #write your code below this line
    
    year = int(input("Give a year:"))
    leap_year = False
 
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
    elif year % 4 == 0:
        leap_year = True

    if leap_year:
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")

if __name__ == '__main__':
    main()
