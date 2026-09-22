def download_acsincome_datasets():
    import os
    
    from folktables import ACSDataSource, ACSIncome
    

    countries: dict[str, str] = {
        "AL": "Alabama",
        "CA": "California",
        "FL": "Florida",
        "GA": "Georgia",
        "IL": "Illinois",
        "MI": "Michigan",
        "NJ": "NewJersey",
        "NY": "NewYork",
        "NC": "NorthCarolina",
        "OH": "Ohio",
        "PA": "Pennsylvania",
        "TX": "Texas",
        "VA": "Virginia"
    }

    for key, value in countries.items():
        data_source = ACSDataSource(survey_year='2018', horizon='1-Year', survey='person')
        acs_data = data_source.get_data(states=[key], download=True)
        features, label, _group = ACSIncome.df_to_pandas(acs_data)

        specific_output_dir = f"datasets/acsincome/original/{value}"
        os.mkdir(specific_output_dir)
        
        features.to_csv(f"{specific_output_dir}/acs_income_features_{value}.csv", index=False)
        label.to_csv(f"{specific_output_dir}/acs_income_labels_{value}.csv", index=False)