from tabulate import tabulate
import pandas as pd

from .Survey_controler import Survey_CTRL 
from .Survey_point import Survey_Point 
from .utils import clear_screen,input_yes_no 
from .excel_tools import to_excel,graphic_to_excel
from .graphic_tools import make_graphic
from .csv_backup import export_to_csv


class Survey_CLI:
    '''command line interface for the Land Measurement application'''

    def __init__(self):
        '''Initialize the CLI with new SurveyControler'''
        self.ctrl = Survey_CTRL()

    def run(self):
        '''Run the main survey loop'''
        point = self.input_number("How many points all there : ",int)
        amsl = self.input_number("Enter AMSL (m): ",float)
        self.ctrl.set_initial(amsl,point)
        initial_elev = amsl

        for _ in range(point):
            clear_screen()
            self.header()

            label,label1,label2 = self.ctrl.add_point()
            input1 = self.input_thread(label1)
            input2 = self.input_thread(label2)

            distance = self.input_number(f"Enter distance from {label1} to {label2} : ",float)

            survey = Survey_Point(label,input1,input2,distance,initial_elev)
            initial_elev = survey.elevation
            self.ctrl.data.append(survey)

            self.ctrl.point_group_index += 1
            self.ctrl.ascii+=1

        self.show_info()
        self.excel_and_graph()
        
        
        

    def input_thread(self,prompt):
        '''Prompt for top/mid/bottom thread values and compute a valid mid-thread'''
        while True:
            try:
                clear_screen()
                self.header()
                print(f'CALCULATE {prompt}')
                print("-"*20)
                top_thread = float(input(f"enter the top trhead, if there is'nt, enter '0' : "))               
                mid_thread = float(input(f"enter the mid thread : "))
                bottom_thread = float(input(f"enter the bottom trhead,if there is'nt, enter '0' : "))
                isdone = self.check()
                if  isdone == 'n':
                    continue
                result_mid_thread = self.ctrl.calculate_mid_thread(top_thread,mid_thread,bottom_thread)
                if top_thread != 0 and bottom_thread != 0:
                    self.print_formula(top_thread,mid_thread,bottom_thread,result_mid_thread,"valid" if mid_thread == result_mid_thread else "invalid")
                input("Enter to continue....")
                return result_mid_thread
                
            except ValueError:
                print("\nMUST BE A NUMBER OR DECIMAL!")
                input("Enter to continue : ")
                continue
                
                 
    def print_formula(self,top_thread,mid_thread,bottom_thread,result_mid_thread,valid):
        '''Display mid-thread calculation steps and validity'''
        print("-"*20)
        print(f'mid thread = {top_thread} + {bottom_thread}/ 2')
        print(f'{mid_thread} = {result_mid_thread} → {valid}')
        print(f'\nmid thread → {valid}')
        

    
    def header(self):
        '''Header display of the program'''
        print("="*20)
        print(f"{'LAND MEASUREMENT':^20}")
        print("="*20)

    def input_number(self,prompt,type_):
        '''Prompt for a numeric input (int or float) with confirmation'''
        while True:
            try:
                clear_screen()
                self.header()
                variable = type_(input(f"{prompt}"))
                isdone =self.check()
                if isdone == "n":
                    continue
                return variable
            
            except ValueError :
                if type_ == int:
                    print("MUST BE AN INTEGER!")
                    input('enter for continue : ')
                    continue
                else:
                    print("MUST BE AN INTEGER OR DECIMAL")
                    input('enter for continue : ')
                    continue

  
    def check(self):
        '''Ask the user to confirm their input'''
        isdone = input("\nWas your input correct? (y/n): ")
        while isdone not in ('y','n'):
            print('choose y/n!')
            isdone = input("Was your input correct? (y/n): ")
        return isdone
        
    def show_info(self):
        '''Display the survey results table using tabulate'''
        clear_screen()
        self.header()
        print("Elevation Data Result:")
        print(20*"-")
        table = self.ctrl.get_table()
        print(f"FIRST AMSL: {self.ctrl.amsl:3f}")
        print(tabulate(table, headers="keys", tablefmt="fancy_grid", floatfmt=".3f"))
        input("Enter to continue.....")
    
    def say_congrats(self,f_type):
        '''Print a congratulatory message'''
        print("-"*20)
        print(f'CONGRATULATION,{f_type}!')
        print("-"*20)


    def excel_and_graph(self):
        '''Make DataFrame'''
        table= pd.DataFrame(self.ctrl.get_table())

        '''Exporting to Excel (with CSV fallback)'''
        clear_screen()
        self.header()
        send_excel = input_yes_no("\nDo you want to send this result to excel? (y/n) : ")
        if send_excel:
            try:
                to_excel(table)
                self.say_congrats("THE FILE HAS BEEN CREATED IN EXCEL")
                input("Enter to continue.....")

            except Exception as e:
                clear_screen()
                self.header()
                print(f"Export failed: {e}")
                print("\nBecause result can't export to excel The result will make csv file....")
                export_to_csv(table)

        '''Generating PNG plots'''
        clear_screen()
        self.header()
        send_graph = input_yes_no("\nDo you want make the graphics of the result? (y/n) : ")
        if send_graph:
            try:
                make_graphic(table)
                self.say_congrats("THE FILE HAS BEEN CREATED IN PNG")
                input("Enter to continue.....")

            except Exception as e:
                print(f"Failed to generate graphics: {e}")
                input("Enter to continue.....")
        else:
            print("\nTHANKS FOR USING THIS PROGRAM!")

        '''Embedding plots into Excel'''
        if send_graph and send_excel :
            clear_screen()
            self.header()
            send = input_yes_no("\nDo you want to make it's result and it's graphic to excel? (y/n) : ")
            if send:
                try:
                    graphic_to_excel()
                    self.say_congrats("THE FILE HAS BEEN MADE!")
                    input("Enter to continue.....")

                except Exception as e:
                    print(f"Failed to embed graphics: {e}")
                    input("Enter to continue.....")