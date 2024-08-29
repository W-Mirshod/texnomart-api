from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product, Category
from root.settings import DEFAULT_FROM_EMAIL


@receiver(post_save, sender=Product)
def saved_product(sender, instance, **kwargs):
    subject = 'Product has been created'
    message = (f"Category {instance.name} has been created\nCheck this out: http://51.21.11.250:8000/"
               f" \n\nCreated Time: {instance.created_at}\n\n\nAdmin Name: admin\nAdmin Password: 123")
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = ['trading3526@gmail.com']

    send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=Category)
def saved_product(sender, instance, **kwargs):
    subject = 'Category has been created'
    message = (f"Category {instance.title} has been created\nCheck this out: http://51.21.11.250:8000/"
               f" \n\nCreated Time: {instance.created_at}\n\n\nAdmin Name: admin\nAdmin Password: 123")
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = ['trading3526@gmail.com']

    send_mail(subject, message, from_email, recipient_list)
