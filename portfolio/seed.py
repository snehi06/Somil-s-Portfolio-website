import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import Profile, Education, Experience, Project, SkillCategory, Skill, Research, Achievement

def seed_data():
    print("Clearing existing data...")
    Profile.objects.all().delete()
    Education.objects.all().delete()
    Experience.objects.all().delete()
    Project.objects.all().delete()
    SkillCategory.objects.all().delete()
    Skill.objects.all().delete()
    Research.objects.all().delete()
    Achievement.objects.all().delete()

    print("Seeding Profile...")
    Profile.objects.create(
        name="Somil Nema",
        email="somilnema29@gmail.com",
        phone="+91 8770577994",
        linkedin_url="#",
        github_url="#",
        hero_text="I build things for the web.",
        about_text="I am an aspiring Software Engineer studying B.Tech in Computer Science and Engineering at Medicaps University. I have a passion for building scalable web applications, optimizing performance, and crafting beautiful user interfaces. My journey in tech involves working extensively with modern web technologies to create impactful digital experiences."
    )

    print("Seeding Education...")
    Education.objects.create(
        institution="Medicaps University",
        degree="Bachelor of Technology in Computer Science and Engineering",
        start_date="August 2022",
        end_date="May 2026"
    )

    print("Seeding Experience...")
    Experience.objects.create(
        company="TECHNO CLUBS",
        role="PRESIDENT University",
        start_date="August 2025",
        is_present=True,
        description="• Led the University Techno Club, organizing technical workshops, coding events, and collaborative projects while coordinating with faculty and managing operations for an active member base.\n• Served as the central hub for five university tech clubs, managing all major events and activities, including large-scale hackathons and cross-club technical initiatives."
    )
    Experience.objects.create(
        company="Protons Hub",
        role="Software Developer Intern",
        location="Remote",
        start_date="January 2026",
        is_present=True,
        description="• Worked on building and improving web applications using Next.js, focusing on routing, performance, and overall user experience.\n• Handled API integration and data fetching, ensuring smooth communication between frontend and backend.\n• Used Supabase for backend tasks such as authentication, database management, and storage.\n• Built responsive UI components using React and Tailwind CSS, making sure the application works well across devices.\n• Fixed bugs and tested features regularly to ensure stability before deployment.\n• Collaborated with team members to understand requirements and deliver features on time."
    )

    print("Seeding Projects...")
    Project.objects.create(
        name="KratiKala",
        tech_stack="HTML5, JavaScript, CSS, JWT, Next.js",
        description="• Built an advanced content-generation platform using Next.js incorporating behavioral analysis techniques, delivering high-precision tone adaptation and style consistency for customized content delivery and enhanced overall user engagement.\n• Implemented a unified editor interface supporting instant previews and content exports, boosting user productivity through simplified controls and faster generation cycles."
    )
    Project.objects.create(
        name="Artisto",
        tech_stack="Next.js, React, Supabase, API Integration, Authentication",
        description="• Built the complete Artisto platform (artistoo.in) from scratch, including both user-facing website and admin panel.\n• Created an artist onboarding system where artists can register, manage their profiles, and update availability through a dedicated dashboard.\n• Implemented a calendar-based booking system to handle artist scheduling and user bookings in a simple and structured way.\n• Used Supabase for database, authentication, and backend operations, managing artist data, bookings, and user information.\n• Integrated APIs for handling authentication, bookings, and data flow between frontend and backend.\n• Tested and improved the application regularly by fixing bugs and refining features during development."
    )

    print("Seeding Skills...")
    lang_cat = SkillCategory.objects.create(name="Programming Languages")
    front_cat = SkillCategory.objects.create(name="Frontend Technologies")
    back_cat = SkillCategory.objects.create(name="Backend & Databases")
    tools_cat = SkillCategory.objects.create(name="Tools & Technologies")
    concept_cat = SkillCategory.objects.create(name="Concepts")

    for skill in ["JavaScript", "TypeScript", "Java", "SQL", "HTML", "CSS"]:
        Skill.objects.create(name=skill, category=lang_cat)
    for skill in ["React.js", "Next.js", "Tailwind CSS", "Framer Motion", "GSAP", "Responsive Web Design"]:
        Skill.objects.create(name=skill, category=front_cat)
    for skill in ["Supabase", "MongoDB", "MySQL", "REST APIs", "Next.js API Routes", "Authentication (JWT)"]:
        Skill.objects.create(name=skill, category=back_cat)
    for skill in ["Git", "GitHub", "Vercel", "Postman", "Socket.io", "Firebase", "VMware"]:
        Skill.objects.create(name=skill, category=tools_cat)
    for skill in ["API Integration", "State Management", "CRUD Operations", "Performance Optimization", "Debugging"]:
        Skill.objects.create(name=skill, category=concept_cat)

    print("Seeding Research...")
    Research.objects.create(
        title="Edge-to-Cloud Collaboration in Machine Learning",
        description="Conducted an in-depth study on collaborative ML systems across edge and cloud environments, analyzing federated learning, model deployment strategies, communication protocols (MQTT, CoAP, gRPC), and security frameworks. Identified how hybrid training, dynamic load balancing, and privacy-preserving methods improve latency, scalability, and real-time decision-making in IoT and autonomous systems."
    )

    print("Seeding Achievements...")
    Achievement.objects.create(description="Qualified as Top 35 finalist from 300+ teams in Technovate for India Ideathon by Times of India and Talrop.")
    Achievement.objects.create(description="Organized hackathon generating 23,000+ impressions on Unstop platform while collaborating with IMC Research and Development team.")
    Achievement.objects.create(description="Managed IEEE Medicaps University CSE as Mangement Head overseeing Rs.1,50,000 annual budget with 40+ team members and cost optimization strategies.")
    Achievement.objects.create(description="Served as IndoriX Community Head driving visual branding initiatives for InternX Internship Fair, enhancing student-corporate networking visibility.")

    print("Seeding complete!")

if __name__ == '__main__':
    seed_data()
