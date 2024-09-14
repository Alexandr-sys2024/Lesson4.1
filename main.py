class Store:
    def __init__(self, name, address):
    # Инициализация магазина с названием, адресом и пустым ассортиментом товаров.
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для товаров


    def add_item(self, item_name, price):
    # Добавление товара в ассортимент.
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен по цене {price}.")


    def remove_item(self, item_name):
    #Удаление товара из ассортимента.
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён.")
        else:
            print(f"Товар '{item_name}' не найден.")


    def get_item_price(self, item_name):
    # Получение цены товара. Если товар отсутствует, возвращает None.
        return self.items.get(item_name, None)


    def update_item_price(self, item_name, new_price):
            # Обновление цены товара.
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")


    def __str__(self):
    # Возвращает строковое представление магазина.
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"

    def display_info(self):
        print(f"Магазин: {self.name}")
        print(f"Адрес: {self.address}")

            # Создание магазина
if __name__ == "__main__":
            golden_store = Store("Golden", "ул. Весенняя, д. 88")

            golden_store.add_item("Хлеб", 65)
            golden_store.add_item("Молоко", 76)
            golden_store.add_item("Сметана", 130)
            golden_store.add_item("Чай", 110)
            golden_store.add_item("Кофе", 399)
            golden_store.add_item("Шоколад", 139)
            golden_store.add_item("Сыр", 659)

            print("\nАссортимент после добавления товаров:")
            print(golden_store)





















