def create_million_line_dataset():
    from pathlib import Path
    
    import pandas as pd
    

    joined_dir = Path("datasets/acsincome/joined")
    files = []
    
    for file in joined_dir.iterdir():
        if file.is_file():
            files.append(pd.read_csv(f"datasets/acsincome/joined/{file.name}"))
    
    result = pd.concat(files)
    result.to_csv("datasets/acsincome/one_million_line/one_million_line_dataset.csv", index=False)