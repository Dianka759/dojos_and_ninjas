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
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, NOW() , NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )
    
    
    @classmethod
    def dojo_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = cls(results[0])
        for ninja in results:
            ninja_data = {
                'id': ninja['ninjas.id'],
                'dojo_id': ninja['dojo_id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'created_at': ninja['ninjas.created_at'],
                'updated_at': ninja['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(ninja_data) )
        return dojo



