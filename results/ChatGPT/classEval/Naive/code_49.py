class JobMarketplace:
    """
    This class provides functionalities to publish positions, remove positions, submit resumes,
    withdraw resumes, search for positions, and obtain candidate information.
    """

    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        """
        Publish a job position and add it to the job_listings list.
        
        :param job_title: The title of the position, str.
        :param company: The company of the position, str.
        :param requirements: The requirements of the position, list.
        """
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job):
        """
        Remove a job position from the job_listings list.
        
        :param job: The position information to be removed, dict.
        """
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        """
        Submit a resume and add it to the resumes list.
        
        :param name: The name of the candidate, str.
        :param skills: The skills of the candidate, list.
        :param experience: The experience of the candidate, str.
        """
        resume = {
            'name': name,
            'skills': skills,
            'experience': experience
        }
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        """
        Withdraw a resume from the resumes list.
        
        :param resume: The resume information to be removed, dict.
        """
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria):
        """
        Search for job positions that meet the given criteria.
        
        :param criteria: The search criteria, str.
        :return: A list of job positions that match the criteria.
        """
        matching_jobs = [
            job for job in self.job_listings
            if any(skill in job['requirements'] for skill in criteria)
        ]
        return matching_jobs

    def get_job_applicants(self, job):
        """
        Obtain candidate information for a specific job position.
        
        :param job: The position information, dict.
        :return: A list of candidate information that meets the job requirements.
        """
        applicants = [
            resume for resume in self.resumes
            if all(skill in resume['skills'] for skill in job['requirements'])
        ]
        return applicants