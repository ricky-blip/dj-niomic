# dj-niomic
Course Niomic : Django

1. Membuat Project Pertama Django.\
    `django-admin startproject mysite` > mysite adalah nama dari project. \
    

    - masuk ke direktori **mysite**. \
    - jalankan server lokal dari Django. \
        ` python manage.py runserver `

2. Membuat Aplikasi Django.\
    `python manage.py startproject niomic` > niomic adalah nama dari aplikasi. \

3. Mendaftarkan Aplikasi **niomic** ke django. \
    - Pada direktori project **mysite** terdapat file **setting.py**
    - Pada bagian **INSTALLED_APPS =** pada file **setting.py** daftarkan aplikasi **niomic**