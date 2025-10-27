import json
from datetime import datetime
# FIX: Removed unused 'logging' import (Pylint: unused-import)
# FIX: Imports are now one per line (Flake8: E401)

# Global variable
stock_data = {}


def addItem(item="default", qty=0, logs=None):
    """
    Adds a quantity of an item to the stock.
    """
    # FIX: (Pylint: dangerous-default-value)
    # Changed default argument from [] to None to prevent
    # all calls from sharing the same mutable list.
    if logs is None:
        logs = []

    # [cite_start]FIX: Added input validation (Lab Suggestion [cite: 77])
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Error: Invalid types for item ({type(item)}) or qty ({type(qty)}). Skipping.")
        return

    if qty <= 0:
        print(f"Warning: Cannot add zero or negative quantity ({qty}) for {item}. Skipping.")
        return

    if not item:
        print("Warning: Cannot add item with no name. Skipping.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    
    # [cite_start]FIX: Use f-string for logging (Pylint: logging-fstring-interpolation) [cite: 76]
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def removeItem(item, qty):
    """
    Removes a quantity of an item from the stock.
    """
    # FIX: Added input validation
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Error: Invalid types for item ({type(item)}) or qty ({type(qty)}). Skipping.")
        return
    
    if qty <= 0:
        print(f"Warning: Cannot remove zero or negative quantity ({qty}) for {item}. Skipping.")
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # [cite_start]FIX: (Pylint: broad-except) [cite: 75]
    # Replaced bare 'except:' with the specific 'KeyError'
    # to avoid catching unintended errors.
    except KeyError:
        print(f"Warning: Item '{item}' not found, cannot remove.")


def getQty(item):
    """
    Gets the quantity of a specific item.
    """
    # FIX: Use .get() for safe dictionary lookup to prevent KeyError
    # if the item does not exist.
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """
    Loads inventory data from a JSON file.
    """
    global stock_data
    try:
        # FIX: (Pylint: consider-using-with)
        # Use 'with open' context manager to ensure the file
        # is always closed, even if errors occur.
        # FIX: (Pylint: unspecified-encoding) Added encoding="utf-8".
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: {file} not found, starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. File might be corrupt. Starting with empty inventory.")
        stock_data = {}


def saveData(file="inventory.json"):
    """
    Saves the current inventory data to a JSON file.
    """
    # FIX: (Pylint: consider-using-with)
    # Use 'with open' context manager.
    # FIX: (Pylint: unspecified-encoding) Added encoding="utf-8".
    with open(file, "w", encoding="utf-8") as f:
        # Added 'indent=4' for readable, pretty-printed JSON
        f.write(json.dumps(stock_data, indent=4))


def printData():
    """
    Prints a formatted report of all items in stock.
    """
    print("\n--- Items Report ---")
    # FIX: Use .items() to iterate and f-string for clean printing
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")
    print("--------------------\n")


def checkLowItems(threshold=5):
    """
    Returns a list of items with stock below the threshold.
    """
    # FIX: Replaced for-loop with a more Pythonic list comprehension
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    Main function to run the inventory system operations.
    """
    # This call will now be skipped by our validation
    loadData() # Load existing data first
    
    addItem("apple", 10)
    # This call will now be skipped by our validation
    addItem("banana", -2)
    # This call will now be skipped by our validation
    addItem(123, "ten")
    
    removeItem("apple", 3)
    # This call will now print a warning instead of passing silently
    removeItem("orange", 1)

    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")

    saveData()
    loadData() # Reload to confirm save was successful
    printData()

    # FIX: (Bandit: B307)
    # Replaced dangerous 'eval()' call with a simple 'print()'.
    print("eval used")


# FIX: (Pylint: missing-if-name-main)
# Wrap the main execution in an 'if __name__ == "__main__":' block
# so it doesn't run when the file is imported.
if __name__ == "__main__":
    main()