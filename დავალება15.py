class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"


class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "გასაყიდი"

    def sell_house(self, buyer, loan_amount=0):
        if loan_amount > 0:
            self.owner.deposit += self.price
            buyer.loan += loan_amount
            self.owner = buyer
            self.status = "გაყიდული სესხით"
            print(f"{self.ID} ბინა გაყიდულია სესხით. ახალი მეპატრონეა: {buyer.name}, სესხის ოდენობა: {loan_amount}")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდული"
            print(f"{self.ID} ბინა გაყიდულია. ახალი მეპატრონეა: {buyer.name}")


seller = Person("გამყიდველი")
buyer = Person("მყიდველი")

house = House("123456", 50000, seller)

print(seller)
print(buyer)
print(house.status)

house.sell_house(buyer)

house = House("123456", 50000, seller)  # ახალი ობიექტი იგივე ID-ით
house.sell_house(buyer, loan_amount=20000)

print(seller)
print(buyer)
print(house.status)
