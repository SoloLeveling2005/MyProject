import psycopg2
from django.shortcuts import render


# from .models import BD


def home(request):
    title = request.POST["title"]
    description = request.POST["description"]

    connection = psycopg2.connect(user="postgres",
                                  password="Solo2005",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    cursor.execute("""SELECT id, title, description FROM public."ToDoTasks";""")
    data_sql = cursor.fetchall()
    data = []
    for i in data_sql:
        data.append({"title": i[1], "description": i[2]})
    if title in request.POST and title is not None and description is not None:
        title = request.POST["title"]
        description = request.POST["description"]

        data_all = {"title": title, "description": description}

        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO public."ToDoTasks"( title, description) VALUES ('{title}', '{description}');""")
        connection.commit()
        print(data_all)
        title = None
        description = None
        return render(request, "home.html", {
            "data": data,
        })

    else:
        title = None
        description = None
        return render(request, "home.html", {
            "data": data,
        })
