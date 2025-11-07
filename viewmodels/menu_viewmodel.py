class MenuViewModel:
    def __init__(self, id, name, price, category, image_url):
        self.id = id
        self.name = name
        self.price = float(price)
        self.category = category
        self.image_url = image_url

    @classmethod
    def from_model(cls, model):
        return cls(
            id=model.id,
            name=model.name,
            price=model.price,
            category=model.category,
            image_url=model.image_url
        )
