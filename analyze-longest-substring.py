import sys
from contiglib import longest_common_substrings

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as file_:
        lines = file_.readlines()
        for (line, nxt) in zip(lines, lines[1:]):
            contig = [line.strip(), nxt.strip()]
            lcs = longest_common_substrings(contig)
            if lcs:
                for l in lcs:
                    print(l)

