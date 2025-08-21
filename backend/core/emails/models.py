from django.db import models


class Lead(models.Model):
    recipient_name = models.CharField(max_length=100)  # John Doe
    company = models.CharField(max_length=100)         # TechCorp
    role = models.CharField(max_length=100)            # CTO
    job_title = models.CharField(max_length=100)       # AI Engineer
    applicant_name = models.CharField(max_length=100)  # Tulshidas Uikey
    skills = models.TextField()                        # Python, Django, React, AI/ML projects
    portfolio = models.URLField(blank=True, null=True) # GitHub link
    why_interested = models.TextField()               # Why interested in the role
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} applying to {self.company} for {self.job_title}"

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company}"

class GeneratedEmail(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="emails")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email for {self.lead.name}"
