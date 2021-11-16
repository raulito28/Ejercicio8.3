import json
def store(var, Coches):
    json.dump(json.dumps(var), open(Coches, "w"))

def retrieve(Coches):
    var = json.loads(json.load(open(Coches, "r")))
    return var