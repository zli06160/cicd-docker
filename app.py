from testZli import uniswap_v2_price_calculator
import csv

app = uniswap_v2_price_calculator.UniswapV2PriceCalculator()

def intergration_test():
    with open("./integration_test_data.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if app.calculate_price(float(row[0]), float(row[1]), float(row[2]), float(row[3])) == float(row[4]):
                continue
            else:
                raise ValueError("Test not passing with the row: {} {} {} {} => ".format(row[0], row[1], row[2], row[3], row[4]))


