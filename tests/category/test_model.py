from typing import Dict

from yelpfusion3.category.model import Category, CategoryDetails


class TestCategory:
    test_data: Dict = {
        "alias": "bicycles",
        "title": "Bicycles",
        "parent_aliases": [],
        "country_whitelist": ["CZ", "DK", "PL", "PT"],
        "country_blacklist": [],
    }

    def test_deserialization(self) -> None:
        category: Category = Category(**self.test_data)

        assert category.alias == "bicycles"
        assert category.title == "Bicycles"
        assert not category.parent_aliases
        assert set(category.country_whitelist) == {"CZ", "DK", "PL", "PT"}
        assert not category.country_blacklist


class TestCategoryDetails:
    test_data: Dict = {
        "category": {
            "alias": "bicycles",
            "title": "Bicycles",
            "parent_aliases": [],
            "country_whitelist": ["CZ", "DK", "PL", "PT"],
            "country_blacklist": [],
        }
    }

    def test_deserialization(self) -> None:
        category_details: CategoryDetails = CategoryDetails(**self.test_data)

        assert category_details.category.alias == "bicycles"
        assert category_details.category.title == "Bicycles"
        assert not category_details.category.parent_aliases
        assert set(category_details.category.country_whitelist) == {"CZ", "DK", "PL", "PT"}
        assert not category_details.category.country_blacklist
