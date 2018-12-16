dataset = {
               "table1": {
                    "tableName":{
                                "size":130,
                                "color":"red",
                                "material":"wood"
                               },
                    "instruction":
                                    [

                                    ]

                },

                "table2":{
                    "tableName": {
                        "size": 130,
                        "color": "red",
                        "material": "wood"
                    },
                    "instruction":
                        [
                            "Painting", "Making"
                        ]

                }
}



key_list = [x for x in dataset.keys()]

def getMatterial(List,key_list):
    if key_list == []:
        return None
    key = key_list[0]
    material = dataset[key]["tableName"]["material"]
    print(material)
    return getMatterial(List,key_list[1:])

print(getMatterial(dataset,key_list))

def getInfo(List,key):
    for table in List:
        if List[table]['tableName']['material'] == key:
            print(List[table])

print(getInfo(dataset,'wood'))

