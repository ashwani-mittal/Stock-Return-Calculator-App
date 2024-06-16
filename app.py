from app.domain.Industry import Industry
from app.domain.StockReturn import StockReturn
from app.utils.reader import convert_industry, convert_stock_returns
import app.utils.stockutils as stockutils
from app.domain.exceptions.InvalidStockName import InvalidStockName
from app.domain.exceptions.InvalidIndustry import InvalidIndustry


# main app file
def main():
    return_file_path = "resources\Stock_Returns.txt"
    industry_file_path = 'resources\Stock_Industry.txt'
    with open(return_file_path, 'r') as r:
        lines = r.readlines()
        # Start from line 1 to ignore the headers in the data file.
        stock_returns: list[StockReturn] = convert_stock_returns(lines[1:])



    with open(industry_file_path, 'r') as i:
        lines = i.readlines()
        industries: list[Industry] = convert_industry(lines[1:])
    
    while True:
        print_main_menu()
        user_selection = int(input("Select Option: "))
        if user_selection == 0:
            break
        elif user_selection == 1:
            print("\n\nDistinct Stocks: ")
            print(stockutils.get_distinct_stocks(stock_returns))
            print("----------------------------\n\n")
            continue
        elif user_selection == 2:
            stock_name = input('Please Enter the name of the stock: ').upper()
            
            try:
                print('\n\nMin, Max and Average return for the stock: ' + stock_name)
                print(stockutils.get_stock_stats(stock_returns, stock_name))
                print("----------------------------\n\n")
            except:
                print(f"You entered an Invalid Stock name.\nTRY AGAIN!\nChoose from the list below: \n{stockutils.get_distinct_stocks(stock_returns)}\n\n" )
                 
        elif user_selection == 3:
            industry_name= input('Please Enter the name of the Industry: ')
            try:
                print('\n\nMin, Max and Average return for the ' + industry_name + ' Industry: ')
                print(stockutils.get_industry_stats(stock_returns,industries,industry_name))
                print("----------------------------\n\n")
            except:
                print(f"You entered an Invalid Industry name.\nTRY AGAIN!\nChoose from the list below: \n{stockutils.get_distinct_industries(industries)}\n\n" )
                 
        else:
            print("INVALID INPUT. \nPlease choose an option from the menu!!\n\n")


def print_main_menu():
    print('Welcome to the Stock Return Calculator!')
    print('Please choose option from the Menu:')
    print('1. Get a list of all distinct Stocks')
    print('2. Get min, max and average return of a Stock')
    print('3. Get min, max and average return of an Industry')
    print('0. Exit App!')   
main()
    
