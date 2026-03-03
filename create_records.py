#  create_records.py
#
# Create dummy test records create_test_records() and dump the test records in
# records.json format. Parameters of records are found in test_specs.py
# (site, prefix, number of records, etc can)
# For future development, POD number can be added, so analysis can be also done
# to POD level (to find if failures point to any specific pod)
#


import random
import json
import datetime
import uuid

from analytics import run_factory_analytics
from test_specs import *


def create_test_records(count, prefix,f_list, p_list, a_list):
    date_str = str(datetime.date.today()).replace("-", "")
    date_code = date_str[-6:]
    serials = [ f"{prefix}{date_code}{n:04}" for n in range(1, count+1)  ]
    records = {}
    products = []
    for key in p_list: products.append(key)
    for serial in serials:
        prod_name = random.choice(products)
        part_num = p_list[prod_name]
        for f in a_list:
            t = str(datetime.datetime.now())
            #With UUIDs, every single "Test Start" and "Test Stop" event is preserved perfectly.
            run_key = str(uuid.uuid4())
            status = "PASS"
            symptom = ""
            if "FAT" in f: yield_loss = 0.18
            elif "IST" in f: yield_loss = 0.1
            else: yield_loss = 0.02
            if random.random() < yield_loss:
                status = "FAIL"
                symptom = random.choice(f_list[f])
            records[run_key]= {
                "SER_NUM":serial,
                "TEST":f,
                "PROD_NAME":prod_name,
                "STATUS":status,
                "SYMPTOM":symptom,
                "PART_NUM":part_num,
                "HW_VER": "A0",
                "HOSTNAME":"POD-01",
                "SITE":prefix,
                "TIMESTAMP":t
                }

    json.dump(records, open("records.json", "w"), indent=4)
    pass

if __name__ == "__main__":
    create_test_records(num_of_records,mfg_sites[0],failure_modes, prod_map, test_areas)




