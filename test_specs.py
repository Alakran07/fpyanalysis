test_areas = ["FAT", "IST", "FFT"]
mfg_sites = ["ATL", "HTX", "TAU", "FLO"]
test_stations = ["POD-01", "POD-02", "POD-03", "POD-04", "POD-05"]
test_slots = [f"Slot_{n:02}" for n in range(1, 11)]
records_file = "records.json"

prod_map = {
    "DEMO_DOG": "73-0112-01",
    "VECNA": "78-3409-01",
    "UPSIDE_DOWN": "73-9034-01",
    "MIND_FLAYER": "78-0090-01",
    "DEMOGORGON": "873-0990-02",
}

num_of_records = 1000

failure_modes = {
    "FAT": [
        "Serial Number mismatch",
        "Console not found",
        "Inventory check-ram",
        "Inventory check-ssd",
        "Inventory check-nic",
        "Inventory check-ps",
        "Inventory check-cpu",
    ],
    "IST": [
        "Mac not found",
        "Temperature alarm",
        "CPU Throttling",
        "PSU Voltage Drop",
        "Stress Test Timeout",
        "FW upgrade Fail",
        "Kernel Alarm",
        "Inlet Temperature alarm",
        "Memory Error",
        "Outlet Temperature alarm",
    ],
    "FFT": [
        "Wrong FW",
        "Fail Monitor",
        "BMC error",
    ],
}
