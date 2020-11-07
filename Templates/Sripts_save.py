import json
def save_file_json(name_file, dic_data):
    with open("Lesson 10\\data\\" + name_file + ".json", "w+") as fp:
        json.dump(dic_data, fp)
    fp.close()

dic_data = {
    "Price": "19.990.000",
    "Name": "ASUS TUF GeForce RTX 3090 24G Gaming",
    "Graphics Engine":"NVIDIA® GeForce RTX™ 3080",
    "Video Memory":"10GB GDDR6X",
    "Memory Interface":"320-bit", 
    "PowerConnector": "2 x 8-pin",
    "Memory Speed": "19.5 Gbps",
    "Engine Clock": "OC Mode - 1740 MHz Gaming Mode - 1710 MHz",
    "Interface": "PCI Express 4.0",
    "Number Of Fan Cooling": 4,
    "CUDA core": 4352,
}

save_file_json("GPU3", dic_data)