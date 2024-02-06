# STR Sequencer

# Background
DNA, the carrier of genetic information in living things, has been used in criminal justice for decades. But how, exactly, does DNA profiling work? Given a sequence of DNA, how can forensic investigators identify to whom it belongs?

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals.

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS, the FBI’s DNA database, uses 20 different STRs as part of its DNA profiling process.

# Specification
This Python sequencing tool leverages 8 of the most common STRs, allowing users to take DNA sequences of any length and match them to a database of known human DNA samples. This repository contains a folder of 20 sample sequences and a database of sample individuals and their known STR counts. These can be used by users to experiment with this tool in a similar way to how it would be used in the real world. Users can also incoporate their own .txt sequences and .csv databases of individuals, editing the Python file accordingly to include the relevant STRs.

# Usage
In the command line type: "python3 STR_Analysis.py database.csv sequence.txt"
- where you include the specific name of the database and sequence of interest
- if an improper command is used, the following reminder will be printed: "Usage: python STR_Analysis.py data.csv sequence.txt"
