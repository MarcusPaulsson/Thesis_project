class JobMarketplace:
    """
    A class to manage job postings and resume submissions.
    """

    def __init__(self):
        """
        Initializes the JobMarketplace with empty lists for job listings and resumes.
        """
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        """
        Posts a new job listing.

        Args:
            job_title (str): The title of the job.
            company (str): The company offering the job.
            requirements (list): A list of required skills.
        """
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job):
        """
        Removes a job listing.

        Args:
            job (dict): The job listing to remove.  It must be an identical dictionary
                        to a job listing already in the job_listings list.
        """
        try:
            self.job_listings.remove(job)
        except ValueError:
            # Job not found in the list.  It's arguably better to not raise an
            # error in this case, as the desired outcome (job not being present)
            # is already achieved.  However, for debugging purposes, it might
            # be useful to log this.
            pass

    def submit_resume(self, name, skills, experience):
        """
        Submits a resume to the marketplace.

        Args:
            name (str): The name of the applicant.
            skills (list): A list of skills the applicant possesses.
            experience (str): A description of the applicant's experience.
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

        Args:
             resume (dict): The resume to withdraw. It must be an identical dictionary
                        to a resume already in the resumes list.
        """
        try:
            self.resumes.remove(resume)
        except ValueError:
            # Resume not found. Similar to remove_job, handle silently or log.
            pass

    def search_jobs(self, criteria):
        """
        Searches for jobs that match the given criteria.

        Args:
            criteria (str): The skill to search for in job requirements.

        Returns:
            list: A list of job listings that include the criteria in their requirements.
        """
        results = []
        for job in self.job_listings:
            if criteria in job['requirements']:
                results.append(job)
        return results

    def get_job_applicants(self, job):
        """
        Retrieves a list of applicants who match the requirements of a given job.

        Args:
            job (dict): The job listing to find applicants for.

        Returns:
            list: A list of resumes that match the job's requirements.
        """
        applicants = []
        for resume in self.resumes:
            if self.matches_requirements(resume, job['requirements']):
                applicants.append(resume)
        return applicants

    def matches_requirements(self, resume, requirements):
        """
        Checks if a resume matches the given requirements.  All requirements must be
        present in the resume's skills for it to be considered a match.

        Args:
            resume (dict): The resume to check.
            requirements (list): A list of required skills.

        Returns:
            bool: True if the resume meets all requirements, False otherwise.
        """
        return all(requirement in resume['skills'] for requirement in requirements)