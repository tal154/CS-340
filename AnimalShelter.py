from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
      
        self.client = MongoClient('mongodb://%s:%s@localhost:54698/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
            return True
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. 
    def read(self,criteria):
        # criteria is not None then this find will return all rows which matches the criteria
        if criteria is not None:
        #criteria should be a dictionary
            return self.database.animals.find(criteria, {'_id':False})
            
        else:
        #if there is no search criteria, then error  
            raise Exception("Nothing to read, because data parameter is empty")
            return False
        
# Create method to implement the U in CRUD.
    def update(self, fromTarget, toTarget):
        if fromTarget is not None:
        #update 
            update_result = self.database.animals.update_many(fromTarget, toTarget)
            print(update_result)
                      
           
        else:
            raise Exception("Nothing to update, criteria parameter is empty")
            return False
        
# Create method to implement the D in CRUD.
    def delete(self, criteria):
        if criteria is not None:
        #delete one
            try:
                delete_result = self.database.animals.delete_many(criteria)
                print(delete_result)
                return True
            
            except Exception as e:
                print("An exception has occurred: ", e)
                return False
                
        else:
        # lets user know there was a problem
            raise Exception("Nothing to delete, because the criteria parameter is empty")
            return False