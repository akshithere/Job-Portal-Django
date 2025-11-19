from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from jobs.models import Job, UserProfile


class Command(BaseCommand):
    help = 'Creates dummy jobs and a recruiter user for testing'

    def handle(self, *args, **kwargs):
        # Create a dummy recruiter if it doesn't exist
        recruiter_username = 'demo_recruiter'
        if not User.objects.filter(username=recruiter_username).exists():
            recruiter = User.objects.create_user(
                username=recruiter_username,
                email='recruiter@demo.com',
                password='demo1234',
                first_name='Demo',
                last_name='Recruiter'
            )
            UserProfile.objects.create(
                user=recruiter,
                user_type='recruiter',
                company='Tech Innovations Inc.',
                phone='+1-555-0100'
            )
            self.stdout.write(self.style.SUCCESS(f'Created recruiter: {recruiter_username} (password: demo1234)'))
        else:
            recruiter = User.objects.get(username=recruiter_username)
            self.stdout.write(self.style.WARNING(f'Recruiter {recruiter_username} already exists'))

        # Dummy job data
        dummy_jobs = [
            {
                'title': 'Senior Software Engineer',
                'company': 'Tech Innovations Inc.',
                'location': 'San Francisco, CA',
                'job_type': 'full_time',
                'salary_range': '$120,000 - $180,000',
                'description': '''We are seeking a talented Senior Software Engineer to join our dynamic team.
You will be responsible for designing, developing, and maintaining scalable web applications.

Key Responsibilities:
- Design and implement new features
- Write clean, maintainable code
- Mentor junior developers
- Collaborate with cross-functional teams
- Participate in code reviews''',
                'requirements': '''Required Qualifications:
- 5+ years of software development experience
- Strong proficiency in Python and Django
- Experience with React or Vue.js
- Excellent problem-solving skills
- BS in Computer Science or related field

Preferred:
- Experience with cloud platforms (AWS, GCP, Azure)
- Knowledge of CI/CD pipelines
- Strong communication skills'''
            },
            {
                'title': 'Frontend Developer',
                'company': 'Creative Digital Agency',
                'location': 'New York, NY',
                'job_type': 'full_time',
                'salary_range': '$80,000 - $120,000',
                'description': '''Join our creative team as a Frontend Developer! You'll work on exciting projects for high-profile clients, creating beautiful and responsive user interfaces.

What You'll Do:
- Build responsive web applications
- Implement pixel-perfect designs
- Optimize applications for performance
- Collaborate with designers and backend developers''',
                'requirements': '''Must Have:
- 3+ years of frontend development experience
- Expert knowledge of HTML, CSS, and JavaScript
- Experience with React or Angular
- Understanding of responsive design
- Portfolio of previous work

Nice to Have:
- Experience with TypeScript
- Knowledge of CSS preprocessors (SASS, LESS)
- Familiarity with design tools (Figma, Sketch)'''
            },
            {
                'title': 'Data Scientist',
                'company': 'Analytics Pro',
                'location': 'Boston, MA',
                'job_type': 'full_time',
                'salary_range': '$100,000 - $150,000',
                'description': '''We're looking for a Data Scientist to help us unlock insights from complex datasets and drive business decisions.

Responsibilities:
- Analyze large datasets to identify trends
- Build predictive models
- Create data visualizations
- Present findings to stakeholders
- Collaborate with engineering teams''',
                'requirements': '''Requirements:
- Master's degree in Statistics, Math, or Computer Science
- 3+ years of data science experience
- Strong Python skills (pandas, scikit-learn, numpy)
- Experience with SQL and data warehousing
- Excellent analytical and communication skills

Preferred:
- PhD in related field
- Experience with deep learning frameworks
- Knowledge of big data technologies (Spark, Hadoop)'''
            },
            {
                'title': 'Product Manager',
                'company': 'StartUp Ventures',
                'location': 'Austin, TX',
                'job_type': 'full_time',
                'salary_range': '$90,000 - $130,000',
                'description': '''We're seeking a passionate Product Manager to lead our product development efforts and shape the future of our platform.

What You'll Do:
- Define product vision and strategy
- Manage product roadmap
- Work with engineering and design teams
- Conduct user research
- Analyze product metrics''',
                'requirements': '''Qualifications:
- 4+ years of product management experience
- Strong understanding of agile methodologies
- Excellent communication and leadership skills
- Data-driven decision maker
- Experience with product analytics tools

Bonus:
- Technical background
- Experience in SaaS products
- MBA or equivalent'''
            },
            {
                'title': 'UX/UI Designer',
                'company': 'Design Studio Pro',
                'location': 'Los Angeles, CA',
                'job_type': 'full_time',
                'salary_range': '$70,000 - $110,000',
                'description': '''Join our design team and create amazing user experiences for web and mobile applications.

Your Role:
- Design user interfaces for web and mobile
- Create wireframes and prototypes
- Conduct user research and testing
- Collaborate with developers and product managers
- Maintain design systems''',
                'requirements': '''What We're Looking For:
- 3+ years of UX/UI design experience
- Proficiency in Figma, Sketch, or Adobe XD
- Strong portfolio demonstrating your work
- Understanding of user-centered design principles
- Excellent visual design skills

Plus:
- Experience with design systems
- Basic HTML/CSS knowledge
- Motion design skills'''
            },
            {
                'title': 'DevOps Engineer',
                'company': 'Cloud Systems Inc.',
                'location': 'Seattle, WA',
                'job_type': 'full_time',
                'salary_range': '$110,000 - $160,000',
                'description': '''We need a skilled DevOps Engineer to help us build and maintain our infrastructure and deployment pipelines.

Responsibilities:
- Manage cloud infrastructure
- Build and maintain CI/CD pipelines
- Monitor system performance
- Implement security best practices
- Automate deployment processes''',
                'requirements': '''Required Skills:
- 4+ years of DevOps experience
- Strong knowledge of AWS or GCP
- Experience with Docker and Kubernetes
- Proficiency in scripting (Python, Bash)
- Understanding of infrastructure as code (Terraform, CloudFormation)

Preferred:
- Experience with monitoring tools (Prometheus, Grafana)
- Knowledge of security best practices
- Experience with microservices architecture'''
            },
            {
                'title': 'Marketing Intern',
                'company': 'Growth Marketing Co.',
                'location': 'Chicago, IL',
                'job_type': 'internship',
                'salary_range': '$20 - $25 per hour',
                'description': '''Great opportunity for students or recent graduates to gain hands-on marketing experience!

What You'll Learn:
- Social media marketing
- Content creation
- Email marketing campaigns
- Marketing analytics
- SEO basics''',
                'requirements': '''Looking For:
- Currently pursuing or recently completed degree in Marketing or related field
- Strong written communication skills
- Familiarity with social media platforms
- Creative and eager to learn
- Basic knowledge of marketing concepts

Bonus:
- Experience with Canva or Adobe Creative Suite
- Knowledge of Google Analytics
- Previous internship experience'''
            },
            {
                'title': 'Full Stack Developer',
                'company': 'Web Solutions LLC',
                'location': 'Remote',
                'job_type': 'contract',
                'salary_range': '$60 - $100 per hour',
                'description': '''6-month contract position for an experienced Full Stack Developer to work on a greenfield project.

Project Details:
- Build a new SaaS platform from scratch
- Work with modern tech stack
- Fully remote position
- Flexible hours''',
                'requirements': '''Must Have:
- 5+ years of full stack development
- Strong backend skills (Node.js or Python)
- Frontend expertise (React, Vue, or Angular)
- Experience with RESTful APIs
- Database design skills (SQL and NoSQL)
- Available for 6-month commitment

Nice to Have:
- Experience building SaaS products
- Knowledge of payment integration
- AWS/cloud experience'''
            },
            {
                'title': 'Customer Support Representative',
                'company': 'SupportTech Solutions',
                'location': 'Miami, FL',
                'job_type': 'part_time',
                'salary_range': '$18 - $22 per hour',
                'description': '''Join our customer support team and help our clients succeed! This is a part-time position, perfect for someone looking for flexible hours.

Responsibilities:
- Respond to customer inquiries via email and chat
- Troubleshoot customer issues
- Document customer interactions
- Provide product information
- Escalate complex issues when needed''',
                'requirements': '''Requirements:
- Excellent communication skills
- Patient and empathetic
- Problem-solving ability
- Computer proficient
- Available 20-25 hours per week

Preferred:
- Previous customer service experience
- Technical aptitude
- Bilingual (English/Spanish)'''
            },
            {
                'title': 'Mobile App Developer',
                'company': 'App Innovations',
                'location': 'Denver, CO',
                'job_type': 'full_time',
                'salary_range': '$95,000 - $140,000',
                'description': '''We're looking for a talented Mobile App Developer to build amazing iOS and Android applications.

What You'll Do:
- Develop native mobile applications
- Implement new features
- Optimize app performance
- Work with design and backend teams
- Participate in the entire app lifecycle''',
                'requirements': '''Qualifications:
- 3+ years of mobile development experience
- Proficiency in Swift and/or Kotlin
- Experience with RESTful APIs
- Understanding of mobile UI/UX principles
- Published apps in App Store or Google Play

Bonus:
- Experience with React Native or Flutter
- Knowledge of mobile security best practices
- Experience with app analytics'''
            }
        ]

        created_count = 0
        for job_data in dummy_jobs:
            # Check if job with same title already exists
            if not Job.objects.filter(title=job_data['title'], recruiter=recruiter).exists():
                Job.objects.create(
                    recruiter=recruiter,
                    **job_data
                )
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created job: {job_data["title"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Job already exists: {job_data["title"]}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} dummy jobs!'))
        self.stdout.write(self.style.SUCCESS(f'Total jobs in database: {Job.objects.count()}'))
