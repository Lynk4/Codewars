def transformFruit(fruit):
    return fruit.replace('rotten','').lower()
def remove_rotten(bag_of_fruits):
    if not bag_of_fruits: 
        return []
    return list(map(transformFruit, bag_of_fruits))
