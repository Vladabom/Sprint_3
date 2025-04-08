import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def nubmer_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
            
        self.__name_items.append(name)
        self.__number_items += 1
    
    def delete_item_for_cheque(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в товарном справочнике')
            
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = list()
        
        for i in self.__name_items:
            total.append(self.__item_price.get(i))
        
        total_amount = sum(total)
        
        if len(total) > 10:
            total_amount -= total_amount * 0.1
        
        return total_amount
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = list()
        total = list()

        for i in self.__name_items:
            if self.__tax_rate.get(i) == 20:
                twenty_percent_tax.append(i)

        for i in twenty_percent_tax:
            total.append(self.__item_price.get(i))

        total_twenty_percent_tax = sum(total)

        if len(twenty_percent_tax) > 10:
            total_twenty_percent_tax -= total_twenty_percent_tax * 0.1

        total_twenty_percent_tax *= 0.2

        return total_twenty_percent_tax
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = list()
        total = list()
        
        for i in self.__name_items:
            if self.__tax_rate.get(i) == 10:
                ten_percent_tax.append(i)

        for i in ten_percent_tax:
            total.append(self.__item_price.get(i))

        total_ten_percent_tax = sum(total)

        if len(ten_percent_tax) > 10:
            total_ten_percent_tax -= ten_percent_tax * 0.1

        total_ten_percent_tax *= 0.1

        return total_ten_percent_tax
    
    def total_tax(self):
        total_tax = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

        return total_tax
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"') 
        
        return print(f'+7{telephone_number}')
    
    @staticmethod
    def get_date_and_time():
        date_and_time = list() 
        now = datetime.datetime.now()  

        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        
        for item in date:
            name = item[0]
            value = item[1](now)  
            date_and_time.append(f"{name}: {value}")

        return print(date_and_time)