"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Vehicles, Starships, Fav
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
#ENDPOINTS

#Devuelve todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    #hacemos la consulta para todos los usuarios registrados
    users_querys = User.query.all()
    #se mapea para convertir el array devuelto a un array de objetos
    results = list(map(lambda user: user.serialize(), users_querys))
    #print(results)

    #si no hay registros, respondemos que no hay usuarios registrados y no sigue leyendo el código
    if results == []:
        return jsonify({"msg": "No hay usuarios registrados"}), 404
    
    #retornamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Hola, estos son los usuarios", 
        "results": results
    }

#Devuelve un usuario por id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    #hacemos la consulta filtrando el usuario por id
    user_query = User.query.filter_by(id = user_id).first()

    #si no hay registro de usuario por ese id, devuelve el msj de error y no sigue leyendo el código
    if user_query is None:
        return jsonify({"msg": "El usuario con id: " + str(user_id) + " no existe"}), 404
    
    #retornamos una respuesta con el resultado de la consulta
    response_body = {
        "msg": "Hola, este es el usuario", 
        "result": user_query.serialize()
    }

    return jsonify(response_body), 200

#Devuelve todos los personajes
@app.route('/people', methods=['GET'])
def get_people():
    #hacemos la consulta para todos los personajes registrados
    people_querys = People.query.all()
    #se mapea para convertir el array devuelto a un array de objetos
    results = list(map(lambda people: people.serialize(), people_querys))
    #print(results)

    #si no hay registros, respondemos que no hay personajes registrados y no sigue leyendo el código
    if results == []:
        return jsonify({"msg": "No hay personajes registrados"}), 404
    
    #retornamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Hola, estos son los personajes", 
        "results": results
    }

    return jsonify(response_body), 200

#Devuelve un personaje por id
@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_person(people_id):
    #hacemos la consulta filtrando el personaje por id
    person_query = People.query.filter_by(id = people_id).first()

    #si no hay registro de personaje por ese id, devuelve el msj de error y no sigue leyendo el código
    if person_query is None:
        return jsonify({"msg": "El personaje con id: " + str(people_id) + " no existe"}), 404
    
    #retornamos una respuesta con el resultado de la consulta
    response_body = {
        "msg": "Hola, este es el personaje", 
        "result": person_query.serialize()
    }

    return jsonify(response_body), 200

#Devuelve todos los planetas
@app.route('/planets', methods=['GET'])
def get_planets():
    #hacemos la consulta para todos los planetas registrados
    planets_querys = Planets.query.all()
    #se mapea para convertir el array devuelto a un array de objetos
    results = list(map(lambda planet: planet.serialize(), planets_querys))
    #print(results)

    #si no hay registros, respondemos que no hay planetas registrados y no sigue leyendo el código
    if results == []:
        return jsonify({"msg": "No hay planetas registrados"}), 404
    
    #retornamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Hola, estos son los planetas", 
        "results": results
    }

    return jsonify(response_body), 200

#Devuelve un planeta por id
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    #hacemos la consulta filtrando el planeta por id
    planet_query = Planets.query.filter_by(id = planet_id).first()

    #si no hay registro de planeta por ese id, devuelve el msj de error y no sigue leyendo el código
    if planet_query is None:
        return jsonify({"msg": "El planeta con id: " + str(planet_id) + " no existe"}), 404
    
    #retornamos una respuesta con el resultado de la consulta
    response_body = {
        "msg": "Hola, este es el planeta", 
        "result": planet_query.serialize()
    }

    return jsonify(response_body), 200

#Devuelve todos los vehículos
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    #hacemos la consulta para todos los vehículos registrados
    vehicles_querys = Vehicles.query.all()
    #se mapea para convertir el array devuelto a un array de objetos
    results = list(map(lambda vehicle: vehicle.serialize(), vehicles_querys))
    #print(results)

    #si no hay registros, respondemos que no hay vehículos registrados y no sigue leyendo el código
    if results == []:
        return jsonify({"msg": "No hay vehículos registrados"}), 404
    
    #retornamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Hola, estos son los vehículos", 
        "results": results
    }

    return jsonify(response_body), 200

#Devuelve un vehículo por id
@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_one_vehicle(vehicle_id):
    #hacemos la consulta filtrando el vehículo por id
    vehicle_query = Vehicles.query.filter_by(id = vehicle_id).first()

    #si no hay registro de vehículo por ese id, devuelve el msj de error y no sigue leyendo el código
    if vehicle_query is None:
        return jsonify({"msg": "El vehículo con id: " + str(vehicle_id) + " no existe"}), 404
    
    #retornamos una respuesta con el resultado de la consulta
    response_body = {
        "msg": "Hola, este es el vehículo", 
        "result": vehicle_query.serialize()
    }

    return jsonify(response_body), 200

#Devuelve todas las naves
@app.route('/starships', methods=['GET'])
def get_starships():
    #hacemos la consulta para todas las naves registradas
    starships_querys = Starships.query.all()
    #se mapea para convertir el array devuelto a un array de objetos
    results = list(map(lambda starship: starship.serialize(), starships_querys))
    #print(results)

    #si no hay registros, respondemos que no hay naves registradas y no sigue leyendo el código
    if results == []:
        return jsonify({"msg": "No hay naves registradas"}), 404
    
    #retornamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Hola, estas son las naves", 
        "results": results
    }

    return jsonify(response_body), 200

#Devuelve una nave por id
@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_one_starship(starship_id):
    #hacemos la consulta filtrando la nave por id
    starship_query = Starships.query.filter_by(id = starship_id).first()

    #si no hay registro de nave por ese id, devuelve el msj de error y no sigue leyendo el código
    if starship_query is None:
        return jsonify({"msg": "La nave con id: " + str(starship_id) + " no existe"}), 404
    
    #retornamos una respuesta con el resultado de la consulta
    response_body = {
        "msg": "Hola, esta es la nave", 
        "result": starship_query.serialize()
    }

    return jsonify(response_body), 200

#Devuelve los favoritos de un usuario
@app.route('/users/<int:user_id>/fav', methods=['GET'])
def get_user_fav(user_id):
    #hacemos la consulta para los favoritos registrados por el usuario
    favs_querys = Fav.query.filter_by(id = user_id)
    #se mapea para convertir el array devuelto a un array de objetos
    results = list(map(lambda fav: fav.serialize(), favs_querys))
    #si el usuario no existe, respondemos que no está registrado y no sigue leyendo el código
    user_query = User.query.filter_by(id = user_id).first()
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    #si no hay registros, respondemos que no hay favoritos registrados y no sigue leyendo el código
    if results == []:
        return jsonify({"msg": "No hay favoritos registrados"}), 404
    
    #retornamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Hola, estos son los favoritos", 
        "results": results
    }

    return jsonify(response_body), 200
#agregar un planeta como favorito
@app.route('/fav/planets/<int:planeta_id>', methods=['POST'])
def add_planet_fav(planeta_id):
    
    request_body = request.get_json(force=True)
    #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["user_id"]).first()
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    
    new_planet_fav = Fav(user_id = request_body["user_id"], planets_id = planeta_id)
    planet_query = Planets.query.filter_by(id = planeta_id).first()
    if planet_query is None:
        return jsonify({"msg": "El planeta no existe"}), 404

    db.session.add(new_planet_fav)
    db.session.commit()

    

    request_body = {
        "msg": "Planeta agregado a favoritos"
    }
    return jsonify(request_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
