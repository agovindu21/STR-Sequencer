# Match DNA sequence to individual based on Short Tandem Repeats(STR) in the sequence

import csv
import sys


def main():
    # Ensure correct command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    file = open(sys.argv[1])
    data = csv.DictReader(file)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as f:
        Seq = f.read()

    # Find longest match of each STR in DNA sequence, from user's choice of large or small database
    match = {}
    if sys.argv[1] == "databases/large.csv":
        STR = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
    else:
        STR = ["AGATC", "AATG", "TATC"]

    for i in range(len(STR)):
        match[STR[i]] = longest_match(Seq, STR[i])

    #  Check database for matching profiles
    for row in data:
        a = 0
        for j in range(len(STR)):
            if int(row[STR[j]]) == match[STR[j]]:
                a += 1
        if a == len(STR):
            name = "name"
            print(f"{row[name]}")
            file.close()
            return

    print("No match")
    file.close()
    return


def longest_match(sequence, subsequence):

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in substring within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

if __name__ == "__main__":
    main()
