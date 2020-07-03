# RemoveNegative
# Language: Python
# Input: CSV (with negative values)
# Output: CSV (mapping to absolute values)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: CSV2GML plugin

PluMA plugin to take a CSV file with both positive and negative data
and convert to a CSV file with the same data as absolute values (so all negative
entries become positive).

Input and output files are straightforward; the input file is the CSV
file to convert (with negative edges) and the output file is the equivalent
CSV file with absolute values.
