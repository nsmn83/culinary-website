import os
import json
from app import app, db, Recipe, Ingredient, Step

RECIPES_DIR = os.path.join(os.path.dirname(__file__), "recipes")

def read_recipe(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if Recipe.query.filter_by(name=data["name"]).first():
        return

    new_recipe = Recipe(
        name=data["name"],
        category=data.get("category", "obiad"),
        time=data.get("time", 30),
        difficulty=data.get("difficulty", "Średni"),
        portions=data.get("portions", 2),
        image=data.get("image_filename", "placeholder.jpg")
    )
    db.session.add(new_recipe)
    db.session.commit()

    for ingredient in data.get("ingredients", []):
        new_ingredient = Ingredient(text=ingredient, recipe=new_recipe)
        db.session.add(new_ingredient)

    for step in data.get("steps", []):
        new_step = Step(text=step, recipe=new_recipe)
        db.session.add(new_step)

    db.session.commit()

def import_recipes():
    for filename in os.listdir(RECIPES_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(RECIPES_DIR, filename)
            read_recipe(file_path)

if __name__ == "__main__":
    with app.app_context():
        import_recipes()
        print("Recipes loaded into database!.")