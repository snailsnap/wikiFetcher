import sys
import wikipedia

CLASS = 6
FAMILY = 7
GENUS = 89
RELEVANT_COLUMNS = {
    'Class': 6,
    'Family': 7
    #'Genus': 8,
    #'Scientific Name': 10
}


def parse_arguments():
    if len(sys.argv) < 3:
        print(
            "Not enough arguments. Usage: [mollusc data file] [output directory]")
        sys.exit(2)
    return (sys.argv[1], sys.argv[2])


def fetchInfo(outDir, term_type, term):
    print("Fetching file for {}: {}".format(term_type, term))
    filePath = '{}{}_{}.txt'.format(outDir, term_type, term)
    with open(filePath, 'w') as file:
        try:
            summary = wikipedia.summary(term, sentences=3)
            for line in summary.splitlines():
                if not line:
                    break
                file.write(line)
        except wikipedia.exceptions.PageError:
            file.write("PageError for '{}'.".format(term))
        except wikipedia.exceptions.DisambiguationError:
            file.write("DisambiguationError for '{}'".format(term))


if __name__ == '__main__':
    # set up
    molluscFile, outDir = parse_arguments()
    fetched_values = set()
    wikipedia.set_lang('de')
    # fetch data
    with open(molluscFile) as molluscData:
        for line in molluscData.readlines()[1:]:
            values = line.split(';')
            for column in RELEVANT_COLUMNS:
                column_num = RELEVANT_COLUMNS[column]
                val = values[column_num]
                if val not in fetched_values:
                    fetchInfo(outDir, column, val)
                    fetched_values.add(val)
