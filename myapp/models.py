from django.db import models

# Create your models here.
class create_crud_a_details(models.Model):
    item_name=models.CharField(max_length=100)
    item_discription=models.CharField(max_length=200)

    def __str__(self):
        return self.item_name
    

    
class create_crud_b_details(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=100)
    action=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

    
class create_crud_c_details(models.Model):
    name=models.CharField(max_length=100)
    discription=models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class create_crud_d_details(models.Model):
    person_name=models.CharField(max_length=50)
    person_emailid=models.EmailField(max_length=100)

    def __str__(self):
        return self.person_name 