import parse_data as parse
import find_center_charge as coc


def main():
    filename = 'raw_data.txt'
    truths, clusters = parse.parse_data(filename)
    center_of_charges = coc.calculate_charges(clusters)
    
    print("center of charges: ", center_of_charges)

if __name__ == "__main__":
    main()

