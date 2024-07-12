class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def drive(self, distance):
        cost_per_km = 10
        self.price -= cost_per_km * distance
        if self.price < 0:
            self.price = 0

    def __str__(self):
        return f"Car(model={self.model}, year={self.year}, price={self.price})"

    @property
    def category(self):
        if self.price > 10_000_000:
            return "елітне"
        elif 2_000_000 <= self.price <= 10_000_000:
            return "середнячок"
        else:
            return "економ"


if __name__ == "__main__":
    car = Car("Dodge 2", 2020, 10_000_000)
    print(car)
    print(car.category)
    car.drive(100)
    print(car)
    print(car.category)