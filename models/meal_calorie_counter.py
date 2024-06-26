from models.meal_ingredient import MealIngredient
from datasource.exceptions import FileIOException
from datasource.recipe_dao import RecipeDao
from ui.text.styler import Styler


class MealCalorieCounter:
    recipe_dao: RecipeDao
    current_file_name: str
    ingredients: dict
    total_calories: int

    def __init__(self) -> None:
        self.recipe_dao = RecipeDao()
        self.current_file_name = "Nieuw Recept"
        self.ingredients = {}
        self.total_calories = 0

    def add_ingredient_to_meal(self, ingredient: str, weight: float, calories_per_100g: int) -> None:
        self.ingredients.update({ingredient: MealIngredient(ingredient, weight, calories_per_100g)})

    def display_recipe_ingredients(self) -> None:
        total_calories = 0
        for key in self.ingredients:
            ingredient = self.ingredients[key]
            Styler.success(f"{ingredient.get_name().capitalize()}: "
                           f"{ingredient.get_calories_in_portion()} kcal voor "
                           f"{ingredient.get_weight()}g")
            total_calories += ingredient.get_calories_in_portion()
        self.total_calories = total_calories
        Styler.success(f"\nTotale calorieën: {self.get_total_calories()}\n")

    def get_total_calories(self) -> int:
        return self.total_calories

    def get_current_file_name(self) -> str:
        return self.current_file_name

    def save_recipe(self, file_name: str) -> None:
        self.current_file_name = file_name
        self.recipe_dao.save_recipe(file_name, self.ingredients)

    def load_recipe(self, file_name: str) -> None:
        try:
            self.current_file_name = file_name
            recipe = self.recipe_dao.load_recipe(file_name)
            self.ingredients = recipe
        except FileIOException:
            raise

    def delete_recipe(self, file_name: str) -> None:
        try:
            self.current_file_name = "Nieuw Recept"
            self.ingredients = {}
            self.total_calories = 0
            self.recipe_dao.delete_recipe(file_name)
        except FileIOException:
            raise

    def clear_recipe(self) -> None:
        self.ingredients = {}
        self.total_calories = 0

    def calculate_total_meal_weight(self) -> float:
        total_meal_weight = 0
        for key in self.ingredients:
            total_meal_weight += self.ingredients[key].get_weight()
        return total_meal_weight

    def calculate_calories_in_portion(self, total_weight, portion_weight) -> int:
        return int((portion_weight * self.total_calories) / total_weight)
