from django.db import models
# from multiselectfield import MultiSelectField
# MATERIAL_CATEGORIES = (
#             	('note book', 'Note Book'),
#             	('pens', 'Pens'),
#             	('highlighters', 'Highlighters'),
#             	('Ruler', 'Ruler'),
#             	('Stapler staples', 'Stapler staples'),
#             	('Glue', 'Glue'),
#             	('Scissors', 'Scissors'),
#         )

# materials_provide = MultiSelectField(blank=True, choices=MATERIAL_CATEGORIES)


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Courses(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

# class Materials_provide(models.Model):
#
#
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name

class Person(models.Model):

        GENDER_CHOICES =(
            ('male', 'Male',),
            ('female', 'Female',),
                ('other','other'),
        )
        PURPOSE_CHOICES = (
            ('enquiry', 'For Enquiry',),
            ('place_order', 'Place_Order',),
            ('return', 'Return'),
            ('other','Other'),
        )
        # MATERIAL_CATEGORIES = (
        #     ('note book', 'Note Book'),
        #     ('pens', 'Pens'),
        #     ('highlighters', 'Highlighters'),
        #     ('Ruler', 'Ruler'),
        #     ('Stapler staples', 'Stapler staples'),
        #     ('Glue', 'Glue'),
        #     ('Scissors', 'Scissors'),
        # )


        Name = models.CharField(max_length = 20, blank = False, null = False )
        DOB = models.DateField( help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
        AGE = models.IntegerField()
        GENDER = models.CharField(max_length=10, choices=GENDER_CHOICES,)
        PHONE_NUMBER = models.CharField(max_length = 10, blank = False,null = False)
        MAIL_ID =models.EmailField()
        ADDRESS = models.CharField(max_length=200,blank = False, null = False)
        department=models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
        courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
        Purpose=models.CharField(max_length=20, choices=PURPOSE_CHOICES,)
        materials_provide=models.CharField(max_length=255,blank = False, null = False)
        def __str__(self):
            return self.Name
        # materials_provide=MultiSelectField(choices= MATERIAL_CATEGORIES)
