class SubCategory():
    def __init__(self, id, name, category):
        self.__id = id
        self.__name = name
        self.__category = category

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    def __str__(self):
        """To string method

        :return: String displaying subcategory.
        """
        return "id = {}\nname = {}\nsubcategories = {}".format(
            self.__id,
            self.__name,
            self.__category.name)
