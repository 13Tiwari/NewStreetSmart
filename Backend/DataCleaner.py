import pandas as pd 

def clean_data(data):
    # Load the crime data from a CSV file
    crime_data = pd.read_csv('Backend/Data/RawData/' + data)

    # Drop all columns except for latitude and longitude
    cleaned_data = crime_data[['latitude', 'longitude']]

    # Save the cleaned data to a new CSV file
    cleaned_data.to_csv('Backend/Data/CleanedData/cleaned_crime_data.csv', index=False)

    print("Data cleaned and saved to 'cleaned_crime_data.csv'")

