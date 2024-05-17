from unittest.mock import Mock

from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        bun_mock1 = Mock()
        bun_mock1.get_name.return_value = "black bun"
        bun_mock1.get_price.return_value = 100

        bun_mock2 = Mock()
        bun_mock2.get_name.return_value = "white bun"
        bun_mock2.get_price.return_value = 200

        bun_mock3 = Mock()
        bun_mock3.get_name.return_value = "red bun"
        bun_mock3.get_price.return_value = 300

        db = Database()
        db.buns = [bun_mock1,
                   bun_mock2,
                   bun_mock3
                   ]

        assert db.available_buns() == [bun_mock1,
                                       bun_mock2,
                                       bun_mock3
                                       ]

    def test_available_ingredients(self):

        ingredient_mock1 = Mock()
        ingredient_mock1.get_type.return_value = "соус"
        ingredient_mock1.get_name.return_value = "hot sauce"
        ingredient_mock1.get_price.return_value = 100

        ingredient_mock2 = Mock()
        ingredient_mock2.get_type.return_value = "соус"
        ingredient_mock2.get_name.return_value = "sour cream"
        ingredient_mock2.get_price.return_value = 200

        ingredient_mock3 = Mock()
        ingredient_mock3.get_type.return_value = "соус"
        ingredient_mock3.get_name.return_value = "chili sauce"
        ingredient_mock3.get_price.return_value = 300

        ingredient_mock4 = Mock()
        ingredient_mock4.get_type.return_value = "начинка"
        ingredient_mock4.get_name.return_value = "cutlet"
        ingredient_mock4.get_price.return_value = 100

        ingredient_mock5 = Mock()
        ingredient_mock5.get_type.return_value = "начинка"
        ingredient_mock5.get_name.return_value = "dinosaur"
        ingredient_mock5.get_price.return_value = 200

        ingredient_mock6 = Mock()
        ingredient_mock6.get_type.return_value = "начинка"
        ingredient_mock6.get_name.return_value = "sausage"
        ingredient_mock6.get_price.return_value = 300

        exp_ingredients = [
            ingredient_mock1,
            ingredient_mock2,
            ingredient_mock3,
            ingredient_mock4,
            ingredient_mock5,
            ingredient_mock6
        ]

        db = Database()
        db.ingredients = [
            ingredient_mock1,
            ingredient_mock2,
            ingredient_mock3,
            ingredient_mock4,
            ingredient_mock5,
            ingredient_mock6
        ]

        assert db.available_ingredients() == exp_ingredients
