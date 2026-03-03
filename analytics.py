from test_specs import *
import json


def run_factory_analytics():
    with open("records.json", "r") as f:
        data = json.load(f)

    quality = {}
    for run_id,record  in data.items():
        station = record["TEST"]
        status = record["STATUS"]
        if station not in quality:
             quality[station] = {"PASS":0, "FAIL":0}
        quality[station][status] = quality[station][status] + 1
    print("_"*50)
    print(f"{'STATION':<15} | {'YIELD (%)':<10} ")
    print("-" * 50)

    for station,info in quality.items():
        total = info["PASS"] + info["FAIL"]
        fpy = (info["PASS"]/total) * 100

        print(f"{station:<15} | {fpy:<3.2f} % ")
    print("-" * 50)

    pass


def run_product_analytics():
    with open("records.json", "r") as f:
        data = json.load(f)

    prod_quality = {}

    for run_id, record in data.items():
        # SWAP: Use PROD_NAME as the key instead of TEST
        product = record["PROD_NAME"]
        status = record["STATUS"]

        if product not in prod_quality:
            prod_quality[product] = {"PASS": 0, "FAIL": 0}

        # Note: We use .get() or check for existence to avoid errors with "ABORT"
        # but for now, sticking to your logic:
        prod_quality[product][status] += 1

    print(f"{'PRODUCT':<15} | {'YIELD (%)':<10} | {'TOTAL UNITS'}")
    print("-" * 50)

    for product, info in prod_quality.items():
        total = info["PASS"] + info["FAIL"]
        if total > 0:
            fpy = (info["PASS"] / total) * 100
            print(f"{product:<15} | {fpy:>9.2f}% | {total:>11}")
    print("-" * 50)
    pass

if __name__ == "__main__":
    run_factory_analytics()
    run_product_analytics()