import os

from scripts.create_joined_datasets import create_joined_datasets
from scripts.create_million_line_dataset import create_million_line_dataset
from scripts.download_adult_dataset import download_adult_dataset
from scripts.download_datasets import download_acsincome_datasets


def main():
    dir_paths = [
        "datasets",
        "datasets/adult",
        "datasets/acsincome",
        "datasets/acsincome/original",
        "datasets/acsincome/joined",
        "datasets/acsincome/one_million_line"
    ]

    for dir_path in dir_paths:
        os.mkdir(dir_path)

    print("Downloading datasets...")
    download_acsincome_datasets()
    download_adult_dataset()

    print("Joining features and labels into one dataset for ACSIncome datasets...")
    create_joined_datasets()

    print("Concatenating ACSIncome dataset into one...")
    create_million_line_dataset()

if __name__ == "__main__":
    main()