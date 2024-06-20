# Sequentially reads a file line by line, searching for occurences of a search string.
# If the string is found then the current line is written out to a new file
# Optionally include the first line regardless, if headers=True
def filter_file_by_string(
    input_file, output_file, search_string, encoding="UTF-8", headers=False
):
    with open(input_file, mode="r", encoding=encoding) as infile, open(
        output_file, mode="w"
    ) as outfile:
        lines = infile.readlines()

        if headers:
            outfile.write(lines[0])

        for line in lines:
            if search_string in line:
                outfile.write(line)
