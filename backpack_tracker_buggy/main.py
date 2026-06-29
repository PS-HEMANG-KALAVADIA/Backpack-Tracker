from student import Student
from item import Item
from backpack import Backpack

def main():
    backpack = Backpack()

    print("=== Student Registration ===")
    name = input("Enter your Name: ").strip()
    student_id = input("Enter your Student ID: ").strip()
    course = input("Enter your Course: ").strip()

    student = Student(name, student_id, course)
    print(f"\nWelcome, {student.get_name()} ({student.get_student_id()}) enrolled in {student.get_course()}!")

    while True:
        print("\n====== Smart Backpack Tracker ======")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Backpack")
        print("4. Check Essential Items")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            item_name = input("Enter item name: ").strip()
            if not item_name:
                print("Error: Item name cannot be empty.")
                continue
            essential_input = input("Is this item essential? (yes/no): ").strip().lower()
            essential = essential_input in ["yes", "y"]
            item = Item(item_name, essential)
            backpack.add_item(item)

        elif choice == "2":
            item_name = input("Enter item name to remove: ").strip()
            if not item_name:
                print("Error: Item name cannot be empty.")
                continue
            removed = backpack.remove_item(item_name)
            if removed:
                print("Item removed successfully.")
            else:
                print("Item not found in your backpack.")

        elif choice == "3":
            backpack.view_items()

        elif choice == "4":
            backpack.check_essentials()

        elif choice == "5":
            print("Exiting Smart Backpack Tracker. Good luck!")
            break
        else:
            print("Error: Invalid choice. Choose a menu option between 1 and 5.")

if __name__ == "__main__":
    main()
