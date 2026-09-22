def create_joined_datasets():
    from pathlib import Path
    
    import pandas as pd
    

    base_dir = Path("datasets/acsincome/original")

    for dir in base_dir.iterdir():
        if dir.is_dir():
            files = []
            for file in dir.iterdir():
                if file.is_file():
                    files.append(pd.read_csv(
                        f"datasets/acsincome/original/{dir.name}/{file.name}"
                    ))
            result = pd.concat(files, axis=1)
            result.to_csv(f"datasets/acsincome/joined/{dir.name}.csv", index=False)