# healthkit-csv-convert
Convert HealthKit XML files to CSV

## How to export
- Open the Health app on your iPhone
- Press upperhand right corner "Person" symbol
- Click on "Data export" at bottom (mileage may vary depending on language settings)
- You may share the resulting zip file by mail, iCloud or similar

## How to use
```Python
python run.py Export.xml export.csv
```
- Import the resulting CSV file into your spreadsheet or data parsing application of choice!

## FAQ
1. How can I modify which values are parsed?

    Just change the array at the beginning of run.py:
    ```Python
    types = ["HKQuantityTypeIdentifierHeartRate"]
    ```
    You may find additional field specifiers inside the XML file.
2. Excel isn't importing the CSV in the right format!

    Your field and line separators may vary on your platform. Change the following variables accordingly:
    ```Python
    field_separator = ";"
    line_separator = "\n"
    ```
