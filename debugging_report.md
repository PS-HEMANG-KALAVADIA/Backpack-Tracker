# Debugging Report: Smart Backpack Tracker

This report details a logical bug intentionally introduced in the **Backpack** class (inside the `backpack_tracker_buggy/` directory) for educational and debugging practice.

---

## 1. Bug Description

When a user attempts to remove a packed item using Menu Option 2, the console prints:
`Item removed successfully.`

However, viewing the backpack contents afterwards using Menu Option 3 ("View Backpack") reveals that the item is still present in the list. The item is not actually removed from the internal `__items` list.

---

## 2. Expected Result

1. User selects **Option 2 (Remove Item)**.
2. User inputs the name of an item currently in the backpack (e.g. `Charger`).
3. The console prints: `Item removed successfully.`
4. User selects **Option 3 (View Backpack)**.
5. The console shows the updated list with the item (`Charger`) completely gone.

---

## 3. Actual Result

1. User selects **Option 2 (Remove Item)**.
2. User inputs the name of an item currently in the backpack (e.g. `Charger`).
3. The console prints: `Item removed successfully.`
4. User selects **Option 3 (View Backpack)**.
5. The console shows the item (`Charger`) is still present in the backpack listing.

---

## 4. Root Cause

The issue is located in [backpack.py (Buggy)](file:///c:/Users/HemangKalavadiya/Documents/Projects/OOPs%20Project/backpack_tracker_buggy/backpack.py#L11-L16):

```python
def remove_item(self, item_name):
    for i in range(len(self.__items)):
        if self.__items[i].get_item_name().lower() == item_name.lower():
            # INTENTIONAL BUG: The item matches, but we do not actually remove it from the list
            # self.__items.pop(i)
            return True
    return False
```

The method successfully searches the list, matches the correct item name using the `lower()` method, and returns `True`. However, because the actual deletion line `self.__items.pop(i)` is commented out, the item is never removed from the `self.__items` list. The `main.py` script receives `True` from the call and prints the success message, leading to a mismatched state.

---

## 5. Debugging Steps

Here are the steps to locate and resolve the bug:

1. **Trace the User Action**: Trace the flow starting from `main.py` inside the branch for choice `2`. Notice that the variable `removed` stores the boolean returned by `backpack.remove_item(item_name)`. If `removed` is `True`, it prints `"Item removed successfully."`.
2. **Review Backpack's logic**: Open `backpack.py` and navigate to the `remove_item` method.
3. **Inspect the Loop Statement**: Trace the loop line by line. When the item matches the user input:
   - Observe that `return True` is invoked immediately.
   - Observe that the list mutation call `self.__items.pop(i)` is commented out.
4. **Fix the code**: Re-enable the deletion call so that the element at index `i` is removed from the `self.__items` list.

---

## 6. Where Screenshots Should Be Taken

For your college assignment submission, please run the buggy version and take screenshots of the following console states:

1. **Screenshot 1 (Populated Backpack)**: Take a screenshot after adding a few items (e.g., Laptop, Charger) and viewing them using Option 3.
2. **Screenshot 2 (Bug Occurrence)**: Take a screenshot showing Option 2 selection, entering `Charger`, and the output showing `Item removed successfully.`.
3. **Screenshot 3 (Stale View)**: Take a screenshot showing Option 3 selection immediately after the removal attempt, displaying the backpack contents with the `Charger` still in the list.

---

## 7. Corrected Code

Here is the comparison diff of the `remove_item` method showing the fix:

```diff
  def remove_item(self, item_name):
      for i in range(len(self.__items)):
          if self.__items[i].get_item_name().lower() == item_name.lower():
-             # INTENTIONAL BUG: The item matches, but we do not actually remove it from the list
-             # self.__items.pop(i)
-             return True
+             # Correct code: Remove the item from the list using pop
+             self.__items.pop(i)
+             return True
      return False
```

---

## 8. Final Fix Explanation

By invoking the `pop(index)` method of Python's standard `list` class, we remove the item element at the given index `i` from the list. Subsequent iterations or calls to `view_items()` will access the modified list where the item is no longer present.
