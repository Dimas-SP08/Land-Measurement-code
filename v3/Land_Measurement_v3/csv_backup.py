def export_to_csv(table):
    '''Save survey data to a CSV backup file'''
    try:
        table.to_csv('Elevation Data Backup.csv', index=False, float_format="%.3f")
        print("THE FILE HAS BEEN CREATED IN CSV")
        input("Enter to continue...")
    except Exception as e:
        print(f"Export failed: {e}")
        input("Enter to continue...")