#main
from create_records import create_test_records
from analytics import run_factory_analytics
from test_specs import *



if __name__ == "__main__":
    create_test_records(num_of_records, mfg_sites[0], failure_modes, prod_map, test_areas)
    run_factory_analytics()


