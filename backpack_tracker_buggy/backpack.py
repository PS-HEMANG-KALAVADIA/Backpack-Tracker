from item import Item

class Backpack:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print("Added Successfully.")

    def remove_item(self, item_name):
        for i in range(len(self.__items)):
            if self.__items[i].get_item_name().lower() == item_name.lower():
                # INTENTIONAL BUG: The item matches, but we do not actually remove it from the list
                # self.__items.pop(i)
                return True
        return False

    def view_items(self):
        if not self.__items:
            print("Your backpack is empty.")
            return
        print("\nCurrent Backpack:")
        for item in self.__items:
            essential_marker = " [Essential]" if item.is_essential() else ""
            print(f"* {item.get_item_name()}{essential_marker}")

    def check_essentials(self):
        has_laptop = False
        has_id_card = False
        has_water_bottle = False

        for item in self.__items:
            name = item.get_item_name().lower().strip()
            if name == "laptop":
                has_laptop = True
            elif name == "id card":
                has_id_card = True
            elif name == "water bottle":
                has_water_bottle = True

        missing = []
        if not has_laptop:
            missing.append("Laptop")
        if not has_id_card:
            missing.append("ID Card")
        if not has_water_bottle:
            missing.append("Water Bottle")

        if not missing:
            print("All essential items are packed!")
        else:
            print("\nMissing Essential Items:")
            for missing_item in missing:
                print(f"* {missing_item}")

    def get_items(self):
        return self.__items
