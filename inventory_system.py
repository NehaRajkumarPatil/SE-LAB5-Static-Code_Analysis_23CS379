"""Inventory Management System
This module allows users to add, remove, view, and save inventory items safely.
"""

import logging
import ast

# Configure logging for the main program
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Global stock data
stock_data = {}


def add_item(item, qty, logs=None):
    """Add an item and its quantity to the inventory."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, (str, int)):
        logging.error("Item name must be a string or integer.")
        return
    if not isinstance(qty, (int, float)):
        logging.error("Quantity must be a number.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logging.info(
        "Item '%s' added successfully. Current quantity: %s",
        item,
        stock_data[item],
    )
    logs.append(f"Added {item} ({qty})")


def remove_item(item):
    """Remove an item from the inventory."""
    try:
        del stock_data[item]
        logging.info("Item '%s' removed from inventory.", item)
    except KeyError:
        logging.warning("Item '%s' not found in inventory.", item)


def get_qty(item):
    """Get the quantity of an item."""
    return stock_data.get(item, 0)


def load_data(filename):
    """Load inventory data from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                name, qty = line.strip().split(',')
                stock_data[name] = int(qty)
        logging.info("Inventory data loaded successfully.")
    except FileNotFoundError:
        logging.error("File '%s' not found.", filename)
    except ValueError:
        logging.error(
            "File format incorrect — expected 'item,quantity' per line."
        )


def save_data(filename):
    """Save inventory data to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for item, qty in stock_data.items():
            file.write(f"{item},{qty}\n")
    logging.info("Inventory data saved successfully.")


def print_data():
    """Print all items and quantities in the inventory."""
    logging.info("Current inventory details:")
    for item, qty in stock_data.items():
        logging.info("Item: %s, Quantity: %s", item, qty)


def check_low_items(threshold):
    """Check and display items with quantity below a given threshold."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    if low_items:
        logging.warning(
            "Low-stock items (below %s): %s",
            threshold,
            low_items,
        )
    else:
        logging.info("No items below threshold.")


def main():
    """Main execution block for testing the inventory system."""
    add_item("Apples", 50)
    add_item("Oranges", 20)
    remove_item("Mangoes")  # Will trigger warning
    save_data("inventory.txt")
    load_data("inventory.txt")
    print_data()
    check_low_items(30)

    # Removed insecure eval() usage
    safe_dict = "{'msg': 'safe parse'}"
    parsed = ast.literal_eval(safe_dict)
    logging.info("Safe parsed data: %s", parsed)


if __name__ == "__main__":
    main()
