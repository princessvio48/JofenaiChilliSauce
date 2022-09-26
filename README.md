# jofenai pilipili documentation
### requirements
1. Python 3.10.4 and above 
2. django 4.0.4
3. virtualenv
3. postgres database management systems

### installation of different requirements
[install django](https://docs.djangoproject.com/en/4.1/intro/install/) this link contain installation of
* python
* django
* virtualenv
.

[install postgres](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/) this link instruct how to install postgres
.

## note
if you add product must given status to true automatically field of that product will not be shipped.
must be yes among(yes, unknown and no options)


### creating super user move to the base directory of project and run the command
###### python manage.py createsuperuser 
then provide
* username
* email
* password
* confirm password then enter

After creating superuser you can login in system and adding products and test for ordering, by creating another user or using anonymous user. Because we success to process order for both user

