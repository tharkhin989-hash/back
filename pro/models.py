from django.db import models
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=255,null=True, blank=True)
    password = models.CharField(max_length=255,null=True, blank=True)
    role= models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table= 'users'
        def __str__ (self):
         return User.name

class Category(models.Model):
    category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'category'
        def __str__(self):
            return self.name

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'post'
        def __str__(self):
            return self.title

class Comment(models.Model):
    STATUS_CHOICES = [
            ('pending','pending'),
            ('approved','approved'),
            ('rejected','rejected'),
        ]
    comment_id= models.AutoField(primary_key=True)
    status= models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    class Meta:
        db_table = 'comment'
        def __str__(self):
            return self.content

class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    visibility = models.CharField(
        max_length=10,
        choices=[
            ('public', 'Public'),
            ('private', 'Private'),
        ],
        default='public'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.phone

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    tag_type = models.CharField(
        max_length=20,
        choices=[
            ('programming', 'Programming'),
            ('design', 'Design'),
            ('business', 'Business'),
            ('other', 'Other'),
        ]
    )

    class Meta:
        db_table = 'tag'

    def __str__ (self):
        return self.name

class PostTag(models.Model):
    post_tag_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_tag'

    def __str__ (self):
        return str(self.post)

class PostLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_like'

    def __str__(self):
        return str(self.user)