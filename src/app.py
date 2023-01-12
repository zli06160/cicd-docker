from testzli import uniswap_v2_price_calculator
import csv

# This will validate the UniSwap V2 price calculator by using a reference file, where a set of test cases are stored.

app = uniswap_v2_price_calculator.UniswapV2PriceCalculator()

def intergration_test():
    with open("../ressources/integration_test_data.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader) # dont use header
        print("Starting tests: integration tests with reference data file...")
        for row in csvreader:
            if app.calculate_price(float(row[0]), float(row[1]), float(row[2])) == float(row[3]):
                print("Test passed with the row: {} {} {} => {}".format(row[0], row[1], row[2], row[3]))
            else:
                raise ValueError("/！\Test not passing with the row: {} {} {} => {} !".format(row[0], row[1], row[2], row[3]))
        print("All tests passed with success.")

if __name__ == '__main__':
    intergration_test()
