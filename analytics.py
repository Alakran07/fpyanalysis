# run_factory_analytics extract info from test records.json file then
# Calculates yield per test staion.
#
# run_product_analytics extract info from test records.json file then
# Calculates yield per product and per test station.
#
# In order to work, records.json needs exist to have information in the expected format.
#
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
        area = record["TEST"]

        if product not in prod_quality:
            prod_quality[product]= {}

        if area not in prod_quality[product]:
            prod_quality[product][area]= {"PASS": 0, "FAIL": 0}

        if status in prod_quality[product][area]:
            prod_quality[product][area][status] += 1
        # Note: We use .get() or check for existence to avoid errors with "ABORT"
        # but for now, sticking to your logic:

    print(f"{'PRODUCT':<15} | {'AREA'} |{'YIELD (%)':<10} | {'TOTAL UNITS'}")
    print("-" * 50)

    for product, info in prod_quality.items():
        for area, info2 in info.items():
            total = info2["PASS"] + info2["FAIL"]

            if total > 0:
                fpy = (info2["PASS"] / total) * 100
                print(f"{product:<15} | {area} |{fpy:>9.2f}% | {total:>11}")
    print("-" * 50)
    pass

if __name__ == "__main__":
    run_factory_analytics()
    run_product_analytics()