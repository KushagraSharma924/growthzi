def parse_resume(file):
    portfolio_data = {
        "hero": {
            "name": "John Doe",
            "title": "Full Stack Developer",
            "summary": "Passionate developer with 5+ years of experience building web applications"
        },
        "about": {
            "bio": "I'm a software engineer specializing in building high-load web applications with modern technologies.",
            "interests": ["Programming", "Machine Learning", "UI/UX Design"]
        },
        "skills": [
            {"name": "JavaScript", "level": "Expert"},
            {"name": "Python", "level": "Advanced"},
            {"name": "React", "level": "Expert"},
            {"name": "Flask", "level": "Advanced"},
            {"name": "SQL", "level": "Intermediate"}
        ],
        "experience": [
            {
                "company": "Tech Innovators",
                "position": "Senior Developer",
                "duration": "2021-Present",
                "description": "Leading development of enterprise SaaS platform"
            },
            {
                "company": "Digital Solutions",
                "position": "Web Developer",
                "duration": "2018-2021",
                "description": "Built responsive web applications for clients"
            }
        ],
        "education": [
            {
                "institution": "University of Technology",
                "degree": "BSc Computer Science",
                "year": "2018"
            },
            {
                "institution": "Online Academy",
                "degree": "Full Stack Web Development",
                "year": "2019"
            }
        ],
        "contact": {
            "email": "john.doe@example.com",
            "phone": "+1 234 567 8901",
            "linkedin": "linkedin.com/in/johndoe",
            "github": "github.com/johndoe"
        }
    }
    
    return portfolio_data


def translate_content(data, target_lang):
    def prefix_values(obj, lang):
        if isinstance(obj, dict):
            return {key: prefix_values(value, lang) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [prefix_values(item, lang) for item in obj]
        elif isinstance(obj, str):
            return f"[{lang}] {obj}"
        else:
            return obj
    
    return prefix_values(data, target_lang)


def get_price_for_country(country):
    conversion_rates = {
        'US': {'currency': 'USD', 'rate': 1.0},
        'CA': {'currency': 'CAD', 'rate': 1.35},
        'GB': {'currency': 'GBP', 'rate': 0.79},
        'EU': {'currency': 'EUR', 'rate': 0.91},
        'JP': {'currency': 'JPY', 'rate': 150.2},
        'AU': {'currency': 'AUD', 'rate': 1.52},
        'IN': {'currency': 'INR', 'rate': 83.1},
        'CN': {'currency': 'CNY', 'rate': 7.23},
        'BR': {'currency': 'BRL', 'rate': 5.47},
        'RU': {'currency': 'RUB', 'rate': 90.4}
    }
    
    base_price = 99.99
    
    if country not in conversion_rates:
        country = 'US'
    
    currency = conversion_rates[country]['currency']
    rate = conversion_rates[country]['rate']
    price = round(base_price * rate, 2)
    
    return {
        'product': 'Premium Subscription',
        'base_price_usd': base_price,
        'country': country,
        'currency': currency,
        'price': price
    }
