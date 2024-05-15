class Category():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__subcategories = []

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id

    @property
    def subcategories(self):
        return self.__subcategories

    def add_subcategory(self, subcategory):
        self.__subcategories.append(subcategory)


    def __str__(self):
        return "id = {}\nname = {}\nsubcategories = {}".format(
            self.__id,
            self.__name,
            self.__subcategories)

