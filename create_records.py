# create_records.py
#
# Generates synthetic manufacturing test records and writes them to records.json.
# Record parameters (sites, stations, slots, products, etc.) are configured in test_specs.py.

import datetime
import json
import random
import uuid

from test_specs import (
    num_of_records, mfg_sites, failure_modes,
    prod_map, test_areas, test_stations, test_slots, records_file,
)

# Yield-loss rate applied per test area during record generation.
YIELD_LOSS = {
    "FAT": 0.18,
    "IST": 0.10,
    "FFT": 0.02,
}


def create_test_records(count, prefix, f_list, p_list, a_list, s_list, sl_list):
    date_code = datetime.date.today().strftime("%y%m%d")
    serials = [f"{prefix}{date_code}{n:04}" for n in range(1, count + 1)]
    records = {}
    products = list(p_list.keys())

    for serial in serials:
        prod_name = random.choice(products)
        part_num = p_list[prod_name]

        for area in a_list:
            run_key = str(uuid.uuid4())
            status = "PASS"
            symptom = ""

            if random.random() < YIELD_LOSS.get(area, 0):
                status = "FAIL"
                symptom = random.choice(f_list[area])

            records[run_key] = {
                "SER_NUM": serial,
                "TEST": area,
                "PROD_NAME": prod_name,
                "STATUS": status,
                "SYMPTOM": symptom,
                "PART_NUM": part_num,
                "HW_VER": "A0",
                "HOSTNAME": random.choice(s_list),
                "SLOT": random.choice(sl_list),
                "SITE": prefix,
                "TIMESTAMP": str(datetime.datetime.now()),
            }

    with open(records_file, "w") as fh:
        json.dump(records, fh, indent=4)


if __name__ == "__main__":
    create_test_records(
        num_of_records, mfg_sites[0], failure_modes,
        prod_map, test_areas, test_stations, test_slots,
    )
