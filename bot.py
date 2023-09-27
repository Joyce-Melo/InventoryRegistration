from botcity.core import DesktopBot
from botcity.maestro import *
import pandas as pd 
import scripts.fileDownload
import scripts.setFileName
from scripts.emailFunctions import main_email
import datetime


def register_product(bot, data_frame, file_name):  
    if bot.find( "logo", matching=0.97, waiting_time=200000):
        for index, row in data_frame.iterrows():
            product = row['product']
            category = row['category']
            code = row['code']
            identifier = row['id']
            description = row['description']
            price = str(row['price'])
            cost_price = str(row['price'] * 0.6)
            stock = row['stock']
            status = row ['status']
                            
            if bot.find( "newProductBtn", matching=0.97, waiting_time=10000):
                bot.click()
                bot.wait(1000)
                                

                        
            if bot.find( "itemNumberField", matching=0.97, waiting_time=10000):
                bot.click_relative(192, 5)
                bot.kb_type(str(index))
                bot.tab()
                            

                                # Name
                bot.paste(product)
                bot.tab()

                                # Category
                bot.paste(category)
                bot.tab()

                                # GTIN
                bot.paste(code)
                bot.tab()

                                # Supplier code
                bot.paste(identifier)
                bot.tab()

                                # Description
                bot.paste(description)
                bot.tab()

                                # Price
                bot.control_a()
                bot.paste(price)
                bot.tab()

                                # Cost Price
                bot.control_a()
                bot.paste(cost_price)
                bot.tab()

                                # Allowance
                bot.tab()

                                # VAT
                bot.tab()

                                # Stock
                bot.control_a() #apaga o valor que existe lá
                bot.paste(stock)


                if bot.find( "saveButton", matching=0.97, waiting_time=10000):
                    bot.click()
                bot.control_w()

                new_file_name = file_name.replace(".xlsx", " - Completed.xlsx")

                data_frame.loc[index,"status"] = "OK"
                                
                data_frame.to_excel(new_file_name, index = False)
                        
            success, code = True, code
            scripts.emailFunctions.main_email(success, code)
            
        success = 'Final'
        code = ""
        scripts.emailFunctions.main_email(success, code)    
        bot.wait(2000)
        print("Finished")
        bot.alt_f4() #Fecha o app
    
    
        

def main():

    file_name = scripts.setFileName.set_file_name()

    data_frame = pd.read_excel(file_name, sheet_name='vendas')

    bot = DesktopBot() #Instanciando o bot

    bot.execute(r"C:\Program Files\Fakturama2\Fakturama.exe") #Executando o app

    # success, code = register_product(bot, data_frame, file_name)

    register_product(bot, data_frame, file_name)

    time_now = datetime.datetime.now()

    print('Process has finished at ', time_now)


    # scripts.emailFunctions.main_email(success, code)

    


        

    
if __name__ == "__main__":
    main()