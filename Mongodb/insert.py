import pymongo
conn = pymongo.Connection("localhost",27017)
db = conn.example
db.words.insert({"word": "oarlock", "definition": "A device attached to a rowboat to hold the oars in place"})
db.words.insert({"word": "seminomadic", "definition": "Only partially nomadic"})
db.words.insert({"word": "perturb", "definition": "Bother, unsettle, modify"})
