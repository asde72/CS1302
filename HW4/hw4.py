import csv
import time

def chooseOption():
    print('--- --- --- Main Menu --- --- ---')
    option = input('Choose option:\n' \
         '[1] Create new text file\n' \
         '[2] Read text file content\n'
         '[3] Append to text file\n'
         '[4] Search text file\n' \
         '[5] Export to CSV\n' \
         '[6] Exit program\n'
         'option = ')
    return option

option = chooseOption()
while option != '6':
    if option == '1': #Create
        pass
        try:
                filenamecreate  = str(input("What is the file name?"))
                with open(filenamecreate, 'w') as f:
                    pass
        except:
            print('An error occurred during the CREATE operation!')


    elif option == '2':  # Read
        pass #TODO: Implement the Requirement 2 here
        try:
            filenameread= str(input("What is the file name"))
            #f string doesent work if file doesent exist
            reader =open(f'{filenameread}', 'r')
            print(reader.read())

        except:
            
            print('An error occurred during the READ operation!')    
    elif option == '3':  # Append
        pass #TODO: Implement the Requirement 3 here
        try:
            filenameappend = str(input("What is the file name"))
            filenameinput = input("What would you like to input?")
            with open(filenameappend, 'a') as appender:
                appender.write(f"{filenameinput}\n") # +\n for new line
        except:
            print("An error occurred during the APPEND operation!")
    elif option == '4':  # Find
        pass #TODO: Implement the Requirement 4 here
        try:
            filenamefind = str(input("What is the file name"))
            filenameinput = input("What would you like to find?")
            with open(filenamefind,'r') as finder:
                for line_number, line in  enumerate(finder,1):
                    if filenameinput in line:
                        print(f'File found on line {line_number}')
                    else:
                        print('No results!')
        except:
            print("An error occurred during the FIND operation!")
    elif option == '5':  # Export
            pass #TODO: Implement the Requirement 5 here
            try:
                filenameread = str(input("What file would you like to read"))
                filenameCSV = str((input("What CSV file should it be exported to?"))+'.csv')

            
                with open(filenameread, 'r') as Export:
                    text_data = Export.readlines()                        
                with open(filenameCSV, 'w', newline='') as csv_file:
                    if not filenameCSV.lower().endswith(".csv"):
                        filenameCSV += ".csv"
                    print(filenameCSV)
                    writer = csv.writer(csv_file)

                    for line in text_data:
                        writer.writerow([line.strip()])

            except:
                print("An error occurred during the EXPORT operation!")
    elif option == '6':
        pass
        exit
    else:
        print('Invalid option!')
    time.sleep(1.5)
    print('Going Back to main menu ',end='')
    for i in range(4):
        print('.', end='')
        time.sleep(.4)
    print()
    option = chooseOption()
