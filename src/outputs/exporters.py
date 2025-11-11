thonimport json
import csv
import xml.etree.ElementTree as ET

class Exporter:
    def export_to_json(self, data, filename):
        """Exports job listings to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def export_to_csv(self, data, filename):
        """Exports job listings to a CSV file."""
        keys = data[0].keys() if data else []
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    
    def export_to_xml(self, data, filename):
        """Exports job listings to an XML file."""
        root = ET.Element("job_listings")
        for job in data:
            job_elem = ET.SubElement(root, "job")
            for key, value in job.items():
                ET.SubElement(job_elem, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)