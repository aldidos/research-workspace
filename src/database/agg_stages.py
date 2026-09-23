
def lookup(_from, localField, foreignField, _as, pipeline = []) : 
    return { 
        '$lookup' : {
            'from': _from,
            'localField': localField,
            'foreignField': foreignField,
            'as': _as,
            'pipeline' : pipeline
        }
    }

def unwind(path) : 
    return {
        '$unwind' : {
            'path': path,
        }
    }

def match(filters) : 
    return {
        '$match' : filters
    }

def project(filters) : 
    return {
        '$project' : filters
    }

def Set(filters) : 
    return {
        '$set' : filters
    }

def group(_id, field_name, accumulator) : 
    return {
        '$group' : {
            '_id': _id,
            field_name : accumulator
        }
    }

def sort(field, order) : 
    return {
        '$sort' : {
            field : order
        }
    }