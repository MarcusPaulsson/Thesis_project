class JobMarketplace:
    """
    A class that provides functionalities to publish positions, remove positions, submit resumes,
    withdraw resumes, search for positions, and obtain candidate information.
    """

    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title: str, company: str, requirements: list):
        """
        Publish a job position and add it to the job_listings.

        :param job_title: The title of the position.
        :param company: The company offering the position.
        :param requirements: A list of requirements for the position.
        """
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job):
        """
        Remove a job position from the job_listings.

        :param job: The job information to be removed.
        """
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name: str, skills: list, experience: str):
        """
        Submit a resume and add it to the resumes list.

        :param name: The name of the candidate.
        :param skills: A list of skills of the candidate.
        :param experience: The experience of the candidate.
        """
        resume = {
            'name': name,
            'skills': skills,
            'experience': experience
        }
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        """
        Withdraw a resume and remove it from the resumes list.

        :param resume: The resume information to be removed.
        """
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria: str):
        """
        Search for job positions that meet the given criteria.

        :param criteria: A skill or requirement to search for.
        :return: A list of matching job positions.
        """
        return [
            job for job in self.job_listings if criteria in job['requirements']
        ]

    def get_job_applicants(self, job):
        """
        Get applicants for a given job position.

        :param job: The job information to check against.
        :return: A list of candidates that meet the job requirements.
        """
        return [
            resume for resume in self.resumes if self.matches_requirements(resume, job['requirements'])
        ]

    def matches_requirements(self, candidate, requirements: list):
        """
        Check if a candidate meets the job requirements.

        :param candidate: A candidate's resume.
        :param requirements: A list of required skills.
        :return: True if the candidate meets all requirements, False otherwise.
        """
        return all(skill in candidate['skills'] for skill in requirements)