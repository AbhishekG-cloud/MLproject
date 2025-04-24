import sys
from src.logger import logging
'''
The sys module in Python provides access to system-specific parameters and functions. 
It allows interaction with the Python interpreter and runtime environment. 
Here's a breakdown of its key aspects:
Core Functionality:
Interpreter Interaction: It provides access to variables and functions that interact strongly with the interpreter. 
Runtime Environment: Offers tools to manipulate different parts of the Python runtime environment. 
System-Specific Parameters: Exposes system-specific parameters and functions.
'''
 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno,str(error)

    )
    return error_message
class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a= 1/0
    except Exception as e:
        logging.info("div by zero")
        raise CustomException
    

