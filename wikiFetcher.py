import sys

CLASS = 6
FAMILY = 7
GENUS = 89
RELEVANT_COLUMNS = {
    'Class': 6,
    'Family': 7,
    'Genus': 8,
    'Species': 9
}

def parse_arguments():
    if len(sys.argv) < 3:
        print("Not enough arguments. Usage: [mollusc data file] [output directory]")
        sys.exit(2)
    return (sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    molluscFile, outDir = parse_arguments()
    with open(molluscFile) as molluscData:
        for line in molluscData.readlines():
            values = line.split(';')
            for val in [x for x in values if x in RELEVANT_COLUMNS]:
                pass
