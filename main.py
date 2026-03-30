# main.py
#
# Simulates manufacturing test records and runs FPY analytics.
#
# create_test_records() generates synthetic records and writes them to records.json.
# run_factory_analytics()  - FPY per test station
# run_product_analytics()  - FPY per product and test area
# run_station_analytics()  - FPY per product, test area, and test station

from create_records import create_test_records
from analytics import run_factory_analytics, run_product_analytics, run_station_analytics
from test_specs import (
    num_of_records, mfg_sites, failure_modes,
    prod_map, test_areas, test_stations, test_slots,
)

if __name__ == "__main__":
    create_test_records(
        num_of_records, mfg_sites[0], failure_modes,
        prod_map, test_areas, test_stations, test_slots,
    )
    run_factory_analytics()
    run_product_analytics()
    run_station_analytics()
