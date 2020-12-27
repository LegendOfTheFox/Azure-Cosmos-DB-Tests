import uuid


def get_cats():
    counter = 0
    cat_list = []
    while counter < 5:
        temp_cat = {
            'id': 'Kitty_' + str(uuid.uuid4()),
            'name': 'Kitty' + str(uuid.uuid4()),
            'type': "tabby"
        }
        cat_list.append(temp_cat)
        counter += 1

    return cat_list
