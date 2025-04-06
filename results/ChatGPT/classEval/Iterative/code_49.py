class JobMarketplace:
    """
    This class provides functionalities to publish positions, remove positions, submit resumes, withdraw resumes,
    search for positions, and obtain candidate information.
    """

    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        """
        Publish a job position and add the information to the job_listings list.
        
        :param job_title: The title of the position, str.
        :param company: The company of the position, str.
        :param requirements: The requirements of the position, list.
        :return: None
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
        :return: None
        """
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        """
        Submit a resume and add the information to the resumes list.
        
        :param name: The name of the resume, str.
        :param skills: The skills of the resume, list.
        :param experience: The experience of the resume, str.
        :return: None
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
        :return: None
        """
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria):
        """
        Search for job positions that meet the requirements.
        
        :param criteria: The requirements of the position, str.
        :return: The position information that meets the requirements, list.
        """
        return [job for job in self.job_listings if any(req in criteria for req in job['requirements'])]

    def get_job_applicants(self, job):
        """
        Obtain candidate information that meets the requirements of the job.
        
        :param job: The position information, dict.
        :return: The candidate information that meets the requirements, list.
        """
        applicants = []
        for resume in self.resumes:
            if all(req in resume['skills'] for req in job['requirements']):
                applicants.append(resume)
        return applicants