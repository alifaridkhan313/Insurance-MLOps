import os
import sys

#this particular file would be responsible for handling exceptions in the code
#we would be implementing try catch block which will try and catch the error with the lines and files with errors


class CustomException(Exception):
    def __init__(self, error_message = Exception, error_details = Exception):
        self.error_message = CustomException.get_detailed_error_message(
            error_message = error_message, 
            error_details = error_details
        )

#try --> except 

    @staticmethod
    def  get_detailed_error_message(error_message: Exception, error_details: sys) -> str:
        _, _, exce_tb = error_details.exc_info()

        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error occured in execution of: 
        [{file_name}] at 
        try block line number: [{try_block_line_number}]
        and exception block line number: [{exception_block_line_number}]
        error message: [{error_message}]
        """
        return error_message
    
    def __str__(self): 
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()   