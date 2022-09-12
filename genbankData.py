import os
import requests
from Bio import SeqIO

# RCSB PDB 
#r = requests.get("https://files.rcsb.org/download/4hhb.pdb")

#print(r.text)


data = {'report': 'fasta'}
r = requests.get("https://www.ncbi.nlm.nih.gov/nuccore/AM711867.1", params =data)
print(r.encoding)
print(r.url)

print(r.text)


