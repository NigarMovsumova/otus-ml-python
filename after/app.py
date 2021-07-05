# from after.baskets import Basket
# 1. Импортирование всего модуля
# import baskets

# 2. импортирование модуля с псевдонимом (alias)
# import baskets as bskt

# 3. импортирование только того, что используем
from after.baskets import Basket

# 4. импорт всего - импортирование можем лишнее, нечитабельно, конфликт имен
# from after.baskets import *

print(__name__)

if __name__ == '__main__':
    basket = Basket()
    print(basket)

# print('testing imports')
