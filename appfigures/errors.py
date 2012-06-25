
#Status Codes
BAD_PARAM = 400
NOT_AUTHENTICATED = 401
UNAUTHORIZED = 403
NOT_FOUND = 404
EXCEEDED_REQUESTS = 420
GENERAL_ERROR = 500
API_UNAVAILABLE = 503


class AppFiguresException(Exception):
    def __init__(self, status, description, message, additional, reference):
        self.status = status
        self.description = description
        self.message = message
        self.additional = additional
        self.reference = reference
    
    @property
    def ref_string(self):
        return "Ref #: {0}".format(self.reference) if self.reference else None
    
    def __unicode__(self):
        parts = (self.status, self.description, self.message, self.additional, self.ref_string)
        return ". ".join((str(s) if s else None for s in parts))
    
    def __str__(self):
        return unicode(self).encode("utf-8")
    

class BadParameterException(AppFiguresException):
    """One of the parameters in the request are incorrect or invalid"""
    def __init__(self, message, additional, reference):
        super(BadParameterException, self).__init__(BAD_PARAM, self.__doc__, 
                                                    message, additional, reference)
        
class NotAuthenicatedException(AppFiguresException):
    """The user or password are incorrect"""
    def __init__(self, message, additional, reference):
        super(NotAuthenicatedException, self).__init__(NOT_AUTHENTICATED, self.__doc__, 
                                                       message, additional, reference)
        
class UnauthorizedException(AppFiguresException):
    """The authenticated user does not have permission to access the requested resource"""
    def __init__(self, message, additional, reference):
        super(UnauthorizedException, self).__init__(UNAUTHORIZED, self.__doc__, 
                                                    message, additional, reference)
        
class NotFoundException(AppFiguresException):
    """The resource you are requesting does not exist"""
    def __init__(self, message, additional, reference):
        super(NotFoundException, self).__init__(NOT_FOUND, self.__doc__, 
                                                message, additional, reference)
        
class RequestLimitException(AppFiguresException):
    """You have exceeded the number of allowed requests for the day"""
    def __init__(self, message, additional, reference):
        super(RequestLimitException, self).__init__(EXCEEDED_REQUESTS, self.__doc__, 
                                                    message, additional, reference)

class ServerException(AppFiguresException):
    """AppFigures Server Error"""
    def __init__(self, message, additional, reference):
        super(ServerException, self).__init__(GENERAL_ERROR, self.__doc__, 
                                              message, additional, reference)
class UnavailableException(AppFiguresException):
    """The API is currently unavailable due to maintenance"""
    def __init__(self, message, additional, reference):
        super(UnavailableException, self).__init__(API_UNAVAILABLE, self.__doc__, 
                                                   message, additional, reference)


EXCEPTIONS = {
    BAD_PARAM: BadParameterException,
    NOT_AUTHENTICATED: NotAuthenicatedException,
    UNAUTHORIZED: UnauthorizedException,
    NOT_FOUND: NotFoundException,
    EXCEEDED_REQUESTS: RequestLimitException,
    GENERAL_ERROR: ServerException,
    API_UNAVAILABLE: UnavailableException
}

        
    



