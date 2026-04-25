class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []

        # validate discount
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

    # -------------------------
    # ADD ITEM
    # -------------------------
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        # tests expect a flat list of item names
        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append(price * quantity)

    # -------------------------
    # APPLY DISCOUNT
    # -------------------------
    def apply_discount(self):
        # key fix: only allow discount if total > 0
        if self.total == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        # format output exactly as tests expect
        if self.total == int(self.total):
            total_display = int(self.total)
        else:
            total_display = self.total

        print(f"After the discount, the total comes to ${total_display}.")

    # -------------------------
    # VOID LAST TRANSACTION
    # -------------------------
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.total -= last
        