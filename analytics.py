# analytics.py
#
# run_factory_analytics  - FPY per test station (HOSTNAME)
# run_product_analytics  - FPY per product and test area
# run_station_analytics  - FPY per product, test area, and test station
#
# records.json must exist before calling any of these functions.
# Run create_records.py first if the file is missing.

import json
import os

from test_specs import records_file


def load_records(filepath=records_file):
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Records file not found: '{filepath}'. Run create_records first."
        )
    with open(filepath, "r") as fh:
        return json.load(fh)


def _fpy(counts):
    """Return First Pass Yield percentage from a {'PASS': n, 'FAIL': n} dict."""
    total = counts["PASS"] + counts["FAIL"]
    if total == 0:
        return None, 0
    return (counts["PASS"] / total) * 100, total


def run_factory_analytics(filepath=records_file):
    data = load_records(filepath)
    quality = {}

    for record in data.values():
        station = record["HOSTNAME"]
        status = record["STATUS"]
        quality.setdefault(station, {"PASS": 0, "FAIL": 0})
        if status in quality[station]:
            quality[station][status] += 1

    col_station, col_yield = 9, 10
    width = col_station + col_yield + 7

    print("_" * width)
    print(f"{'STATION':<{col_station}} | {'YIELD (%)':<{col_yield}}")
    print("-" * width)
    for station in sorted(quality):
        fpy, total = _fpy(quality[station])
        if fpy is not None:
            print(f"{station:<{col_station}} | {fpy:>{col_yield}.2f}%")
    print("-" * width)


def run_product_analytics(filepath=records_file):
    data = load_records(filepath)
    prod_quality = {}

    for record in data.values():
        product = record["PROD_NAME"]
        area = record["TEST"]
        status = record["STATUS"]
        prod_quality.setdefault(product, {}).setdefault(area, {"PASS": 0, "FAIL": 0})
        if status in prod_quality[product][area]:
            prod_quality[product][area][status] += 1

    col_product, col_area, col_yield, col_total = 15, 5, 10, 11
    width = col_product + col_area + col_yield + col_total + 13

    print("_" * width)
    print(
        f"{'PRODUCT':<{col_product}} | {'AREA':<{col_area}}"
        f" | {'YIELD (%)':<{col_yield}} | {'TOTAL UNITS'}"
    )
    print("-" * width)
    for product in sorted(prod_quality):
        for area in sorted(prod_quality[product]):
            fpy, total = _fpy(prod_quality[product][area])
            if fpy is not None:
                print(
                    f"{product:<{col_product}} | {area:<{col_area}}"
                    f" | {fpy:>{col_yield}.2f}% | {total:>{col_total}}"
                )
    print("-" * width)


def run_station_analytics(filepath=records_file):
    data = load_records(filepath)
    summary = {}

    for record in data.values():
        product = record["PROD_NAME"]
        area = record["TEST"]
        station = record["HOSTNAME"]
        status = record["STATUS"]
        summary.setdefault(product, {}).setdefault(area, {}).setdefault(
            station, {"PASS": 0, "FAIL": 0}
        )
        if status in summary[product][area][station]:
            summary[product][area][station][status] += 1

    col_product, col_area, col_station, col_yield, col_total = 15, 5, 9, 10, 11
    width = col_product + col_area + col_station + col_yield + col_total + 16

    print("_" * width)
    print(
        f"{'PRODUCT':<{col_product}} | {'AREA':<{col_area}}"
        f" | {'STATION':<{col_station}} | {'YIELD (%)':<{col_yield}}"
        f" | {'TOTAL UNITS'}"
    )
    print("-" * width)
    for product in sorted(summary):
        for area in sorted(summary[product]):
            for station in sorted(summary[product][area]):
                fpy, total = _fpy(summary[product][area][station])
                if fpy is not None:
                    print(
                        f"{product:<{col_product}} | {area:<{col_area}}"
                        f" | {station:<{col_station}}"
                        f" | {fpy:>{col_yield}.2f}% | {total:>{col_total}}"
                    )
    print("-" * width)


if __name__ == "__main__":
    run_factory_analytics()
    run_product_analytics()
    run_station_analytics()
