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
            magnet_store = Store("Магнит", "ул. Гагарина, д. 99")

            magnet_store.add_item("Помидоры", 230)
            magnet_store.add_item("Огурцы", 199)
            magnet_store.add_item("Капуста", 139)
            magnet_store.add_item("Морковь", 99)

            print("\nАссортимент после добавления товаров:")
            print(magnet_store)

            # Изменение 2 продуктов на новые

            magnet_store.remove_item("Капуста")
            magnet_store.add_item("Авокадо", 430)
            magnet_store.remove_item("Огурцы")
            magnet_store.add_item("Лук", 98)

            print("\nАссортимент после замены двух продуктов:")
            print(magnet_store)

            # Обновление цены для двух продуктов

            magnet_store.update_item_price("Авокадо", 455)
            magnet_store.update_item_price("Лук", 130)

            print("\nАссортимент после обновления цен:")
            print(magnet_store)






            
