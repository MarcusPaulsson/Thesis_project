class JobMarketplace:
    """
    A class that provides functionalities to publish positions, remove positions, submit resumes, withdraw resumes,
    search for positions, and obtain candidate information.
    """

    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title: str, company: str, requirements: list):
        """
        Publish a job position and add it to the job_listings.
        
        :param job_title: The title of the position.
        :param company: The company offering the position.
        :param requirements: The skills required for the position.
        """
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job: dict):
        """
        Remove a job position from the job_listings.
        
        :param job: The job information to be removed.
        """
        self.job_listings = [j for j in self.job_listings if j != job]

    def submit_resume(self, name: str, skills: list, experience: str):
        """
        Submit a resume and add it to the resumes list.
        
        :param name: The name of the candidate.
        :param skills: The skills of the candidate.
        :param experience: The experience of the candidate.
        """
        resume = {
            'name': name,
            'skills': skills,
            'experience': experience
        }
        self.resumes.append(resume)

    def withdraw_resume(self, resume: dict):
        """
        Withdraw a resume and remove it from the resumes list.
        
        :param resume: The resume information to be removed.
        """
        self.resumes = [r for r in self.resumes if r != resume]

    def search_jobs(self, criteria: str):
        """
        Search for job positions that match the given criteria.
        
        :param criteria: The skill or requirement to search for.
        :return: A list of job positions that match the criteria.
        """
        return [job for job in self.job_listings if criteria in job['requirements']]

    def get_job_applicants(self, job: dict):
        """
        Get candidates who match the requirements of a specific job.
        
        :param job: The job information.
        :return: A list of candidates who meet the job requirements.
        """
        return [resume for resume in self.resumes if self.matches_requirements(resume, job['requirements'])]

    def matches_requirements(self, resume: dict, requirements: list) -> bool:
        """
        Check if a resume matches the job requirements.
        
        :param resume: The resume information.
        :param requirements: The job requirements.
        :return: True if the resume matches the requirements, False otherwise.
        """
        return all(skill in resume['skills'] for skill in requirements)