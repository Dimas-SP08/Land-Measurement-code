import os
from tabulate import tabulate
import pandas as pd

'''NEEDED VARIABLE'''
asci1=97 # 'a' in ASCII
asci2=98 # 'b' in ASCII
data = []
elev_difference=0
point_number1=1
point_number2=2

os.system("cls")
print(f"{'WELCOME TO THE PROGRAM':^20}")
print(f"{'LAND MEASUREMENT':^20}")
print("-"*20)

'''INPUT HOW MANY POINT'''
while True:
    try:
        point = int(input("How many points all there : "))
        break
    except:
        print("Must be a number!")
        continue

'''INPUT AMSL'''
while True:
    try:
        amsl = int(input("Enter AMSL (m): "))
        break
    except:
        print("Must be a number!")
        continue
elevation=amsl

'''INPUT THREAD AND CALCULATE MID THREAD'''
def calculate_mid_point(promt):
    while True:
        try:
            os.system("cls")
            print(f'Calculate {promt}')
            print("-"*20)
            top_thread = float(input(f"\nenter the top trhead, if there is'nt, enter '0' : "))                  
            mid_thread = float(input(f"enter the mid thread : "))
            bottom_thread = float(input(f"enter the bottom trhead,if there is'nt, enter '0' : "))
            
            '''validation of mid thread'''
            if top_thread != 0 and bottom_thread != 0:                       
                result_mid_thread = (top_thread + bottom_thread)/2
                if mid_thread == result_mid_thread:
                    print("-"*20)
                    print(f'mid thread = {top_thread} + {bottom_thread}/ 2')
                    print(f'{mid_thread} = {result_mid_thread} -> valid')
                    print('\nmid thread is valid')
                    isdone = input("\nWas your input correct? (y/n): ")
                    while isdone not in ('y','n'):
                        print('choose y/n!')
                        isdone = input("Was your input correct? (y/n): ")
                    if  isdone == 'n':
                        continue
                    return result_mid_thread
                    
                
                elif mid_thread != result_mid_thread:
                    print("-"*20)
                    print(f'mid thread = {top_thread} + {bottom_thread}/ 2')
                    print(f'{mid_thread} ≠ {result_mid_thread} -> invalid')
                    print('\nmid thread is not valid')
                    isdone = input("\nWas your input correct? (y/n): ")
                    while isdone not in ('y','n'):
                        print('choose y/n!')
                        isdone = input("Was your input correct? (y/n): ")
                    if  isdone == 'n':
                        continue
                    return result_mid_thread   
                    

            else:               
                isdone = input("\nWas your input correct? (y/n): ")
                while isdone not in ('y','n'):
                    print('choose y/n!')
                    isdone = input("Was your input correct? (y/n): ")
                if  isdone == 'n':
                    continue
                return mid_thread  
                
        except:
            print("\nMUST BE A NUMBER OR DECIMAL!")
            input("Enter to continue : ")
            continue
            
'''PROGRAM'''            
for _ in range(point):
    os.system("cls")
    print(f"{'WELCOME TO THE PROGRAM':^20}")
    print(f"{'LAND MEASUREMENT':^20}")
    print("-"*20)

    '''DETERMINING MID THREAD'''
    label1=    f'P{point_number1}-{chr(asci1)}'
    label2=    f'P{point_number1}-{chr(asci2)}'
    input1= calculate_mid_point(label1)
    input2= calculate_mid_point(label2)

    '''CALCULATE ELEVATION DIFFERENCE'''
    elev_difference =float(input1)-float(input2)
    
    '''INPUT DISTANCE'''
    while True:
        try:
            os.system("cls")
            distance = float(input(f"Enter distance from p{point_number1}-{chr(asci1)} to p{point_number1}-{chr(asci2)} : "))
            isdone = input("\nWas your input correct? (y/n): ")
            while isdone not in ('y','n'):
                print('choose y/n!')
                isdone = input("Was your input correct? (y/n): ")
            if isdone == 'y':
                break
            elif  isdone == 'n':
                continue
        except:
            print("Must be a number")
            input('enter for continue : ')
            continue

    '''CALCULATE ELEVATION'''
    elevation += elev_difference

    '''DETERMINING STATUS'''
    stats= 'RISE' if elev_difference >= 0 else 'FALL'

    '''RESULT CALCULATION'''
    result = {
       'POINT NUMBER':f'p{point_number1}-p{point_number2}',
       'BACKSIGHT':input1,
       'FORESIGHT':input2,
       'DISTANCE (m)':distance,
       'HEIGHT DIFFERENCE':elev_difference,
       'ELEVATION (AMSL)':elevation,
       'STATUS':stats
       }

    '''INCREMENT COUNTERS FOR NEXT POINT'''
    point_number1 += 1
    point_number2+=1
    asci1+=1
    asci2+=1 

    data.append(result)

'''SHOW RESULT'''
os.system("cls")
print("Elevation Data Result:")
print(tabulate(data, headers="keys", tablefmt="fancy_grid", floatfmt=".3f"))




'''SEND TO EXCEL'''
while True:
    try:
        send = input("\nDo you want to send this result to excel (y/n) : ")
        while send not in ('y','n'):
            print('\nchoose y/n!')
            send = input("\nDo you want to send this result to excel (y/n) : ")
        if send == 'y':
            final= pd.DataFrame(data)
            final.to_excel('Elevation Data.xlsx',float_format='%.3f',index=False)
            print('CONGRATULATION, THE FILE HAS BEEN DELIVERED!')
            input("Enter for last program : ")
            break
        if send == 'n':
            break
    except:
        print("The result can't send to excel!")
        try_ =input('if you want try again (y/n) :')
        while try_ not in ('y','n'):
            print("choose y/n!")
            try_ =input('if you want try again (y/n) :')
        if try_ == 'y':
            continue
        if try_ == 'n':
            break
        


