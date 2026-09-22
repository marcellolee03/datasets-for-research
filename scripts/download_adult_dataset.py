def download_adult_dataset():
    import kaggle
    
    kaggle.api.authenticate()

    kaggle.api.dataset_download_files(
        "uciml/adult-census-income",
        path="datasets/adult/",
        unzip=True
    )