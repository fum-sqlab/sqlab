from rest_framework import status
from rest_framework.exceptions import APIException

class exceptions(APIException):

    status_code = status.HTTP_400_BAD_REQUEST
    
    def __init__(self, type=""):
        
        if type == "field":
            self.status_code = status.HTTP_404_NOT_FOUND
            default_code = ""
            default_detail = "FIELD_NOT_FOUND."
        elif type == "form":
            self.status_code = status.HTTP_404_NOT_FOUND
            default_code = ""
            default_detail = "FORM_NOT_FOUND."
        elif type == "page":
            self.status_code = status.HTTP_404_NOT_FOUND
            default_code = ""
            default_detail = "PAGE_NOT_FOUND."
        elif type == "section":
            self.status_code = status.HTTP_404_NOT_FOUND
            default_code = ""
            default_detail = "SECTION_NOT_FOUND."
        elif type == "group":
            self.status_code = status.HTTP_404_NOT_FOUND
            default_code = ""
            default_detail = "GROUP_NOT_FOUND."

        super().__init__(detail=default_detail, code=default_code)

