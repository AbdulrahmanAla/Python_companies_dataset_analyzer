#############################################################################
# Project 9
#
# create an open_file function that prompts the user to input a file name to open and keeps prompting until a correct name is entered
#
# create a read file function that takes the file pointer that has the names of the companies and their codes. it skips the header line and creates a set of all the company’s names. And it also creates a master dictionary where the key is the company code and the value is spesific information asked in the document.
#
# create add_price function, that does not return anything, but it changes the master dictionary while reading the prices file. 
#create amax_price function, This function takes the master dictionary and a company symbol, and it gets the max high price and the date of the max price. It returns the tuple
#
# create find_max_friends function, This function takes a list of names and the corresponding list of friends and determines who has the most friends (max_number).
#
# create a max price function. This function takes the master dictionary and finds the company with the highest high price. it uses the function get_max_price_of_company to get each company’s high price.
#
# create average price for comapny function. This function uses the master dictionary and company symbol to find the average high price for the company
#create a display function. This function does not return anything, but it takes a list of strings and displays that list in three columns, each column is 35 characters wide.
#
#Tcreate the menu function. his function is where the user is going ract with your program. it would print the welcoming banner provided. Then, it would open both files and create a master dictionary by calling the respective functions. it would always displaythe options,and then ask for the user input. Re-prompt on invalid input. 
#
#############################################################################


import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    \n'''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''Docstring'''
    loop= True
    while loop == True: # here I made a loop so the user will be asked many times until they enter a valid file name
        try:
            promot= input("\nEnter the price's filename: ")
            filename= promot
            fp= open(filename,"r")# opened the file in reading mode
            loop = False
        except FileNotFoundError:# I made an except if the file wasn't found an error message wil be printed and the user will be asked again
            print("\nFile not found. Please try again.")
    
        
    loop2 = True
    while loop2 == True: # here I made a loop so the user will be asked many times until they enter a valid file name
        try:
            promot2= input("\nEnter the security's filename: ")
            filename2 = promot2
            fp2= open(filename2,"r")# opened the file in reading mode
            loop2 = False
        except FileNotFoundError:# I made an except if the file wasn't found an error message wil be printed and the user will be asked again
            print("\nFile not found. Please try again.")
    
    return fp,fp2
    
    
#This function takes the file pointer that has the names of the companies and their codes. it skips the header line and creates a set of all the company’s names. And it also creates a master dictionary where the key is the company code and the value is spesific information asked in the document. 
def read_file(securities_fp):
    '''Docstring'''
    reader= csv.reader(securities_fp)# use csv.reader to skip the header line
    next(reader, None)# skips the header line
    companies_name_set= set()# create a set
    companies_dict= {}# create a dict
    for line in reader:# loop inside the csv file
        companies_name_set.add(line[1])# this line would get the company code and add it to the set
        
        companies_dict[line[0]] = [line[1],line[3],line[4],line[5],line[6],[]]# this line would add the company code as a key for the dictionary and add the specified value  
    return companies_name_set, companies_dict
#This function does not return anything, but it changes the master dictionary while reading the prices file. 
def add_prices (master_dictionary, prices_file_pointer):
    '''Docstring'''
    reader= csv.reader(prices_file_pointer)#use csv.reader to skip the header line
    next(reader, None)# skips the header line
    
    for line in reader: # create a loop on the prices file
        
        if line[1] in master_dictionary.keys():# this would check if the company code is in the  keys of the dictonary

            master_dictionary[line[1]][5].append([line[0],float(line[2]),float(line[3]),float(line[4]),float(line[5])])# this line would  get into the empty list and append the specified values into the list
        else:# if the company code wasn't in the dictonary keys it sould skip it
            continue # using continue it would skip that code
    pass
    
#This function takes the master dictionary and a company symbol, and it gets the max high price and the date of the max price. It returns the tuple
def get_max_price_of_company (master_dictionary, company_symbol):
    '''Docstring'''
    max_price= []
    if company_symbol not in master_dictionary:
        return (None,None)

    for i in master_dictionary[company_symbol][5]:# this line would loop inside the list that we added some information before in the previous function
        if i == []:#this line would check if the list we created from the previous function is empty or not and if it was empty it would return None None as asked in the document
            return ( None, None)
        tup=(i[4],i[0])# this line would get the high info and the date and add it to a tuple
        max_price.append(tup)# this line would append the tup to the list max_price
    if max_price == []:#this line would check if the list we created from the previous function is empty or not and if it was empty it would return None None as asked in the document
        return ( None, None)
    return max(max_price)#this would  get the max price using max function 

    pass
#This function takes the master dictionary and finds the company with the highest high price. it uses the function get_max_price_of_company to get each company’s high price.
def find_max_company_price (master_dictionary):
    '''Docstring'''
    comanpy__max__price__list= [] # this line would create a list to add the prices of the compnies
    for comanpy_code in master_dictionary: # this line would loop in the dictonary
        max_company_price= get_max_price_of_company(master_dictionary,comanpy_code) # this line would use the previous function to get the max price of a specified company and sotre it in a variable to use it later
        if max_company_price == (None,None): # based on the document if the company was none it would skip it
            continue # using continue would skip it
        tup= (max_company_price[0],comanpy_code)# store the values inside a tuple 
        comanpy__max__price__list.append(tup)# add the tuple inside a list
    max_value=max(comanpy__max__price__list)# get the max value of the list
    return max_value[::-1]# return the max but in reverse as asked it is shown in the tests
    pass
