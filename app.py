from flask import Flask, render_template, request

app = Flask(__name__)

# Example recipe data
recipes_data = {
    'sniadanie': [
        {'name': 'Jajecznica z pomidorami', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'jajecznica.jpg', 'url': '/recipe/jajecznica', 'rating': 4},
        {'name': 'Owsianka z owocami', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'temp.jpg', 'url': '/recipe/owsianka', 'rating': 5},
        {'name': 'Kanapki z szynką', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'kanapki.jpg', 'url': '/recipe/kanapki', 'rating': 3},
        {'name': 'Omlet z warzywami', 'time': '15 min', 'difficulty': 'Średni', 'image': 'lazania.jpg', 'url': '/recipe/omlet', 'rating': 4},
        {'name': 'Placuszki bananowe', 'time': '20 min', 'difficulty': 'Średni', 'image': 'pizza.jpg', 'url': '/recipe/placuszki', 'rating': 5},
        {'name': 'Tosty francuskie', 'time': '15 min', 'difficulty': 'Średni', 'image': 'schabowy.jpg', 'url': '/recipe/tosty', 'rating': 4},
        {'name': 'Smoothie bowl', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'dynica.jpg', 'url': '/recipe/smoothie', 'rating': 5},
        {'name': 'Muffinki jajeczne', 'time': '25 min', 'difficulty': 'Średni', 'image': 'jajecznica.jpg', 'url': '/recipe/muffinki', 'rating': 4},
        {'name': 'Jogurt z granolą', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'schabowy.jpg', 'url': '/recipe/jogurt', 'rating': 4},
        {'name': 'Twarożek z rzodkiewką', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'kanapki.jpg', 'url': '/recipe/twarozek', 'rating': 3},
        {'name': 'Bagietka z pastą jajeczną', 'time': '15 min', 'difficulty': 'Łatwy', 'image': 'salatka.jpg', 'url': '/recipe/bagietka', 'rating': 4},
        {'name': 'Płatki kukurydziane z mlekiem', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'lazania.jpg', 'url': '/recipe/platki', 'rating': 3},
        {'name': 'Kanapki z awokado', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'muffinki.jpg', 'url': '/recipe/awokado', 'rating': 5},
        {'name': 'Budyń waniliowy', 'time': '15 min', 'difficulty': 'Łatwy', 'image': 'pizza.jpg', 'url': '/recipe/budyn', 'rating': 4},
        {'name': 'Omlet na słodko', 'time': '15 min', 'difficulty': 'Średni', 'image': 'schabowy.jpg', 'url': '/recipe/omlet_slodki', 'rating': 4},
    ],
    'obiad': [
        {'name': 'Jajecznica z pomidorami', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'jajecznica.jpg', 'url': '/recipe/jajecznica', 'rating': 4},
        {'name': 'Owsianka z owocami', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'temp.jpg', 'url': '/recipe/owsianka', 'rating': 5},
        {'name': 'Kanapki z szynką', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'kanapki.jpg', 'url': '/recipe/kanapki', 'rating': 3},
        {'name': 'Omlet z warzywami', 'time': '15 min', 'difficulty': 'Średni', 'image': 'lazania.jpg', 'url': '/recipe/omlet', 'rating': 4},
        {'name': 'Placuszki bananowe', 'time': '20 min', 'difficulty': 'Średni', 'image': 'pizza.jpg', 'url': '/recipe/placuszki', 'rating': 5},
        {'name': 'Tosty francuskie', 'time': '15 min', 'difficulty': 'Średni', 'image': 'schabowy.jpg', 'url': '/recipe/tosty', 'rating': 4},
        {'name': 'Smoothie bowl', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'dynica.jpg', 'url': '/recipe/smoothie', 'rating': 5},
        {'name': 'Muffinki jajeczne', 'time': '25 min', 'difficulty': 'Średni', 'image': 'jajecznica.jpg', 'url': '/recipe/muffinki', 'rating': 4},
        {'name': 'Jogurt z granolą', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'schabowy.jpg', 'url': '/recipe/jogurt', 'rating': 4},
        {'name': 'Twarożek z rzodkiewką', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'kanapki.jpg', 'url': '/recipe/twarozek', 'rating': 3},
        {'name': 'Bagietka z pastą jajeczną', 'time': '15 min', 'difficulty': 'Łatwy', 'image': 'salatka.jpg', 'url': '/recipe/bagietka', 'rating': 4},
        {'name': 'Płatki kukurydziane z mlekiem', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'lazania.jpg', 'url': '/recipe/platki', 'rating': 3},
        {'name': 'Kanapki z awokado', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'muffinki.jpg', 'url': '/recipe/awokado', 'rating': 5},
        {'name': 'Budyń waniliowy', 'time': '15 min', 'difficulty': 'Łatwy', 'image': 'pizza.jpg', 'url': '/recipe/budyn', 'rating': 4},
        {'name': 'Omlet na słodko', 'time': '15 min', 'difficulty': 'Średni', 'image': 'schabowy.jpg', 'url': '/recipe/omlet_slodki', 'rating': 4},
    ],
    'kolacja': [
        {'name': 'Jajecznica z pomidorami', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'jajecznica.jpg', 'url': '/recipe/jajecznica', 'rating': 4},
        {'name': 'Owsianka z owocami', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'temp.jpg', 'url': '/recipe/owsianka', 'rating': 5},
        {'name': 'Kanapki z szynką', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'kanapki.jpg', 'url': '/recipe/kanapki', 'rating': 3},
        {'name': 'Omlet z warzywami', 'time': '15 min', 'difficulty': 'Średni', 'image': 'lazania.jpg', 'url': '/recipe/omlet', 'rating': 4},
        {'name': 'Placuszki bananowe', 'time': '20 min', 'difficulty': 'Średni', 'image': 'pizza.jpg', 'url': '/recipe/placuszki', 'rating': 5},
        {'name': 'Tosty francuskie', 'time': '15 min', 'difficulty': 'Średni', 'image': 'schabowy.jpg', 'url': '/recipe/tosty', 'rating': 4},
        {'name': 'Smoothie bowl', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'dynica.jpg', 'url': '/recipe/smoothie', 'rating': 5},
        {'name': 'Muffinki jajeczne', 'time': '25 min', 'difficulty': 'Średni', 'image': 'jajecznica.jpg', 'url': '/recipe/muffinki', 'rating': 4},
        {'name': 'Jogurt z granolą', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'schabowy.jpg', 'url': '/recipe/jogurt', 'rating': 4},
        {'name': 'Twarożek z rzodkiewką', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'kanapki.jpg', 'url': '/recipe/twarozek', 'rating': 3},
        {'name': 'Bagietka z pastą jajeczną', 'time': '15 min', 'difficulty': 'Łatwy', 'image': 'salatka.jpg', 'url': '/recipe/bagietka', 'rating': 4},
        {'name': 'Płatki kukurydziane z mlekiem', 'time': '5 min', 'difficulty': 'Łatwy', 'image': 'lazania.jpg', 'url': '/recipe/platki', 'rating': 3},
        {'name': 'Kanapki z awokado', 'time': '10 min', 'difficulty': 'Łatwy', 'image': 'muffinki.jpg', 'url': '/recipe/awokado', 'rating': 5},
        {'name': 'Budyń waniliowy', 'time': '15 min', 'difficulty': 'Łatwy', 'image': 'pizza.jpg', 'url': '/recipe/budyn', 'rating': 4},
        {'name': 'Omlet na słodko', 'time': '15 min', 'difficulty': 'Średni', 'image': 'schabowy.jpg', 'url': '/recipe/omlet_slodki', 'rating': 4},
    ]
}


@app.route('/')
def index():
    return render_template('index.html')

# Dynamic category route
@app.route('/category/<category>')
def category(category):
    recipes = recipes_data.get(category, [])

    query = request.args.get('q', '').lower()
    if query:
        # filtruje przepisy po nazwie
        recipes = [r for r in recipes if query in r['name'].lower()]

    return render_template('category.html', category=category, recipes=recipes)


@app.route('/recipe.html')
def recipe():
    return render_template('recipe.html')

@app.route('/login.html')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
