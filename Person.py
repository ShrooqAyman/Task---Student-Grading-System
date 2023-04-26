import abc

class Person():
    """
    A class representing a person.

    Attributes:
        id (int): id of the person.
        name (str): name of the person.
        age (int): age of the person.
        email (str): email of the person.
    """


    def __init__(self, id:int, name:str, age:int, email:str):
        """
        Initialize a new person with the given id, name , age and email.
        
        Args:
            id (int): id of the person.
            name (str): name of the person.
            age (int): age of the person.
            email (str): email of the person.
        """
        if age < 0:
            print('age must be larger than 0')
            return
        else:
            try:
                self.id = id
                self.name = name
                self.age = age
                self.email = email
            except Exception as e:
                print(f'Error: {e}')


    def get_id(self):
        """
        Return person's id.
        
        Returns:
            int: an integer representing person's id.
        """
        return self.id


    def get_email(self):
        """
        Return person's email.
        
        Returns:
            str: a string representing person's email.
        """
        return self.email


    def get_name(self):
        """
        Return person's name.
        
        Returns:
            str: a string representing person's name.
        """
        return self.name


    def get_age(self):
        """
        Return person's age.
        
        Returns:
            int: an integer representing person's age.
        """
        return self.age


    def get_info(self):
        return f'Id: {self.id} - Name: {self.name} - Email: {self.email} - Age: {self.age}'