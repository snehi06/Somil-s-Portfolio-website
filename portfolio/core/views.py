from django.shortcuts import render
from .models import Profile, Education, Experience, Project, SkillCategory, Research, Achievement

def index(request):
    profile = Profile.objects.first()
    education = Education.objects.all().order_by('-id')
    experience = Experience.objects.all()
    projects = Project.objects.all().order_by('-id')
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    research = Research.objects.all()
    achievements = Achievement.objects.all()

    context = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'projects': projects,
        'skill_categories': skill_categories,
        'research': research,
        'achievements': achievements,
    }
    return render(request, 'core/index.html', context)
