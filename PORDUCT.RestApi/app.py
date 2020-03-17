from flask import Flask, jsonify, request
app = Flask(__name__)

from products import products

@app.route('/hola')
def hola():
    return jsonify({"mansage": "holo!"})

@app.route('/products')
def getproducts():
    return jsonify({"products": products, "mensage": "products list"})


@app.route('/products/<string:product_name>')
def getproduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):   
        return jsonify({"product": productsFound[0]})
    return jsonify({"mensaje": "producto no encontrado"})


@app.route('/products', methods=['POST'])
def addproduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"mensaje":"product added succesfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "mensaje":"product updated",
            "product": productFound[0]
        })
    return jsonify({"mensaje":"product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteproduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound)> 0):
        products.remove(productFound[0])
        return jsonify({
            "mensaje": "product deleted", "products": products
        })
    return jsonify({"mensaje": "product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)