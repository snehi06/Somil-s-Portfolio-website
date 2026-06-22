from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    resume_link = models.URLField(blank=True, null=True)
    hero_text = models.CharField(max_length=300, blank=True, default='')
    about_text = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    is_present = models.BooleanField(default=False)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['-id'] # Simple ordering

    def __str__(self):
        return f"{self.role} at {self.company}"

class Project(models.Model):
    name = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=300)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Skill Categories"
        
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    
    def __str__(self):
        return self.name

class Research(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Research"
        
    def __str__(self):
        return self.title

class Achievement(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description[:50]
