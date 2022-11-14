import json
# File I/O Open function for read data from JSON File
data = {}  # Define Empty Dictionary Object

# Define a format Dictionary Object
formatted_pos = {
    "dataset_name": "pos_0.png.json",
    "image_link": "",
    "annotation_type": "image"
}

# Define a null attribute Dictionary Object
annot_att_null = {
    "annotation_attributes": {
        "vehicle": {
            "Type": "null",
            "Pose": "null",
            "Model": "null",
            "Make": "null",
            "Color": "null"
        },
        "license_plate": {
            "Difficulty Score": "null",
            "Value": "null",
            "Occlusion": "null"
        }
    }
}

try:

    with open("pos_0.png.json", "r") as file_object:
        data = json.load(file_object)
        listOfDicts = data["objects"]

        # responsible for getting null value
        def nullfunc():
            boxlistao = []
            boxlistao = {"bbox": boxlistao}
            boxlistao["presence"] = 0
            vehicle = {"vehicle": boxlistao}
            annotation_objects = {"annotation_objects": vehicle}
            # print(annotation_objects)

            bboxli = []
            bboxli = {"bbox": bboxli}
            bboxli["presence"] = 0
            license_plate = {"license_plate": bboxli}
            vehicle.update(license_plate)
            formatted_pos.update(annotation_objects)

            formatted_pos.update(annot_att_null)
            # print(formatted_pos)

            with open('formatted_null', 'w') as formatted:
                json.dump([formatted_pos], formatted, indent=4, separators=(',', ': '), skipkeys=False, ensure_ascii=True, check_circular=True,
                          allow_nan=True, cls=None, default=None, sort_keys=False,)
            print(formatted_pos)

        if len(listOfDicts) == 0:
            nullfunc()

        else:

            # helping to get dict key and value
            def find(lst, key, value):
                for i, dic in enumerate(lst):
                    if dic[key] == value:
                        return i
                return -1

            classVehicle = find(listOfDicts, 'classTitle', 'Vehicle')
            classLicpl = find(listOfDicts, 'classTitle', 'License Plate')

            listOfDict0 = listOfDicts[classVehicle]
            listOfDict1 = listOfDicts[classLicpl]

            # helping to get annotation attribute
            def annot_att_fun(annot_att):
                newkeylist = []
                newvallist = []
                for each_item in annot_att:
                    for k, v in each_item.items():
                        if k == "name":
                            keylist = [v]
                            for x in keylist:
                                newkeylist.append(x)
                        if k == "value":
                            vallist = [v]
                            for x in vallist:
                                newvallist.append(x)

                annot_att = dict(zip(newkeylist, newvallist))
                return annot_att

            if (listOfDict0['classTitle'] == "Vehicle" and listOfDict1['classTitle'] == "License Plate"):

                # print(listOfDict0) #dict
                # print(listOfDict1) #dict

                # helping to get points annotation object and list
                def box_func(pointsao_lis):
                    boxlistao_lis = []
                    for point in pointsao_lis:
                        boxlistao_lis.append(point)
                    boxlistao_lis = boxlistao_lis[0] + boxlistao_lis[1]
                    return boxlistao_lis

                boxlistao = box_func(listOfDict0['points']['exterior'])
                boxlistao = {"bbox": boxlistao}
                boxlistao["presence"] = 1
                vehicle = {"vehicle": boxlistao}
                annotation_objects = {"annotation_objects": vehicle}
                # print(annotation_objects)

                bboxli = box_func(listOfDict1['points']['exterior'])
                bboxli = {"bbox": bboxli}
                bboxli["presence"] = 1
                license_plate = {"license_plate": bboxli}
                vehicle.update(license_plate)
                formatted_pos.update(annotation_objects)
                # print(formatted_pos)

            # Getting annotation attribute
                annot_attdict_vh = annot_att_fun(listOfDict0['tags'])
                vehicle = {"vehicle": annot_attdict_vh}
                # print(vehicle)

                annot_attdict_lic = annot_att_fun(listOfDict1['tags'])
                annot_attdict_lic.update({"Occlusion": 0})
                license_plate = {"license_plate": annot_attdict_lic}
                # print(license_plate)

                vehicle.update(license_plate)
                annotation_attributes = {"annotation_attributes": vehicle}
                formatted_pos.update(annotation_attributes)
                # print(formatted_pos)

                with open('formatted_pos_0', 'w') as formatted:
                    json.dump([formatted_pos], formatted, indent=4, separators=(',', ': '), skipkeys=False, ensure_ascii=True, check_circular=True,
                              allow_nan=True, cls=None, default=None, sort_keys=False,)

                print(formatted_pos)

            else:
                nullfunc()

except:
    print("Import Error")


"""

            def annot_att_null_fun(annot_att_null):
                newkeylist = []
                newvallist = []
                for each_item in annot_att_null:
                    for k, v in each_item.items():
                        if k == "name":
                            keylist = [v]
                            for x in keylist:
                                newkeylist.append(x)
                        if k == "value":
                            vallist = [v]
                            for x in vallist:
                                newvallist.append(x)
                i = 0
                while i < len(newvallist):
                    newvallist[i] = "null"
                    i += 1
                annot_att_null = dict(zip(newkeylist, newvallist))
                return annot_att_null


                annot_attdict_vh = annot_att_null_fun(listOfDict0['tags'])
                vehicle = {"vehicle": annot_attdict_vh}
                # print(vehicle)
                
                annot_attdict_lic = annot_att_null_fun(listOfDict1['tags'])
                annot_attdict_lic.update({"Occlusion": "null"})
                license_plate = {"license_plate": annot_attdict_lic}
                # print(license_plate)

                vehicle.update(license_plate)
                annotation_attributes = {"annotation_attributes": vehicle}
"""
