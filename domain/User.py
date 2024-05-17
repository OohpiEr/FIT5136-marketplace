class User:
    """User class"""

    def __init__(self, id, email, password, inventory):
        self.__id = id
        self.__password = password
        self.__email = email
        self.inventory = inventory
        

    @property
    def id(self):
        """getter for the id

        :return: id
        """
        return self.__id
    
    @property
    def password(self):
        """getter for the password

        :return: password
        """
        return self.__password
    
    @property
    def email(self):
        """getter for the email

        :return: email string
        """
        return self.__email
