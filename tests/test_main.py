from src.main import (
    Calculate,
)


class TestMain:
    def test_calculate_add_two_numbers(
        self,
    ):
        assert (
            Calculate.add(
                1,
                2,
            )
            == 3
        )
