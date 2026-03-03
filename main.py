#  main.py
#
# This file simulate creation of test records, create_records.py and quality analytics (FPY)
#
# Create dummy test records create_test_records() and dump the test records in
# records.json format, then run_factory_analytics() gets fpy per test station
# and run_product_analytics() does it for product and area.True


from create_records import create_test_records
from analytics import run_factory_analytics
from analytics import run_product_analytics
from test_specs import *



if __name__ == "__main__":
    create_test_records(num_of_records, mfg_sites[0], failure_modes, prod_map, test_areas)
    run_factory_analytics()
    run_product_analytics()


