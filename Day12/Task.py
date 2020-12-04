''' EXCERCISE 

Create a JSON of all object types and import the JSON into a SQL Database
Note: The JSON file should have valus of all Datatypes  '''

from pymongo import MongoClient

connection = MongoClient("localhost", 27017)

pythonDataTypes = {
    "Numeric": {
        "int": 15,
        "float": 4.856,
        "complex": "3 + 2j",
    },
    "Sequence Type": {
        "str": "BestEnlist Python Development",
        "list": "[1, 2, 3, 4, 5]",
        "tuple": "(1, 2, 3, 4, 5)"
    },
    "Boolean": {
        "bool": "True"
    },
    "Set": {
        "set": "{1, 2, 3, 4, 5}"
    },
    "Dictionary": {
        "dict": {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    }
}

db = connection['bepythonDB']

collection = db['datatype']

collection.insert_one(pythonDataTypes)

if collection:
    print("Data inserted successfully")
    for data in collection.find({}):
        print(data)
else:
    print("Error")
