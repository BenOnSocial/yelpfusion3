from yelpfusion3.model.model import Model


class Category(Model):
    """
    Category title and alias pairs associated with this business.
    """

    alias: str
    """
    Alias of a category, when searching for business in certain categories, use alias rather than the title.
    """

    title: str
    """
    Title of a category for display purpose.
    """
