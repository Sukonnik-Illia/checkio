def rec(path, value, result):
    if type(value) == dict and value != {}:
        for key in value:
            rec(path + [key], value[key], result)
    else:
        result['/'.join(path)] = value if value != {} else ""


def flatten(d):
    result = {}
    rec([], d, result)
    return result
