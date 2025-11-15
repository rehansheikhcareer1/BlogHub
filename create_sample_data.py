"""
Script to create sample data for BlogHub
Run this to populate the database with categories, tags, and sample posts
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Category, Tag, Post
from django.utils.text import slugify

def create_sample_data():
    print("Creating sample data for BlogHub...")
    
    # Create superuser if doesn't exist
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@bloghub.com',
            password='admin123'
        )
        print("✓ Admin user created (username: admin, password: admin123)")
    else:
        admin = User.objects.get(username='admin')
        print("✓ Admin user already exists")
    
    # Create sample users
    sample_users = [
        {'username': 'john_doe', 'email': 'john@example.com', 'password': 'pass123'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'password': 'pass123'},
        {'username': 'mike_wilson', 'email': 'mike@example.com', 'password': 'pass123'},
    ]
    
    users = []
    for user_data in sample_users:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(**user_data)
            users.append(user)
            print(f"✓ User created: {user_data['username']}")
        else:
            users.append(User.objects.get(username=user_data['username']))
    
    # Create categories
    categories_data = [
        {'name': 'Technology', 'description': 'Latest tech trends, gadgets, and innovations'},
        {'name': 'Lifestyle', 'description': 'Health, fitness, and daily living tips'},
        {'name': 'Travel', 'description': 'Explore the world and travel guides'},
        {'name': 'Food & Cooking', 'description': 'Recipes, restaurants, and culinary adventures'},
        {'name': 'Business', 'description': 'Entrepreneurship, startups, and business insights'},
        {'name': 'Education', 'description': 'Learning resources and educational content'},
        {'name': 'Entertainment', 'description': 'Movies, music, games, and pop culture'},
        {'name': 'Sports', 'description': 'Sports news, analysis, and updates'},
    ]
    
    categories = []
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'slug': slugify(cat_data['name']),
                'description': cat_data['description']
            }
        )
        categories.append(category)
        if created:
            print(f"✓ Category created: {cat_data['name']}")
    
    # Create tags
    tags_data = [
        'Python', 'Django', 'JavaScript', 'React', 'AI', 'Machine Learning',
        'Web Development', 'Mobile Apps', 'Cloud Computing', 'DevOps',
        'Health', 'Fitness', 'Nutrition', 'Yoga', 'Meditation',
        'Travel Tips', 'Adventure', 'Photography', 'Culture',
        'Recipes', 'Cooking Tips', 'Restaurants', 'Food Review',
        'Startup', 'Marketing', 'Finance', 'Leadership',
        'Tutorial', 'Tips & Tricks', 'How-to', 'Guide'
    ]
    
    tags = []
    for tag_name in tags_data:
        tag, created = Tag.objects.get_or_create(
            name=tag_name,
            defaults={'slug': slugify(tag_name)}
        )
        tags.append(tag)
        if created:
            print(f"✓ Tag created: {tag_name}")
    
    # Create sample posts
    sample_posts = [
        {
            'title': 'Getting Started with Django: A Complete Guide',
            'content': '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

In this comprehensive guide, we'll walk through everything you need to know to get started with Django. From installation to creating your first project, we've got you covered.

Why Choose Django?

Django comes with a lot of built-in features that make web development easier. It includes an ORM (Object-Relational Mapping) system, authentication, admin interface, and much more. This means you can build powerful web applications quickly without writing boilerplate code.

Setting Up Your Environment

First, make sure you have Python installed on your system. Django works with Python 3.8 and above. You can install Django using pip, Python's package manager.

Creating Your First Project

Once Django is installed, you can create a new project using the django-admin command. This will set up the basic structure of your Django application with all the necessary files and folders.

Understanding Django's Architecture

Django follows the MVT (Model-View-Template) pattern. Models define your data structure, Views handle the business logic, and Templates render the HTML. This separation of concerns makes your code more maintainable and scalable.

Conclusion

Django is an excellent choice for building web applications. Its batteries-included philosophy means you can focus on building features rather than infrastructure. Start your Django journey today!''',
            'excerpt': 'Learn Django from scratch with this comprehensive guide covering installation, setup, and core concepts.',
            'category': categories[0],  # Technology
            'tags': [tags[0], tags[1], tags[6], tags[24]],  # Python, Django, Web Development, Tutorial
            'author': admin,
            'status': 'published',
            'views': 245,
        },
        {
            'title': '10 Healthy Habits to Transform Your Life',
            'content': '''Living a healthy lifestyle doesn't have to be complicated. Small, consistent changes can lead to significant improvements in your overall well-being. Here are 10 habits that can transform your life.

1. Start Your Day with Water

Drinking a glass of water first thing in the morning helps kickstart your metabolism and hydrate your body after hours of sleep. Add a slice of lemon for extra benefits.

2. Move Your Body Daily

You don't need to spend hours at the gym. Even 30 minutes of walking, yoga, or dancing can make a huge difference in your physical and mental health.

3. Eat More Whole Foods

Focus on incorporating more fruits, vegetables, whole grains, and lean proteins into your diet. These nutrient-dense foods provide the energy and nutrients your body needs.

4. Practice Mindfulness

Take a few minutes each day to meditate, practice deep breathing, or simply sit in silence. This helps reduce stress and improve mental clarity.

5. Get Quality Sleep

Aim for 7-9 hours of sleep each night. Create a bedtime routine and stick to it. Your body needs this time to repair and recharge.

Remember, consistency is key. Start with one or two habits and gradually add more as they become part of your routine.''',
            'excerpt': 'Discover 10 simple yet powerful habits that can dramatically improve your health and well-being.',
            'category': categories[1],  # Lifestyle
            'tags': [tags[10], tags[11], tags[12], tags[25]],  # Health, Fitness, Nutrition, Tips & Tricks
            'author': users[0] if users else admin,
            'status': 'published',
            'views': 189,
        },
        {
            'title': 'Top 5 Hidden Gems in Southeast Asia',
            'content': '''Southeast Asia is known for its popular destinations like Bangkok, Bali, and Singapore. But beyond these tourist hotspots lie incredible hidden gems waiting to be discovered.

1. Luang Prabang, Laos

This UNESCO World Heritage town offers a perfect blend of natural beauty and cultural richness. Wake up early to witness the daily alms-giving ceremony and explore stunning waterfalls nearby.

2. Hoi An, Vietnam

While not entirely unknown, Hoi An's ancient town charm and lantern-lit streets create a magical atmosphere. The tailor shops here are world-famous, and the food scene is incredible.

3. Koh Rong, Cambodia

This island paradise offers pristine beaches and bioluminescent plankton. It's less developed than Thailand's islands, giving you a more authentic beach experience.

4. Pai, Thailand

Nestled in the mountains of northern Thailand, Pai is a haven for backpackers and nature lovers. Hot springs, waterfalls, and a laid-back vibe make it special.

5. Siquijor, Philippines

Known for its mystical reputation, this island offers beautiful beaches, waterfalls, and a glimpse into Filipino culture away from the crowds.

Each of these destinations offers unique experiences that will make your Southeast Asian adventure unforgettable.''',
            'excerpt': 'Explore 5 amazing destinations in Southeast Asia that most tourists miss but absolutely shouldn\'t.',
            'category': categories[2],  # Travel
            'tags': [tags[15], tags[16], tags[17], tags[26]],  # Travel Tips, Adventure, Photography, How-to
            'author': users[1] if len(users) > 1 else admin,
            'status': 'published',
            'views': 312,
        },
        {
            'title': 'The Ultimate Guide to Italian Pasta Making',
            'content': '''There's something magical about homemade pasta. The texture, the taste, the satisfaction of creating something from scratch – it's an experience every food lover should have.

The Basics of Pasta Dough

Traditional Italian pasta is made with just two ingredients: flour and eggs. The ratio is typically 100g of flour per egg. Use tipo 00 flour if you can find it, as it creates the smoothest texture.

Kneading and Resting

Knead the dough for about 10 minutes until it's smooth and elastic. Then let it rest for at least 30 minutes. This allows the gluten to relax, making it easier to roll out.

Rolling and Shaping

You can use a pasta machine or a rolling pin. The key is to roll it thin enough to see your hand through it. Then cut it into your desired shape – fettuccine, tagliatelle, or pappardelle.

Cooking Fresh Pasta

Fresh pasta cooks much faster than dried – usually just 2-3 minutes in boiling salted water. It should be al dente, with a slight bite to it.

Sauce Pairing

Different pasta shapes pair better with different sauces. Thicker sauces work well with wider noodles, while lighter sauces complement thinner pasta.

Making pasta from scratch might seem intimidating, but with practice, it becomes second nature. Your family and friends will be impressed!''',
            'excerpt': 'Master the art of making authentic Italian pasta from scratch with this detailed guide.',
            'category': categories[3],  # Food & Cooking
            'tags': [tags[19], tags[20], tags[21], tags[24]],  # Recipes, Cooking Tips, Restaurants, Tutorial
            'author': users[2] if len(users) > 2 else admin,
            'status': 'published',
            'views': 156,
        },
        {
            'title': 'Building a Successful Startup: Lessons from the Trenches',
            'content': '''Starting a business is one of the most challenging yet rewarding experiences you can have. After building and scaling multiple startups, here are the key lessons I've learned.

1. Solve a Real Problem

Don't build a solution looking for a problem. Start with a genuine pain point that people are willing to pay to solve. Talk to potential customers before writing a single line of code.

2. Build an MVP First

Your first version doesn't need to be perfect. Build a Minimum Viable Product that solves the core problem, then iterate based on user feedback.

3. Focus on One Thing

It's tempting to add features and expand quickly, but focus is crucial in the early stages. Do one thing exceptionally well before diversifying.

4. Hire Slowly, Fire Fast

Your team can make or break your startup. Take time to find the right people, but don't hesitate to let go of those who aren't working out.

5. Cash is King

No matter how great your idea is, you need to manage your finances carefully. Know your burn rate and always have a runway of at least 6 months.

6. Listen to Customers

Your customers will tell you what they need if you listen. Regular feedback sessions and user testing are invaluable.

The startup journey is a marathon, not a sprint. Stay persistent, stay focused, and keep learning.''',
            'excerpt': 'Real-world lessons and practical advice for entrepreneurs building their first startup.',
            'category': categories[4],  # Business
            'tags': [tags[23], tags[24], tags[25], tags[26]],  # Startup, Marketing, Finance, Leadership
            'author': admin,
            'status': 'published',
            'views': 278,
        },
    ]
    
    for post_data in sample_posts:
        post_tags = post_data.pop('tags')
        post, created = Post.objects.get_or_create(
            title=post_data['title'],
            defaults={
                **post_data,
                'slug': slugify(post_data['title'])
            }
        )
        if created:
            post.tags.set(post_tags)
            # Add some likes
            if users:
                for user in users[:2]:
                    post.likes.add(user)
            print(f"✓ Post created: {post_data['title']}")
    
    print("\n" + "="*50)
    print("✅ Sample data created successfully!")
    print("="*50)
    print("\nYou can now:")
    print("1. Login to admin: http://127.0.0.1:8001/admin/")
    print("   Username: admin")
    print("   Password: admin123")
    print("\n2. View the website: http://127.0.0.1:8001/")
    print("\n3. Sample users (password: pass123):")
    print("   - john_doe")
    print("   - jane_smith")
    print("   - mike_wilson")

if __name__ == '__main__':
    create_sample_data()
