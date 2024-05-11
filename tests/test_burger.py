from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_mock_2]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_mock_2, ingredient_mock_1]

    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 5.5
        burger.bun = bun_mock

        ingredient_mock_1 = Mock()
        ingredient_mock_1.get_price.return_value = 1.5
        ingredient_mock_2 = Mock()
        ingredient_mock_2.get_price.return_value = 2.75
        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]

        exp_price = bun_mock.get_price() * 2 + ingredient_mock_1.get_price() + ingredient_mock_2.get_price()
        assert burger.get_price() == exp_price

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Чёрная булочка"
        bun_mock.get_price.return_value = 5.5
        burger.bun = bun_mock

        ingredient_mock_1 = Mock()
        ingredient_mock_1.get_type.return_value = "начинка"
        ingredient_mock_1.get_name.return_value = "Котлета"
        ingredient_mock_1.get_price.return_value = 1.5
        burger.ingredients = [ingredient_mock_1]

        receipt = burger.get_receipt()

        assert bun_mock.get_name.return_value in receipt
        assert ingredient_mock_1.get_type.return_value in receipt
        assert ingredient_mock_1.get_name.return_value in receipt
        assert str(bun_mock.get_price() * 2 + ingredient_mock_1.get_price()) in receipt
