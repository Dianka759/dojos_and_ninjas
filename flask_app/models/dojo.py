from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE dojo.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojo =cls(results[0])

        for ninja in results:
            dojo_location = cls(ninja)
            ninja_data = {
                "id":ninja["ninja.id"],
                "dojo_id":ninja["dojo_id"],
                "first_name":ninja["first_name"],
                "last_name":ninja["last_name"],
                "age":ninja["age"],
                "created_at":ninja["ninjas.created_at"],
                "updated_at":ninja["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        all_dojos = []
        for dojo in dojos_from_db:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        dojo_from_db = connectToMySQL('dojos_and_ninjas').query_db(query,data)

        return cls(dojo_from_db[0])


    @classmethod
    def save_ninja(cls, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s), (%(last_name)s), (%(age)s, (%(dojo_id)s));"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )


    @classmethod
    def save_dojo(cls, data ):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, NOW() , NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos"
        dojo = connectToMySQL("dojos_and_ninjas").query_db(query)
        return dojo

        
    @classmethod
    def get_ninjas(cls):
        query = "SELECT * FROM ninjas"
        ninja = connectToMySQL("dojos_and_ninjas").query_db(query)
        return ninja
