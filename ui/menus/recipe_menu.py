from models.meal_calorie_counter import MealCalorieCounter
from ui.input.input_handler import InputHandler
from ui.menus.exceptions import BackException, ExitException
from ui.console.console_operations import ConsoleOperations
from ui.text.color_string import ColorString
from ui.text.styler import Styler


class RecipeMenu:
    calorie_counter = MealCalorieCounter()

    @staticmethod
    def display_options() -> None:
        Styler.print_white("Recept Volgen")
        Styler.print_blue("--={*}=--")
        Styler.print_gray("Voer de ingrediënten van je recept in, samen")
        Styler.print_gray("met het gewicht van het ingrediënt en de hoeveelheid")
        Styler.print_gray("calorieën per 100g. Het totale aantal")
        Styler.print_gray("calorieën in dit recept wordt weergegeven na")
        Styler.print_gray("het invoeren van je ingrediënt.")
        Styler.print_blue("--={*}=--")
        Styler.print_white("Wat wil je doen?")
        Styler.print_blue("--={*}=--")
        Styler.print_cyan("[1]: Voeg een ingrediënt toe")
        Styler.print_cyan("[2]: Bewaar dit recept (Niet geïmplementeerd)")
        Styler.print_cyan("[3]: Laad een recept (Niet geïmplementeerd)")
        Styler.print_blue("--={*}=--\n")

    @staticmethod
    def start_recipe_menu() -> None:
        while True:
            try:
                RecipeMenu.display_options()
                RecipeMenu.calorie_counter.display_recipe_ingredients()
                user_input = InputHandler.prompt_string(
                    ColorString.blue_string("Voer een van de bovenstaande opties in: "))
                RecipeMenu.handle_user_input(user_input)
            except BackException:
                ConsoleOperations.clear()
                break
            except ExitException:
                raise

    @staticmethod
    def handle_user_input(user_input: str) -> None:
        match user_input:
            case "1":
                RecipeMenu.add_ingredient()
            case "2":
                ConsoleOperations.clear()
                Styler.warning("Niet geïmplementeerd\n")
            case "3":
                ConsoleOperations.clear()
                Styler.warning("Niet geïmplementeerd\n")
            case _:
                ConsoleOperations.clear()
                Styler.warning("Voer een geldige optie in\n")

    @staticmethod
    def add_ingredient():
        try:
            ingredient = InputHandler.prompt_string(
                ColorString.blue_string("\nVoer de naam van het ingrediënt in: "))
            weight = InputHandler.prompt_float(
                ColorString.blue_string("Voer het gewicht van het ingrediënt in (in gram): "))
            calories_per_100g = InputHandler.prompt_int(
                ColorString.blue_string("Voer het aantal calorieën per 100g van het ingrediënt in: "))
            RecipeMenu.calorie_counter.add_ingredient_to_meal(ingredient, weight, calories_per_100g)
            ConsoleOperations.clear()
        except BackException:
            raise
        except ExitException:
            raise
