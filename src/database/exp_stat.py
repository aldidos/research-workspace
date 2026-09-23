
def trim(input) : 
    return {
        '$trim' : { 'input' : input }
    }

def toLower(str) : 
    return {
        '$toLower' : str
    }

def map(input, _as, _in) : 
    return {
        '$map' : {
            'input' : input, 
            'as' : _as, 
            'in' : _in
        }
    }

def eq(l_value, r_value) : 
    return {  
        '$eq' : [ l_value, r_value ] 
    }

def OR(exprs) : 
    return {
        '$or' : exprs
    }

def IN(value, array_expression) : 
    return {
        '$in' : [ value, array_expression ]
    }

def And(exprs) : 
    return {
        '$and' : exprs
    }

def gte(l_exp, r_exp) : 
    return {
        '$gte' : [l_exp, r_exp]
    }

def expr(filter) : 
    return {
        '$expr' : filter
    }    

def size(path) : 
    return {
        '$size' : path
    }

def array_element_at(array, index) : 
    return {
        '$arrayElemAt' : [ array, index ]
    }

def date_from_string(date_string) :  ####
    return {
        '$dateFromString' : {
            'dateString' : date_string
        }
    }

def date_diff(start_date, end_date, unit) : 
    return {
        '$dateDiff' : {
            'startDate' : start_date, 
            'endDate' : end_date, 
            'unit' : unit
        }
    }

def get_field(field, input) : 
    return {
        '$getField' : {
            'field' : field, 
            'input' : input
        }
    }

def get_array_obj_field(array, index, field) : 
    return get_field( field, array_element_at( array, index ) )