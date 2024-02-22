from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class BootCourse(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, blank=True,null=True)
    description = models.TextField()
    instructor = models.CharField(max_length=50)
    image = models.ImageField(upload_to='itie_img/', null=True, blank=True)
    video = models.FileField(upload_to='itie_videos/',null=True, blank=True)
    price=models.FloatField(null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    duration_field = models.DurationField(default=timezone.timedelta)
    watch_percent = models.FloatField(blank=True,null=True)
    status_choices = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('draft', 'Draft'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    carriculum_title = models.CharField(max_length=100, default=False)
    carriculum_desc =  models.TextField(default=False)
    brochure = models.FileField(upload_to='bootcamp_brochure',null=True, blank=True)
    is_wep_main = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class BootBatch(models.Model):
    batch_name = models.CharField(max_length=100)
    course = models.ForeignKey(BootCourse, on_delete=models.CASCADE , null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def _str_(self):
        return f"{self.course.title} - Batch {self.id}"
    
class testimonial(models.Model):
    image = models.ImageField(upload_to='itie_testimonials',null=True,blank=True)
    name = models.CharField(max_length=100, null =True)
    designation = models.CharField(max_length =100 , null=True )
    text = models.TextField(null = True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.name