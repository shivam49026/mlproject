import sys
<<<<<<< HEAD

def error_message_detail(error,error_detail:sys):
   _,_,exc_tb = error_detail.exc_info()
   file_name = exc_tb.tb_frame.f_code.co_filename
   error_message ="Error ocuurred in python script name[{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

   return error_message

   
class CustomException(Exception): #ingheritinhg from Parent (Exception) class
   def __init__(self,error_message,error_detail:sys):
      super.__init__(error_message)
      self.error_message=error_message_detail(error_message,error_detail=error_detail)
=======
import logging
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message ="Error ocuurred in python script name[{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

   

class CustomException(Exception): #ingheritinhg from Parent (Exception) class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
      return self.error_message
    
# if __name__ == "__main__":
#     try :
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)
    
>>>>>>> 8556bbd64ec1064de265a56d281f977cd8f518c7
