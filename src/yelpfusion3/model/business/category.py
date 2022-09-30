from pydantic import BaseModel


class Category(BaseModel):
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
