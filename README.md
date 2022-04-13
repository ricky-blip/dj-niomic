# dj-niomic
Course Niomic : Django

1. Membuat Project Pertama Django\
    `django-admin startproject mysite` > **mysite** adalah nama dari project.    

    - masuk ke direktori **mysite**.
    - jalankan server lokal dari Django\
        ` python manage.py runserver `

2. Membuat Aplikasi Django\
    `python manage.py startapp niomic` > **niomic** adalah nama dari aplikasi.

3. Mendaftarkan Aplikasi **niomic** ke Django
    - Pada direktori project **mysite** terdapat file **setting.py**
    - Pada bagian **INSTALLED_APPS =** pada file **setting.py** daftarkan aplikasi **niomic**

4. Admin Interface yang ada di Django
    - Inisialisasi sebuah database.
        - masuk ke direktori **mysite**\
            command : `python manage.py migrate` 
        - membuat SuperUser\
            command : `python manage.py createsuperuser`\
                Username = niomic\
                Email address = niomic@django.com\
                password = niomic
    - lalu jalankan server lokal dari Django\
        ` python manage.py runserver `

5. Membuat View pada Django
   - pada direktori aplikasi **niomic**
        - masuk ke **views.py** 
        - import httpResponse `from django.http import HttpResponse`
        - buat method dengan nama **index** dengan parameter **request** lalu return **HttpResponse** nya
            ```
                def index(request):
                    return HttpResponse("Hello World")
            ```

6. URL Mapping
   - pada direktori aplikasi **niomic**
     - buat file baru dengan nama **urls.py**
     - masuk ke **urls.py**
       - import url path `from django.urls import path` 
       - import views `from . import views`
       - buat url pattern
            ```
                urlpatterns = [
                    path('', views.index)
                ]
            ```
    - Merujuk akar dari url django
      - masuk ke direktori **mysite**
      - masuk ke **urls.py**
        - tambahkan import include pada django.urls
            ```
                from django.contrib import admin
                from django.urls import include,path
            ``` 
        - tambahkan path baru di url pattern, menuju ke aplikasi **niomic** -> urls.py
            ```
                urlpatterns = [
                    path('niomic/', include('niomic.urls')),
                    path('admin/', admin.site.urls),
                ]
            ```
            
7. 

