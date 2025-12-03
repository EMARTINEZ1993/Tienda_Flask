from flask import Flask, render_template, session, redirect, url_for
from products import products
import os 

app=Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "clave_secreta_para_sesiones")

#crear Funcion para cargar o crear las categorias
def get_categories():
    return sorted(set(p["category"] for p in products))

@app.route("/")
def index():
    categories = get_categories()
    return render_template("index.html", products=products, categories=categories)


#Crear ruta y funcion para acceder a la pagina de categorias
@app.route("/categoria/<category>")

def categoria(category):
    filtered = [p for p in products if p["category"].lower() == category.lower()]
    categories = get_categories()
    if not filtered:
        return render_template("categoria.html", products=[], category=category, categories=categories, empty=True)
    return render_template("categoria.html", products=filtered, category=category, categories=categories, empty=False)


#Crear ruta y funcion para acceder a la pagina de detalle de productos
@app.route("/producto/<int:producto_id>")
def product_detail(producto_id):
    product = next((p for p in products if p["id"] == producto_id), None)
    categories = get_categories()
    if not product:
        return "Producto no encontrado", 404
    return render_template("product_detail.html", product=product, categories=categories)


@app.route("/agregar/<int:producto_id>")
def add_to_cart(producto_id):
    session.setdefault("cart", [])
    session["cart"].append(producto_id)
    session.modified = True
    return redirect(url_for("cart"))

@app.route("/carrito")
def cart():
    cart_ids = session.get("cart", [])
    categories = get_categories()
    items = [p for p in products if p["id"] in cart_ids]
    return render_template("cart.html", items=items, categories=categories)

@app.route("/vaciar")
def empty_cart():
    session["cart"] = []
    return redirect(url_for("cart"))

#Quedar al final
if __name__ == "__main__":
    app.run(debug=True)