
from django.shortcuts import render

def home(request):
    users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22},
    ]
    return render(request, "index.html", {"title": "User List", "users": users})