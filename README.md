# Demo Django Project

This is simple CRUD application that uses the Django framework. This project is based on the Django Workshop. To see full project that was the basis of the workshop, here is the [link](https://github.com/cr8ivecodesmith/djnotes2
)

## Requirements 
- Django. Recommended version used is provided in **requirements.txt** in case problems occur
- Virtualenv. It strongly recommended to always run in a sandboxed environment especially when working on mulitple projects. For more information please check out the [official documentation](https://virtualenv.pypa.io/en/stable/). 
    - Alternatively you can also use [conda environments](https://conda.io/)




## How to run : 

When the requirements have been installed first run the migration tool to initialize the database.

`python manage.py migrate`

 This uses SQLite for portability. 

Then : 

`python manage.py runserver`

## How it was done
**currently work in progress**


### Create the Notes App

`python manage.py startapp notes`

This will create a note app.

### Creating our model

we create our model

Under notes/models.py  

```python
class AuditModelMixin(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(AuditModelMixin):
    title = models.CharField(max_length=129, blank=True)
    note = models.TextField(blank=True)
```

Here we create an abstract class **AuditModelMixin**, a class that we will inherit for reuse some fields such as created_time and modified_time  

the **Note** class will be the model for the items we will be using

After creating our model, run

`python manage.py makemigrations`

This will generate sql migration scripts or files that will generate our tables. Then we will run 

`python manage.py migrate`

To apply the changes in the database

Now that we have our tables, we can proceed in creating our views and template. 


## Preparing the Templates

### The base Template

```html
<!DOCTYPE html>
<html>
<head>
    <title>Notes App {{ page_title }}</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>
<div class="container">
	<div class="row">
			<div class="col-md-12">		
				{% block content %}
				{% endblock %}
			</div>
	</div>
</div>
</body>
</html>
```
Save this file as base.html. This will serve as the page that we will extend for the other templates we will be using. We will then create those templates. Since the `{% block content %}` is where our content will go, just write the content you need on the template  you will write. 





TBA
