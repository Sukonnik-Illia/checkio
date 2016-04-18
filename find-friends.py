def check_connection(network, first, second):
    groups = [set(i.split('-')) for i in network]
    first = set(first.split('-'))
    second = set(second.split('-'))
    for i in range(len(groups)):
        for group in groups:
            if first.intersection(group):
                first.update(group)
            if second.intersection(group):
                second.update(group)

    return True if second.intersection(first) else False

def dict_create(network):
    k, names = [set(x.split("-")) for x in network], set([])
    for t in k:
        names.update(t)
    d ={}
    for name in names:
        d[name] = {x for x in names if {name, x} in k }
    return """
           """
