thonimport requests
from datetime import datetime

class LinkedInParser:
    def __init__(self, search_params):
        self.search_params = search_params
        self.base_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings"
    
    def fetch_job_listings(self):
        """
        Fetches job listings from LinkedIn based on the provided search parameters.
        Returns:
            list: List of job listings (dictionaries).
        """
        response = requests.get(self.base_url, params=self.search_params)
        if response.status_code == 200:
            job_listings = response.json().get('elements', [])
            return [self.parse_job_listing(job) for job in job_listings]
        else:
            raise Exception(f"Failed to fetch job listings: {response.status_code}")
    
    def parse_job_listing(self, job):
        """
        Parses individual job listing to extract required details.
        Parameters:
            job (dict): Job data from LinkedIn API.
        Returns:
            dict: Parsed job details.
        """
        return {
            "job_id": job.get("jobId"),
            "job_link": job.get("jobLink"),
            "job_title": job.get("jobTitle"),
            "company_name": job.get("companyName"),
            "company_linkedin_url": job.get("companyLink"),
            "job_location": job.get("location"),
            "job_published_at": job.get("datePosted"),
            "job_posted_time": self.format_posted_time(job.get("postedTime")),
            "job_salary_info": job.get("salary", ""),
            "applicants_count": job.get("applicantsCount"),
            "benefits": job.get("benefits", ""),
            "description_text": job.get("description"),
            "apply_link": job.get("applyLink"),
            "job_seniority_level": job.get("seniorityLevel"),
            "job_employment_type": job.get("employmentType"),
            "job_function": job.get("jobFunction"),
            "job_industries": job.get("industries")
        }
    
    def format_posted_time(self, posted_time):
        """Formats the posted time to a human-readable format."""
        if posted_time:
            return datetime.strptime(posted_time, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%b %d, %Y")
        return "N/A"