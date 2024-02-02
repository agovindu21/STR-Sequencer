# STR-Sequencing Emulator

# Background
This Python sequencing tool leverages short tandem repeats (STRs), allowing users to take DNA sequences of any length and match them to a database of known human DNA samples. Short tandem repeats (STRs) are commonly repeating DNA satellites, with repeat units that are 2 to 7 base pairs in length. Because the number of repeats varys among individuals, STR analysis is a common molecular biology tool used to compare STRs at specific loci in DNA between two or more samples. This is also an especially useful forensic tool, and is very often used for human identification purposes. 

# Usage

Python3 STR_Analysis.py database.csv sequence.txt
- where you include the specific name of the database and sequence of interest
- if the command-line is used improperly, the following error will arise: "Usage: python dna.py data.csv sequence.txt"

This repository contains a folder of 20 sample sequences and a database of sample individuals and their known STR counts. These can be used by users to experiment with this tool in a similar way to how it would be used in the real world. Users can also incoporate their own .txt sequences and .csv databases of individuals, editing the Python file accordingly to include the relevant STRs.
