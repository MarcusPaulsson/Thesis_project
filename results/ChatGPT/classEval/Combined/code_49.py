class JobMarketplace:
    """
    This class provides functionalities to publish positions, remove positions, 
    submit resumes, withdraw resumes, search for positions, and obtain candidate information.
    """

    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title: str, company: str, requirements: list) -> None:
        """
        Publish a new job position.
        :param job_title: The title of the position.
        :param company: The company of the position.
        :param requirements: The requirements of the position.
        """
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job: dict) -> None:
        """
        Remove a job position.
        :param job: The position information to be removed.
        """
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name: str, skills: list, experience: str) -> None:
        """
        Submit a new resume.
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

    def withdraw_resume(self, resume: dict) -> None:
        """
        Withdraw a resume.
        :param resume: The resume information to be removed.
        """
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria: str) -> list:
        """
        Search for jobs based on criteria.
        :param criteria: The requirement to search for.
        :return: A list of matching job positions.
        """
        return [
            job for job in self.job_listings 
            if any(criterion in job['requirements'] for criterion in criteria)
        ]

    def get_job_applicants(self, job: dict) -> list:
        """
        Get applicants for a specific job.
        :param job: The job information.
        :return: A list of candidates that match the job requirements.
        """
        return [
            resume for resume in self.resumes 
            if self.matches_requirements(resume, job['requirements'])
        ]

    def matches_requirements(self, resume: dict, requirements: list) -> bool:
        """
        Check if the resume matches the job requirements.
        :param resume: The candidate's resume.
        :param requirements: The job requirements.
        :return: True if matches, False otherwise.
        """
        return all(skill in resume['skills'] for skill in requirements)