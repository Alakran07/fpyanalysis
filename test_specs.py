test_areas =   ["FAT","IST","FFT"]
test_status =  ["PASS","FAIL","ABORT"]
mfg_sites = ["ATL", "HTX", "TAU", "FLO"]
test_stations = ["POD-01", "POD-02", "POD-03"]
prod_map = {
    "DEMO_DOG":"73-0112-01",
    "VECNA":"78-3409-01",
    "UPSIDE_DOWN":"73-9034-01",
    "MIND_FLAYER": "78-0090-01",
    "DEMOGORGON":"873-0990-02"
    }
num_of_records = 1000

failure_modes = {
     "FAT":[
            "Serial Number missmatch",
            "Console not found",
            "Inventory check-ram",
            "Inventory check-ssd",
            "Inventory check-nic",
            "Inventory check-ps",
            "Inventory check-cpu"
        ],
     "IST":[
            "Mac not found",
            "Temperature alarm",
            "CPU Throttling",
            "PSU Voltage Drop",
            "Stress Test Timeout",
            "FW upgrade Fail",
            "Kernel Alarm",
            "Inlet Temperature alarm",
            "CPU Throttling",
            "Outlet Temperature alarm",
        ],
    "FFT": [
            "Wrong FW",
            "fail monitor",
            "BMC error",
        ]
    }