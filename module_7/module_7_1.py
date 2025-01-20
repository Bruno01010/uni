class Product:
    def __init__(self, name, weight, category):
        self.name = name                  # Название продукта (строка)
        self.weight = weight              # Общий вес товара (дробное число)
        self.category = category          # Категория товара (строка)

    def __str__(self):
        # Возвращает строку в формате '<название>, <вес>, <категория>'
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = '../products.txt'  # Инкапсулированный атрибут для имени файла с продуктами

    def get_products(self):
        """Считывает всю информацию из файла и возвращает единую строку со всеми товарами."""
        try:
            with open(self.__file_name, 'r') as file:  # Открываем файл для чтения
                return file.read()  # Считываем весь текст из файла и возвращаем его
        except FileNotFoundError:
            return ''  # Если файл не найден, возвращаем пустую строку

    def add(self, *products):
        """Добавляет продукты в файл, если их еще нет."""
        existing_products = self.get_products()  # Получаем существующие продукты из файла
        with open(self.__file_name, 'a') as file:  # Открываем файл для добавления новых продуктов
            for product in products:  # Проходим по всем переданным продуктам
                if isinstance(product, Product):  # Проверяем, является ли объект продуктом
                    # Проверяем, есть ли уже этот продукт в файле
                    if product.name in existing_products:
                        print(f'Продукт {product.name} уже есть в магазине')  # Продукт уже существует
                    else:
                        file.write(f'{product}\n')  # Записываем продукт в файл с новой строки


# Пример использования классов
s1 = Shop()  # Создаем объект магазина
p1 = Product('Potato', 50.5, 'Vegetables')  # Создаем объект продукта с названием "Potato", весом 50.5 и категорией "Vegetables"
p2 = Product('Spaghetti', 3.4, 'Groceries')  # Создаем еще один продукт с названием "Spaghetti", весом 3.4 и категорией "Groceries"
p3 = Product('Potato', 5.5, 'Vegetables')  # Создаем продукт с тем же названием "Potato", но с другим весом

print(p2)  # Выводим строковое представление продукта p2

s1.add(p1, p2, p3)  # Добавляем продукты p1, p2 и p3 в магазин

print(s1.get_products())  # Выводим все продукты из магазина