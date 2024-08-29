from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.title)}-{i}"
                if not Category.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.FloatField()
    discount = models.PositiveIntegerField(default=0)
    is_liked = models.ManyToManyField(User, related_name='liked_products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.name)}-{i}"
                if not Product.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(Product, self).save(*args, **kwargs)

    @property
    def discounted_price(self):
        if self.discount:
            return self.price * (1 - (self.discount / 100))
        return self.price

    def __str__(self):
        return self.name


class Rating(BaseModel):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    value = models.CharField(max_length=25, choices=RatingChoices.choices, default=RatingChoices.One.value)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'product'], name='unique_rating'), ]


class Image(BaseModel):
    is_primary = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product.name


class Comment(BaseModel):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    media_file = models.FileField(upload_to='comments/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name


class Key(BaseModel):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Value(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Attribute(BaseModel):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.key.name}: {self.value.name}"
