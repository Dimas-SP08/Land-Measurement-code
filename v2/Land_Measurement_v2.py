'''LAND MEASUREMENT PROGRAM'''

'''Initialize variables for ASCII values, data storage, elevation difference, and point numbering'''
asci1=97 # 'a' in ASCII
asci2=98 # 'b' in ASCII
data = []
elev_difference=0
point_number1=1
point_number2=2

import os

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


def check():
    isdone = input("\nWas your input correct? (y/n): ")
    while isdone not in ('y','n'):
        print('choose y/n!')
        isdone = input("Was your input correct? (y/n): ")
    return isdone
    

'''INPUT THREAD AND CALCULATE MID THREAD'''
def calculate_mid_point(promt):
    """Function to calculate the mid thread based on top, mid, and bottom thread inputs."""
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
                    isdone = check()
                    if  isdone == 'n':
                        continue
                    return result_mid_thread
                    
                elif mid_thread != result_mid_thread:
                    print("-"*20)
                    print(f'mid thread = {top_thread} + {bottom_thread}/ 2')
                    print(f'{mid_thread} ≠ {result_mid_thread} -> invalid')
                    print('\nmid thread is not valid')
                    isdone = check()
                    if  isdone == 'n':
                        continue
                    return result_mid_thread   
                    
            else:               
                isdone = check()
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
            isdone = check()
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
from tabulate import tabulate
os.system("cls")
print("Elevation Data Result:")
print(tabulate(data, headers="keys", tablefmt="fancy_grid", floatfmt=".3f"))

'''MAKE DATAFRAME'''
import pandas as pd
final= pd.DataFrame(data)

'''SEND TO EXCEL'''
while True:
    try:
        send = input("\nDo you want to send this result to excel? (y/n) : ")
        while send not in ('y','n'):
            print('\nchoose y/n!')
            send = input("\nDo you want to send this result to excel? (y/n) : ")
        if send == 'y':
            final.to_excel('Elevation Data.xlsx',float_format='%.3f',index=False)
            print("-"*20)
            print('CONGRATULATION, THE FILE HAS BEEN DELIVERED!')
            print("-"*20)
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



'''MAKE THE GRAPHICS'''
while True:
    try:
        send2 = input("\nDo you want make the graphics of the result? (y/n) : ")
        while send2 not in ('y','n'):
            print('\nchoose y/n!')
            send2 = input("\nDo you want make the graphics of the result? (y/n) : ")
        if send2 == 'y':

            import matplotlib.pyplot as plt

            '''MAKE ELEVATION PROFILE PLOT'''
            fig1, ax = plt.subplots(dpi=100, tight_layout=True)
            ax.plot(final['POINT NUMBER'], final['ELEVATION (AMSL)'],lw=2, ls='-.')
            ax.grid(True)
            ax.set_xlabel('Point Number')
            ax.set_ylabel('Elevation (m)')
            ax.set_title('Elevation Profile')
            plt.xticks(rotation=45, ha='right')
            fig1.savefig('elevation_profile_plot.png')

            '''MAKE HEIGHT DIFFERENCE BAR PLOT'''
            fig2, ax2 = plt.subplots(dpi=100, tight_layout=True)
            ax2.bar(final['POINT NUMBER'], final['HEIGHT DIFFERENCE'], color='orange')
            ax2.set_xlabel('Point Number')
            ax2.set_ylabel('Height Difference (m)')
            ax2.set_title('Height Difference Between Points')
            plt.xticks(rotation=45, ha='right')
            fig2.savefig('height_difference_bar_plot.png')

            '''MAKE DISTANCE VS ELEVATION WITH SCATTTER PLOT'''
            fig=plt.figure(dpi=100)
            plt.scatter(final['DISTANCE (m)'], final['ELEVATION (AMSL)'])
            plt.title("Jarak vs Elevasi")
            plt.xlabel("Jarak kumulatif (m)")
            plt.ylabel("Elevasi AMSL (m)")
            plt.xticks(rotation=45, ha='right')
            plt.grid(True)
            plt.tight_layout()
            fig.savefig('elevation_scatter_plot.png')
            print("-"*20)
            print('CONGRATULATION, THE FILE HAS BEEN DELIVERED!')
            print("-"*20)
            break

        if send2 == 'n':
            break
    except:
        print("can't make the graphics!")
        try_ =input('if you want try again (y/n) :')
        while try_ not in ('y','n'):
            print("choose y/n!")
            try_ =input('if you want try again (y/n) :')
        if try_ == 'y':
            continue
        if try_ == 'n':
            break


'''ADD THE RESULT AND PLOTS TO EXCEL'''
if send2 == 'y' and send == 'y':
    while True:
        try:
            send3 = input("\nDo you want to send it's result and it's graphic to excel? (y/n) : ")
            while send3 not in ('y','n'):
                print('\nchoose y/n!')
                send3 = input("\nDo you want to send it's result and it's graphic to excel? (y/n) : ")
            if send3 == 'y':

                from openpyxl import load_workbook
                from openpyxl.drawing.image import Image

                wb = load_workbook('Elevation Data.xlsx')
                ws = wb.active

                def add_image_to_excel(no_image,image_path, cell):
                    no_image = Image(image_path)
                    ws.add_image(no_image,cell)

                add_image_to_excel('elevation_scatter_plot.png', 'elevation_scatter_plot.png', 'I2')
                add_image_to_excel('elevation_profile_plot.png', 'elevation_profile_plot.png', 'I30')
                add_image_to_excel('height_difference_bar_plot.png', 'height_difference_bar_plot.png', 'I58')
                wb.save('Elevation Data with graphic.xlsx')
                print("-"*20)
                print('CONGRATULATION, THE FILE HAS BEEN DELIVERED!')
                print("-"*20)
                print("THANKS FOR USING THIS PROGRAM!\n")
                input("Enter for last program : ")
                break
            if send3 == 'n':
                print("\nTHANKS FOR USING THIS PROGRAM!")
                break
        except:
            print("The graphics can't send to excel!")
            try_ =input('if you want try again (y/n) :')
            while try_ not in ('y','n'):
                print("choose y/n!")
                try_ =input('if you want try again (y/n) :')
            if try_ == 'y':
                continue
            if try_ == 'n':
                print("\nTHANKS FOR USING THIS PROGRAM!")
                break


