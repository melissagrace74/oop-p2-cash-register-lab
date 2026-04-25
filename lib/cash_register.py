class CashRegister:
    def __init__(self, discount=0):  # Constructor accepting an optional discount parameter
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0  # Initial total is 0
        self.items = []  # Initialize empty list to store item names
        self.previous_transactions = []  # Store transactions to support voiding last transaction

    def add_item(self, item, price, quantity=1):
        """
        Adds item(s) to the register. If quantity > 1, it adds that many of the item.
        Updates the total accordingly.
        """
        self.total += price * quantity

        # Add item to the items list
        for _ in range(quantity):
            self.items.append(item)

        # Record transaction for possible voiding later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Applies discount to the total if a valid discount is set."""
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply discount by reducing the total
        self.total = self.total * (1 - self.discount / 100)

        # Remove the last transaction to reflect discount
        if self.previous_transactions:
            self.previous_transactions.pop()

        # Format total (removes decimals if it's a whole number)
        formatted_total = int(self.total) if self.total.is_integer() else round(self.total, 2)

        print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        """Removes the most recent transaction and updates the total accordingly."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]

        # Rebuild the items list after removing the last transaction
        self.items = []
        for t in self.previous_transactions:
            for _ in range(t["quantity"]):
                self.items.append(t["item"])

        if not self.items:
            self.total = 0.0
            