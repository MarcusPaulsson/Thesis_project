class JobMarketplace:
    """
    This is a class that provides functionalities to publish positions, remove positions, submit resumes, withdraw resumes, search for positions, and obtain candidate information.
    """

    def __init__(self):
        """
        Initializes the JobMarketplace with empty lists for job listings and resumes.
        """
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        """
        Publishes a new job listing.

        :param job_title: The title of the position (str).
        :param company: The company offering the position (str).
        :param requirements: A list of required skills or qualifications (list of str).
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
        Removes a job listing from the marketplace.

        :param job: The job listing to remove (dict).
        :return: None
        """
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        """
        Submits a resume to the marketplace.

        :param name: The name of the applicant (str).
        :param skills: A list of skills possessed by the applicant (list of str).
        :param experience: A brief description of the applicant's experience (str).
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
        Withdraws a resume from the marketplace.

        :param resume: The resume to withdraw (dict).
        :return: None
        """
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria):
        """
        Searches for job listings that match the given criteria.

        :param criteria: The search criteria (str).  Looks for this string within the job requirements.
        :return: A list of job listings that match the criteria (list of dict).
        """
        results = []
        for job in self.job_listings:
            if criteria in job['requirements']:
                results.append(job)
        return results

    def get_job_applicants(self, job):
        """
        Retrieves a list of applicants whose skills match the job requirements.

        :param job: The job listing to find applicants for (dict).
        :return: A list of resumes that match the job requirements (list of dict).
        """
        applicants = []
        for resume in self.resumes:
            if self.matches_requirements(resume, job['requirements']):
                applicants.append(resume)
        return applicants

    def matches_requirements(self, resume, requirements):
        """
        Checks if a resume's skills meet all the job requirements.

        :param resume: The resume to check (dict).
        :param requirements: A list of required skills (list of str).
        :return: True if the resume meets all requirements, False otherwise (bool).
        """
        for requirement in requirements:
            if requirement not in resume['skills']:
                return False
        return True