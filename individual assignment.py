from collections import deque
# Stack for undoing stock movements
class StockMovement:
    def __init__(self, item, quantity, action):
        self.item = item
        self.quantity = quantity
        self.action = action  # 'add' or 'remove'

undo_stack = []

# Queue for incoming orders
order_queue = deque()

# Dictionary for available stock
available_stock = {
    'item_a': 50,
    'item_b': 30,
    'item_c': 20
}

# Function to add stock
def add_stock(item, quantity):
    if item in available_stock:
        available_stock[item] += quantity
    else:
        available_stock[item] = quantity
    undo_stack.append(StockMovement(item, quantity, 'remove'))  # For undo

# Function to remove stock
def remove_stock(item, quantity):
    if item in available_stock and available_stock[item] >= quantity:
        available_stock[item] -= quantity
        undo_stack.append(StockMovement(item, quantity, 'add'))  # For undo
    else:
        print("Not enough stock to remove")

# Function to undo the last stock movement
def undo_last_movement():
    if undo_stack:
        last_movement = undo_stack.pop()
        if last_movement.action == 'add':
            add_stock(last_movement.item, last_movement.quantity)
        else:
            remove_stock(last_movement.item, last_movement.quantity)

# Function to add an order to the queue
def add_order(order):
    order_queue.append(order)

# Function to process an incoming order
def process_order():
    if order_queue:
        order = order_queue.popleft()
        item, quantity = order
        remove_stock(item, quantity)

# Example Usage
add_stock('item_a', 10)         # Add stock
remove_stock('item_b', 5)       # Remove stock
undo_last_movement()             # Undo last removal
add_order(('item_c', 5))         # Add order
process_order()                  # Process the order

# Print available stock
print(available_stock)
