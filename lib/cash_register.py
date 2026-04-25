class CashRegister:
    def __init__(self, discount=0):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # ✅ correct discount math
        self.total = self.total * (1 - self.discount / 100)

        # remove last transaction
        if self.previous_transactions:
            self.previous_transactions.pop()

        # format like test expects (no .0)
        formatted_total = int(self.total) if self.total.is_integer() else round(self.total, 2)

        print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]

        self.items = []
        for t in self.previous_transactions:
            for _ in range(t["quantity"]):
                self.items.append(t["item"])

        if not self.items:
            self.total = 0.0
            