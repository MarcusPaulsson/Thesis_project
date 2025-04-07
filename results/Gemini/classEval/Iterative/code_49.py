class JobMarketplace:
    """
    A class to manage job postings and resumes.
    """

    def __init__(self):
        """
        Initializes the JobMarketplace with empty job listings and resumes.
        """
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        """
        Publishes a new job posting.

        Args:
            job_title (str): The title of the job.
            company (str): The name of the company.
            requirements (list): A list of required skills or qualifications.

        Returns:
            None
        """
        if not all(isinstance(arg, str) for arg in [job_title, company]) or not isinstance(requirements, list):
            raise TypeError("Invalid input types. job_title and company must be strings, requirements must be a list.")

        job = {'job_title': job_title, 'company': company, 'requirements': requirements}
        self.job_listings.append(job)

    def remove_job(self, job):
        """
        Removes a job posting from the marketplace.

        Args:
            job (dict): The job posting to remove.

        Returns:
            None

        Raises:
            ValueError: If the job is not found in the job listings.
        """
        if not isinstance(job, dict):
            raise TypeError("job must be a dictionary.")

        try:
            self.job_listings.remove(job)
        except ValueError:
            raise ValueError("Job not found in job listings.")

    def submit_resume(self, name, skills, experience):
        """
        Submits a resume to the marketplace.

        Args:
            name (str): The name of the applicant.
            skills (list): A list of skills the applicant possesses.
            experience (str): A brief description of the applicant's experience.

        Returns:
            None
        """
        if not all(isinstance(arg, str) for arg in [name, experience]) or not isinstance(skills, list):
            raise TypeError("Invalid input types. name and experience must be strings, skills must be a list.")

        resume = {'name': name, 'skills': skills, 'experience': experience}
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        """
        Withdraws a resume from the marketplace.

        Args:
            resume (dict): The resume to withdraw.

        Returns:
            None

        Raises:
            ValueError: If the resume is not found in the resumes list.
        """
        if not isinstance(resume, dict):
            raise TypeError("resume must be a dictionary.")

        try:
            self.resumes.remove(resume)
        except ValueError:
            raise ValueError("Resume not found in resumes.")

    def search_jobs(self, criteria):
        """
        Searches for job postings that match the given criteria.

        Args:
            criteria (str): The search criteria (e.g., a skill or keyword).

        Returns:
            list: A list of job postings that match the criteria.
        """
        if not isinstance(criteria, str):
            raise TypeError("criteria must be a string.")

        results = []
        for job in self.job_listings:
            if any(criteria.lower() in req.lower() for req in job['requirements']):
                results.append(job)
        return results

    def get_job_applicants(self, job):
        """
        Finds applicants whose skills match the requirements of a given job.

        Args:
            job (dict): The job posting to find applicants for.

        Returns:
            list: A list of resumes that match the job requirements.
        """
        if not isinstance(job, dict):
            raise TypeError("job must be a dictionary.")

        applicants = []
        for resume in self.resumes:
            if self.matches_requirements(resume, job['requirements']):
                applicants.append(resume)
        return applicants

    def matches_requirements(self, resume, requirements):
        """
        Checks if a resume matches the given job requirements.

        Args:
            resume (dict): The resume to check.
            requirements (list): A list of required skills.

        Returns:
            bool: True if the resume meets all requirements, False otherwise.
        """
        if not isinstance(resume, dict) or not isinstance(requirements, list):
            raise TypeError("resume must be a dictionary and requirements must be a list.")

        for requirement in requirements:
            if requirement.lower() not in [skill.lower() for skill in resume['skills']]:
                return False
        return True