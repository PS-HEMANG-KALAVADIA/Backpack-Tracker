class Item:
    def __init__(self, item_name, essential):
        self.__item_name = item_name
        self.__essential = essential

    def get_item_name(self):
        return self.__item_name

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def is_essential(self):
        return self.__essential

    def set_essential(self, essential):
        self.__essential = essential
