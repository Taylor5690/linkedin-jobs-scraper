thonimport json
import requests
from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import Exporter

def run_scraper(search_params, output_format='json'):
    """
    Main runner function for the LinkedIn Jobs Scraper.
    Parameters:
        search_params (dict): Dictionary of search parameters (e.g., job title, location).
        output_format (str): Desired output format ('json', 'csv', 'xml').
    Returns:
        None
    """
    parser = LinkedInParser(search_params)
    job_listings = parser.fetch_job_listings()

    exporter = Exporter()
    if output_format == 'json':
        exporter.export_to_json(job_listings, 'output.json')
    elif output_format == 'csv':
        exporter.export_to_csv(job_listings, 'output.csv')
    elif output_format == 'xml':
        exporter.export_to_xml(job_listings, 'output.xml')

if __name__ == "__main__":
    search_params = {
        "job_title": "Full-stack Developer",
        "location": "Warsaw, Poland",
        "company": "ALGOTEQUE"
    }
    run_scraper(search_params)