from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    """
    defines category of apps 
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "category"


class SubCategory(models.Model):
    """
    defines subcategory of apps 
    """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "subcategory"


class App(models.Model):
    """
    defines an app with points rewarded 
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/app_images/')
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
    Profile of a user, used built-in User model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class TotalPoints(models.Model):
    """
    defines total points earned by a User, used Profile model
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.profile.user.username}'s total points"


class Task(models.Model):
    """
    defines a task that a user can complete to earn points
    """
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=PENDING)
    points = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username}'s task for {self.app.name} ({self.app.points} points)"

    def save(self, *args, **kwargs):
        if self.status == Task.COMPLETED:
            total_points, created = TotalPoints.objects.get_or_create(
                profile=self.user.profile)
            total_points.points += self.app.points
            total_points.save()
        super(Task, self).save(*args, **kwargs)


class Screenshot(models.Model):
    """
    user uploads screenshot as proof of completing the task
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/task_screenshots/')

    def save(self, *args, **kwargs):
        self.task.status = Task.COMPLETED
        self.task.save()
        super(Screenshot, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    creates a new Profile object for each new user object
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_total_points(sender, instance, created, **kwargs):
    """
    creates a TotalPoints object for each new Profile object
    """
    if created:
        TotalPoints.objects.create(profile=instance)
