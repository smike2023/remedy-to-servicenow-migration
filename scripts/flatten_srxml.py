# flatten_srxml.py

# This placeholder script flattens a simple SRXML XML into key-value format.
# Intended for preparing the data for ServiceNow Import Set compatibility.

import xml.etree.ElementTree as ET

def flatten_srxml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        print("Flattened SRXML Output:")
        for service_request in root.findall('ServiceRequest'):
            flattened = {}
            for element in service_request:
                flattened[element.tag] = element.text
            print(flattened)
    except Exception as e:
        print("Failed to flatten SRXML:", e)

# Example usage
if __name__ == "__main__":
    flatten_srxml("mock_srxml.xml")
