import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("filling", "cutlet", 100),
            ("sauce", "hot sauce", 200),
            ("bun", "red bun", 300),

        ]
    )
    def test_get_price(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_price() == price

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("filling", "cutlet", 100),
            ("sauce", "hot sauce", 200),
            ("bun", "red bun", 300),

        ]
    )
    def test_get_name(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_name() == name

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("filling", "cutlet", 100),
            ("sauce", "hot sauce", 200),
            ("bun", "red bun", 300),

        ]
    )
    def test_get_type(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_type() == ingredient_type
