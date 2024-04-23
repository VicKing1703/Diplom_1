import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("чёрная булочка", 100),
            ("white bun", 33.55),
            ("red bun", 300),
        ]
    )
    def test_bun_string_name(self, name, price):
        assert Bun(name, price).get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("чёрная булочка", 100),
            ("white bun", 33.55),
            ("red bun", 300),
        ]
    )
    def test_bun_float_price(self, name, price):
        assert Bun(name, price).get_price() == price
