user_id = {
    0: 'Root',
    1: 'Moses',
    2: 'Noel',
    3: 'Thiago',
    4: 'Anna',
    5: 'Sarah',
}

def greeting(id):
    return 'Hi %s' % user_id[id]

greeting(1)
