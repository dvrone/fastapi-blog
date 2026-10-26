from datetime import datetime, timedelta

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author": "John Smith",
        "title": "Getting Started with Python",
        "content": "Python is a beginner-friendly programming language with a wide range of applications, including web development, data science, and automation.",
        "date_posted": datetime.now() - timedelta(days=3),
    },
    {
        "id": 2,
        "author": "Emily Johnson",
        "title": "Building Your First Web App with Flask",
        "content": "Flask is a lightweight Python web framework that allows developers to build web applications quickly and efficiently.",
        "date_posted": datetime.now() - timedelta(days=2),
    },
    {
        "id": 3,
        "author": "Michael Brown",
        "title": "The Benefits of Daily Planning",
        "content": "Planning your tasks ahead of time helps you manage your schedule, stay organized, and focus on what matters most.",
        "date_posted": datetime.now() - timedelta(days=1),
    },
    {
        "id": 4,
        "author": "Sophia Wilson",
        "title": "Git and GitHub for Developers",
        "content": "Git helps developers track changes in their code, while GitHub provides a platform for hosting projects and collaborating with others.",
        "date_posted": datetime.now() - timedelta(hours=5),
    },
    {
        "id": 5,
        "author": "Daniel Taylor",
        "title": "Start Small, Build Something Great",
        "content": "When learning to code, start with small projects. Focus on making them work first, then gradually improve their functionality and design.",
        "date_posted": datetime.now(),
    },
]


# @app.get('/', response_class=HTMLResponse)
# @app.get('/posts', response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    # return {'message': 'Hello World!'}
    return f"<h1>{posts[-1]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
