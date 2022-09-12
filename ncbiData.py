import sys
import zipfile
import pandas as pd
from pprint import pprint
from datetime import datetime
from collections import defaultdict, Counter
from IPython.display import display
import json


import matplotlib.pyplot as plt
plt.style.use('ggplot')

try:
    import ncbi.datasets
except ImportError:
    print('ncbi.datasets module not found. TO install, run pip install ncbi-datasets-pylib')

## Start an api_instance
api_instance = ncbi.datasets.GenomeApi(ncbi.datasets.ApiClient())

# NCBI by acession
assembly_acession = ['GCF_000001405.40'] # Need to be a full acession.version
genome_summary = api_instance.assembly_descriptors_by_accessions(assembly_acession , page_size = 1)
print(type(genome_summary))

#genome_summary contains metadata about the genome assembly and the total count of results in JSON format.
print(f"Number of assemblies:  {genome_summary.total_count}")

#Other informations
for assembly in map(lambda d: d.assembly, genome_summary.assemblies):
    print(
        assembly.assembly_accession,
        assembly.assembly_level,
        len(assembly.chromosomes),
        assembly.submission_date,
        sep='\t'
        )

#print(genome_summary)


# Now let's say you only know the name of the organism for which you want to retrieve assembly information.
## a few examples to try 
# tax_name = 'mammals'
# tax_name = 'birds'
# tax_name = 'butterflies'
tax_name = 'primates'

genome_summary = api_instance.assembly_descriptors_by_taxon(
    taxon=tax_name,
    page_size=1000)
print(f"Number of assemblies in the group '{tax_name}': {genome_summary.total_count}")


# we can analyze the results and organize by GenBank and RefSeq, and make a nice tabular output and pie-chart of the results

assm_counter = Counter()
for assembly in map(lambda d: d.assembly, genome_summary.assemblies):
    if assembly.assembly_accession[:3] == 'GCA':
        assm_counter['GenBank'] += 1
    elif assembly.assembly_accession[:3] == 'GCF':
        assm_counter['RefSeq'] += 1
    
print(assm_counter)
