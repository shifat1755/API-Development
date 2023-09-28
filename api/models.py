from django.db import models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    locations=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('Non IT','Non IT'),
                                                  ('Mobiles Phones', 'Mobile Phones')
                                                  ))
    addd_data=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + ", add: "+self.locations

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default="default@example.com")
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(
        max_length=50,
        choices=(
            ('Manager', 'Manager'),
            ('Software Developer', 'sd'),
            ('Project lead', 'pl')
        )
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)