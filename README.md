# Smart Backpack Tracker

## 1. Project Overview

Smart Backpack Tracker is a lightweight Python console application that showcases core Object-Oriented Programming (OOP) concepts. It allows a student to register themselves, manage backpack items, and verify that essential items are packed before leaving for college.

This project was developed as part of an Object-Oriented Programming (OOP) fundamentals assignment and demonstrates how real-world problems can be solved using classes and objects.

---

##  2. Features

*  Student registration
*  Add items to the backpack
*  Remove items from the backpack
*  View all packed items
*  Check whether essential items (Laptop, ID Card, and Water Bottle) are packed
*  Menu-driven console interface

---

##  3. OOP Concepts Used

| Concept                 | Implementation                                                                         |
| ----------------------- | -------------------------------------------------------------------------------------- |
| **Classes & Objects**   | `Person`, `Student`, `Backpack`, and `Item` classes                                    |
| **Functions (Methods)** | `add_item()`, `remove_item()`, `view_items()`, `check_essentials()`                    |
| **Encapsulation**       | Private attributes (`__name`, `__items`, `__item_name`) with getter and setter methods |
| **Inheritance**         | `Student` inherits from `Person`                                                       |

---

##  4. Project Structure

```text
Smart-Backpack-Tracker/
│
├── Simple/
│   ├── main.py
│   ├── backpack.py
│   ├── item.py
│   ├── person.py
│   └── student.py
│
├── Buggy/
│   ├── main.py
│   ├── backpack.py
│   ├── item.py
│   ├── person.py
│   └── student.py
│
├── Debugging_Report.md
└── README.md
```

---

##  5. Installation & How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/Smart-Backpack-Tracker.git
```

Navigate to the project folder:

```bash
cd Smart-Backpack-Tracker/Simple
```

Run the application:

```bash
python main.py
```

To test the debugging assignment, run the version inside the **Buggy** folder.

---

##  6. Sample Usage

```text
====== Smart Backpack Tracker ======

1. Add Item
2. Remove Item
3. View Backpack
4. Check Essential Items
5. Exit

Enter your choice: 1
Enter item name: Laptop
Added Successfully.

Enter your choice: 4

Missing Essential Items:
* ID Card
* Water Bottle
```

---

##  7. Project Status

* ✔️ Designed the project structure
* ✔️ Implemented all required classes
* ✔️ Demonstrated Classes and Objects
* ✔️ Implemented Encapsulation using private attributes
* ✔️ Implemented Inheritance (`Student` extends `Person`)
* ✔️ Developed a menu-driven console application
* ✔️ Created a working version (`Simple`)
* ✔️ Created an intentionally buggy version (`Buggy`)
* ✔️ Prepared a debugging report explaining the bug and its resolution

---

##  8. Future Improvements

* Save backpack data using file handling.
* Add categories for backpack items.
* Allow editing of existing items.
* Improve input validation and error handling.
* Add a graphical user interface (GUI).

---

##  9. Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Python Standard Library
* Console-Based Application

---

##  10. Author

**Hemang Kalavadia**


 Thank you for visiting this project!
