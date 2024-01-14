from botcity.core import DesktopBot
from botcity.maestro import *
import pandas as pd 
from modules.EmailBuilder import EmailSender
import modules.SetLog
import os


class ProductRegistration:
    def __init__(self):
        self.set_log = modules.SetLog.SetLog()
        self.email_builder = EmailSender()
        try:
            self.bot = DesktopBot() #Instanciando o bot
            self.bot.execute(r"C:\Program Files\Fakturama2\Fakturama.exe") #Executando o app
        except Exception as e:
            self.set_log.set_log_error(str(e))

    def register_product(self, data_frame, file_name):
        try:
            if self.bot.find( "logo", matching=0.97, waiting_time=200000):
                for index, row in data_frame.iterrows():
                    try:
                        product = row['product']
                        category = row['category']
                        code = row['code']
                        identifier = row['id']
                        description = row['description']
                        price = str(row['price'])
                        cost_price = str(row['price'] * 0.6)
                        stock = row['stock']
                        status = row ['status']
                                        
                        if self.bot.find( "newProductBtn", matching=0.97, waiting_time=10000):
                            self.bot.click()
                            self.bot.wait(1000)
                                                
                        if self.bot.find( "itemNumberField", matching=0.97, waiting_time=10000):
                            self.bot.click_relative(192, 5)
                            self.bot.kb_type(str(index))
                            self.bot.tab()                                 
                            self.bot.paste(product)
                            self.bot.tab()
                            self.bot.paste(category)
                            self.bot.tab()
                            self.bot.paste(code)
                            self.bot.tab()
                            self.bot.paste(identifier)
                            self.bot.tab()
                            self.bot.paste(description)
                            self.bot.tab()
                            self.bot.control_a()
                            self.bot.paste(price)
                            self.bot.tab()
                            self.bot.control_a()
                            self.bot.paste(cost_price)
                            self.bot.tab()
                            self.bot.tab()
                            self.bot.tab()
                            self.bot.control_a() #apaga o valor que existe lá
                            self.bot.paste(stock)                           
                            if self.bot.find( "saveButton", matching=0.97, waiting_time=10000):
                                self.bot.click()
                            self.bot.control_w()
                            
                            self.new_file_name = file_name.replace('.xlsx', ' - Completed.xlsx')                           
                            data_frame.loc[index,'status'] = 'OK'                            
                            data_frame.to_excel(self.new_file_name, index = False)                                               
                            notify, code = 'SUCCESS', code
                            self.email_builder.main_email(notify, code)
                            set_log = modules.SetLog.SetLog()                            
                            set_log.set_log_info(f'Product {code} successfully registered')

                    except Exception as e:
                        notify, code = 'REGISTRATION ERROR', code
                        self.set_log.set_log_error(e)
                        self.email_builder.main_email(notify, email_body=e)
                           
                notify = 'Final'
                code = ""
                set_log.set_log_info('Process has finished')
                self.email_builder.main_email(notify=notify, code=code, file_name=self.new_file_name)    
                self.bot.wait(2000)
                self.bot.alt_f4() 
                
        except Exception as e:
                notify, code = 'ERROR', ""
                self.set_log.set_log_error(e)
                self.email_builder.main_email(notify, email_body=e)
                

    def file_name(self):
         try:
            new_workbook_name = self.new_file_name
            print('pegou o new workbook name')
            return new_workbook_name
         except Exception as e:
            notify = 'ERROR'
            self.set_log.set_log_error(e)
            self.email_builder.main_email(notify, email_body=e)
           
