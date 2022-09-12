from typing import List

from ncbi.datasets.openapi import ApiClient as DatasetsApiClient
from ncbi.datasets.openapi import ApiException as DatasetsApiException
from ncbi.datasets import GeneApi as DatasetsGeneApi

# Provide your own gene ids as a list of integers
input_gene_ids: List[int] = [1, 2, 3, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def example_usage_of_api(gene_ids: List[int]):
    if len(gene_ids) == 0:
        print("Please provide at least one gene-id")
        return

    with DatasetsApiClient() as api_client:
        gene_api = DatasetsGeneApi(api_client)

        # Get just metadata
        try:
            gene_reply = gene_api.gene_metadata_by_id(gene_ids)
            for gene in gene_reply.genes:
                print(gene.gene.gene_id)
        except DatasetsApiException as e:
            print(f"Exception when calling GeneApi: {e}\n")

        # Or, download a data package with FASTA files
        try:
            print("Begin download of data package ...")
            gene_ds_download = gene_api.download_gene_package(
                gene_ids, include_annotation_type=["FASTA_GENE"], _preload_content=False
            )
            gene_reply = gene_api.gene_metadata_by_id(gene_ids)
            zipfile_name = "gene_ds.zip"

            with open(zipfile_name, "wb") as f:
                f.write(gene_ds_download.data)
            print(f"Download completed -- see {zipfile_name}")

        except DatasetsApiException as e:
            print(f"Exception when calling GeneApi: {e}\n")

example_usage_of_api(input_gene_ids)