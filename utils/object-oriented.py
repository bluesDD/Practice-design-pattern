class Customers:
    def __init__(self, customers):
        self.customers = customers

    def add(self, customer):
        result = self.customers
        result.append(customer)
        return Customers(result)

if __name__ == "__main__":
    c = Customers(["jogn", "jughee"])
    c.add("Ken")
    print(c.customers)

    c2 = Customers(["jogn", "jughee"])
    c2.add("Ben")
    print(c2.customers)
