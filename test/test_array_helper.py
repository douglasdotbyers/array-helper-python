import pytest

from app.array_helper import ArrayHelper

class TestArrayHelper:
    def setup_method(self, method):
        self.__array_helper = ArrayHelper()

    def teardown_method(self, method):
        self.__array_helper = None

    def test_divide_with_none_array_raises_invalid_array_value_error(self):
        # Arrange.
        array = None
        parts = 3

        # Act.
        with pytest.raises(ValueError) as error:
            self.__array_helper.divide(array, parts)

        # Assert.
        assert "Invalid value for 'array' – 'None'" == str(error.value)

    def test_divide_with_none_parts_raises_invalid_parts_value_error(self):
        # Arrange.
        array = [1, 2, 3]
        parts = None

        # Act.
        with pytest.raises(ValueError) as error:
            self.__array_helper.divide(array, parts)

        # Assert.
        assert "Invalid value for 'parts' – 'None'" == str(error.value)

    def test_divide_with_zero_parts_raises_invalid_parts_value_error(self):
        # Arrange.
        array = [1, 2, 3]
        parts = 0

        # Act.
        with pytest.raises(ValueError) as error:
            self.__array_helper.divide(array, parts)

        # Assert.
        assert "Invalid value for 'parts' – '0'" == str(error.value)

    def test_divide_with_less_than_zero_parts_raises_invalid_parts_value_error(self):
        # Arrange.
        array = [1, 2, 3]
        parts = -1

        # Act.
        with pytest.raises(ValueError) as error:
            self.__array_helper.divide(array, parts)

        # Assert.
        assert "Invalid value for 'parts' – '-1'" == str(error.value)

    def test_divide_with_empty_array_and_3_parts_returns_array_with_3_parts(self):
        # Arrange.
        array           = []
        parts           = 3
        expected_result = [[], [], []]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result

    def test_divide_with_array_of_length_6_and_1_part_returns_array_with_1_part_and_no_remainder(self):
        # Arrange.
        array           = [1, 2, 3, 4, 5, 6]
        parts           = 1
        expected_result = [[1, 2, 3, 4, 5, 6]]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result

    def test_divide_with_array_of_length_6_and_2_parts_returns_array_with_2_equal_sized_parts_and_no_remainder(self):
        # Arrange.
        array           = [1, 2, 3, 4, 5, 6]
        parts           = 2
        expected_result = [[1, 2, 3], [4, 5, 6]]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result

    def test_divide_with_array_of_length_6_and_3_parts_returns_array_with_3_equal_sized_parts_and_no_remainder(self):
        # Arrange.
        array           = [1, 2, 3, 4, 5, 6]
        parts           = 3
        expected_result = [[1, 2], [3, 4], [5, 6]]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result

    def test_divide_with_array_of_length_6_and_4_parts_returns_array_with_3_equal_sized_parts_and_remainder_of_length_3(self):
        # Arrange.
        array           = [1, 2, 3, 4, 5, 6]
        parts           = 4
        expected_result = [[1], [2], [3], [4, 5, 6]]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result

    def test_divide_with_array_of_length_6_and_5_parts_returns_array_with_4_equal_sized_parts_and_remainder_of_length_2(self):
        # Arrange.
        array           = [1, 2, 3, 4, 5, 6]
        parts           = 5
        expected_result = [[1], [2], [3], [4], [5, 6]]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result

    def test_divide_with_array_of_length_6_and_6_parts_returns_array_with_6_equal_sized_parts_and_no_remainder(self):
        # Arrange.
        array           = [1, 2, 3, 4, 5, 6]
        parts           = 6
        expected_result = [[1], [2], [3], [4], [5], [6]]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result

    def test_divide_with_array_of_length_5_and_3_parts_returns_array_with_2_equal_sized_parts_and_remainder_of_length_1(self):
        # Arrange.
        array           = [1, 2, 3, 4, 5]
        parts           = 3
        expected_result = [[1, 2], [3, 4], [5]]

        # Act.
        actual_result = self.__array_helper.divide(array, parts)

        # Assert.
        assert expected_result == actual_result