#a. This function uses the master dictionary and company symbol to find the average high price for the company
def get_avg_price_of_company (master_dictionary, company_symbol):
    '''Docstring'''
    total=0 #specifiy a value to the toal
    if company_symbol in master_dictionary:# check if the company code is inside the dictonary

        for i in master_dictionary[company_symbol][5]:# if the company code inside the dictonary it would add the price to the total value and keep addint it everytime
            total+= i[4]
    
        index= len(master_dictionary[company_symbol][5])# this line would get how many prices are there to calculate the average
        avg= round((total/index),2)#round the average
        return avg
    else:# if the company was None it would retuen 0.0
        return 0.0
    pass
#This function does not return anything, but it takes a list of strings and displays that list in three columns, each column is 35 characters wide.       
def display_list (lst):  # "{:^35s}"
    text = ""
    number = 0
    for index,data in enumerate(lst):# this line would enumerate over the list
        inde = index+1
        if inde % 3 == 0:# this line would prevent from adding new line when tere are less than 3 in the same line
            text += "{:^35s}".format(data) #formating as asked in the pdf
            print(text) # print the text in three columns
            number = 0 # reset the number of columns
            text = "" # reset each row 
        else:
            number += 1 
            text += "{:^35s}".format(data)
    if number == 1: 
        print(text + "\n") 
    else:
        print("\n")
        
    
# # This function is where the user is going ract with your program. it would print the welcoming banner provided. Then, it would open both files and create a master dictionary by calling the respective functions. it would always displaythe options,and then ask for the user input. Re-prompt on invalid input.   
def main():
    print(WELCOME) # print welcome
    file1, file2 = open_file() # open the files
    companySet, dic = read_file(file2) # this line would read the file and store it in the two variables
    add_prices(dic,file1) 
    loop = True
    while loop != False: # create a loop that would keep asking until the user exit from it
        try:
            promot_for_menu= int(input(MENU))
            print("\nOption: ") 
            if str(promot_for_menu) not in "123456":# this line would check if the promot was an option or not
                print("\nInvalid option. Please try again.")# if the user enter any value other than options number it would print an error message
            loop = False
        except ValueError:# if the user enters a string it would exceute this except statement
            print("\nOption: ") 
            print("\nInvalid option. Please try again.")
            # the lines above are writen so if the user enter invalid value it would print an invalid print stement and repromot again
    while promot_for_menu != 6: # if the user enters the last option it would exit from it
        if promot_for_menu == 1:
            print("{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            sorted_companySet = sorted(companySet)# sort the compnies set
            display_list(sorted_companySet)# use the display list to display the sorted company set in the correct format
        elif promot_for_menu == 2:
            print("companies' symbols:")
            company_symbols = list(dic.keys())# this line would get a list of the company names
            company_symbols.sort()           # sort the company names
            display_list(company_symbols)#use the display list to display the sorted company_symbols in the correct format
        elif promot_for_menu == 3:
            loop = True
            while loop != False:
                promot_for_company= input('Enter company symbol for max price: ') #this line would ask for compan
                if promot_for_company not in dic: # this line would check if the company in the dictionary 
                    print("\nError: not a company symbol. Please try again.\n")
                else:
                    loop = False # stop the loop after check the company symbol
            max_price_company = get_max_price_of_company(dic,promot_for_company) # assign the maximum price to a varible [max_price_company]
            if max_price_company != (None,None): # if the max price is not found, it will print the max price for the company 
                print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(max_price_company[0],max_price_company[1]))
            else: # print no prices if there is no max price
                print("\nThere were no prices.")
        elif promot_for_menu == 4:
            max_price_company =  find_max_company_price(dic) # call the function find_max_company_price() and assign it to max_price_company
            print("The company with the highest stock price is {:s} with a value of ${:.2f}\n".format(max_price_company[0],max_price_company[1])) # print the max price company as (name of the company, the max price of the company)
        elif promot_for_menu == 5:
            loop = True # loop until finish the checking
            while loop != False: 
                promot_for_company= input('Enter company symbol for average price: ')
                if promot_for_company not in dic:   # this line would check if the company in the dictionary 
                    print("\nError: not a company symbol. Please try again.\n")
                else:
                    loop = False # stop the loop after check the company symbol
            avg_company = get_avg_price_of_company(dic,promot_for_company) # call get_avg_price_of_company() and assign it to avg_company 
            print("\nThe average stock price was ${:.2f}.\n".format(avg_company))
        ### ask again for the input ###
        loop = True
        while loop != False: # create a loop that would keep asking until the user exit from it
            try:
                promot_for_menu= int(input(MENU))
                print("\nOption: ") 
                if str(promot_for_menu) not in "123456":# this line would check if the promot was an option or not
                    print("\nInvalid option. Please try again.")# if the user enter any value other than options number it would print an error message
                loop = False
            except ValueError:# if the user enters a string it would exceute this except statement
                print("\nOption: ") 
                print("\nInvalid option. Please try again.")
                # the lines above are writen so if the user enter invalid value it would print an invalid print stement and repromot again
            
if __name__ == "__main__": 
    main() 
