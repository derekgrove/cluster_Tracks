import parse_data as parse
import find_center_charge as coc


def main():
    filename = 'raw_data.txt'
    truths, clusters = parse.parse_data(filename)
    total_charges = coc.calculate_charges(clusters)
    
    print(total_charges)

if __name__ == "__main__":
    main()

