from flask import Flask , jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) == 0):
        return jsonify({"message": "Product not found"})
    
    return jsonify({"product": productsFound[0]})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(new_product)
    return jsonify({"message": "Product added successfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) == 0):
        return jsonify({"message": "Product not found"})
    
    productsFound[0]['name'] = request.json['name']
    productsFound[0]['price'] = request.json['price']
    productsFound[0]['quantity'] = request.json['quantity']

    return jsonify({"message": "Product updated", "product": productsFound[0]})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) == 0):
        return jsonify({"message": "Product not found"})
    
    products.remove(productsFound[0])
    return jsonify({"message": "Product deleted", "products": products})

if __name__ == '__main__':
    app.run(debug=True, port=4000) 