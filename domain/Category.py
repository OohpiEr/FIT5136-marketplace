class Category():
    """Category class"""
    def __init__(self, id, name):
        """Constructor

        :param id: category id, primary key
        :param name: category name
        """
        self.__id = id
        self.__name = name
        self.__subcategories = []

    @property
    def name(self):
        """Getter for category name

        :return: category name
        """
        return self.__name
    
    @property
    def id(self):
        """Getter for category id

        :return: category id
        """
        return self.__id

    @property
    def subcategories(self):
        """Getter for category subcategories

        :return: list of subcategories in the category
        """
        return self.__subcategories

    def add_subcategory(self, subcategory):
        """Adds a subcategory to the category

        :param subcategory: Subcategory object
        """
        self.__subcategories.append(subcategory)


    def __str__(self):
        """To string method

        :return: String displaying category.
        """
        return "id = {}\nname = {}\nsubcategories = {}".format(
            self.__id,
            self.__name,
            str(self.__subcategories))

