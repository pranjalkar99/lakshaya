class EventNotFound(Exception):
    """Handles invalid event type provided to 
        publishers

        Attributes:
            event_type --> the event that's invalid
            message --> additional message to log or print
    
    """
 
    def __init__(self, event_type: str, message: str ="invalid event"):
        self.event_type = event_type
        self.message = message

    def __repr__(self):
        return f"{self.event_type} --> {self.message}"


class DuplicateStudent(Exception):
    """Handles dupicate student error

        Attributes:
            message --> additional message to log or print
    
    """
 
    def __init__(self, message: str ="student already exists"):

        self.message = message

    def __repr__(self):
        return {self.message}

class OutOfLimit(Exception):
    """Handles out of limit error

        Attributes:
            message --> additional message to log or print
    
    """
 
    def __init__(self, message: str ="array out of limit"):

        self.message = message

    def __repr__(self):
        return {self.message} 

class AuthenticationError(Exception):
    """Handles user authentication error

        Attributes:
            message --> additional message to log or print
    
    """
 
    def __init__(self, message: str ="user is not authenticated"):

        self.message = message

    def __repr__(self):
        return f"{self.message}"



class UnauthorizedUser(Exception):
    """Handles user authorization error

        Attributes:
            message --> additional message to log or print
    
    """
 
    def __init__(self, user_role, message: str ="user is not authorized"):

        self.user_role = user_role
        self.message = message

    def __repr__(self):
        return (
            f"User {self.user_role}: {self.message}"
        )


class UnexpectedError(Exception):
    """Handles unknown errors

        Attributes:
            message --> additional message to log or print
    
    """
 
    def __init__(self, message: str ="unexpected error occured"):

        self.message = message

    def __repr__(self):
        return {self.message}


class NotFoundError(Exception):
    """Handles not found

        Attributes:
            message --> additional message to log or print
    
    """
 
    def __init__(self, message: str ="element not found"):

        self.message = message

    def __repr__(self):
        return {self.message}