class Store:
    def __init__(self, name, address):
        """Инициализация магазина с названием, адресом и пустым ассортиментом товаров."""
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для товаров

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен по цене {price}.")

    def remove_item(self, item_name):
        """Удаление товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_item_price(self, item_name):
        """Получение цены товара. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Обновление цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def __str__(self):
        """Возвращает строковое представление магазина."""
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"


# Пример использования
if __name__ == "__main__":
    # Создание магазина
    semerochka_store = Store("Семерочка", "ул. Заречная, д. 77")

    # Добавление 5 продуктов
    semerochka_store.add_item("Хлеб", 1.2)
    semerochka_store.add_item("Молоко", 0.9)
    semerochka_store.add_item("Яблоки", 2.5)
    semerochka_store.add_item("Сахар", 1.0)
    semerochka_store.add_item("Картофель", 0.7)

    print("\nАссортимент после добавления товаров:")
    print(semerochka_store)

    # Изменение 2 продуктов на новые
    semerochka_store.remove_item("Хлеб")
    semerochka_store.add_item("Булка", 1.3)
    semerochka_store.remove_item("Сахар")
    semerochka_store.add_item("Соль", 0.8)

    print("\nАссортимент после замены двух продуктов:")
    print(semerochka_store)

    # Обновление цены для двух продуктов
    semerochka_store.update_item_price("Яблоки", 3.0)
    semerochka_store.update_item_price("Картофель", 0.9)

    print("\nАссортимент после обновления цен:")
    print(semerochka_store)

    semerochka_store.remove_item("Булка")
    semerochka_store.add_item("Пицца", 1.5)
    semerochka_store.remove_item("Соль")
    semerochka_store.add_item("Перец", 0.9)

    print("\nАссортимент после замены двух продуктов:")
    print(semerochka_store)

    def __str__(self):
        """Возвращает строковое представление магазина."""
        return (f"Магазин: {"Семерочка"}, Адрес: {"ул. Заречная, д. 77"}, "
                f"Товары: {'Молоко': 0.9, 'Яблоки': 3.0, 'Картофель': 0.9, 'Питца': 1.5, 'Перец': 0.9}")







