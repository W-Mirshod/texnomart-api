import json
import os

from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone

from product.models import Product, Category
from root.settings import DEFAULT_FROM_EMAIL, BASE_DIR


@receiver(post_save, sender=Product)
def saved_product(sender, instance, **kwargs):
    subject = 'Product has been created'
    message = (f"Category \"{instance.name}\" has been created\nCheck this out: http://51.21.11.250:8000/"
               f" \n\nCreated Time: {instance.created_at}\n\n\nAdmin Name: admin\nAdmin Password: 123")
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = ['trading3526@gmail.com']

    send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=Category)
def saved_product(sender, instance, **kwargs):
    subject = 'Category has been created'
    message = (f"Category \"{instance.title}\" has been created\nCheck this out: http://51.21.11.250:8000/"
               f" \n\nCreated Time: {instance.created_at}\n\n\nAdmin Name: admin\nAdmin Password: 123")
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = ['trading3526@gmail.com']

    send_mail(subject, message, from_email, recipient_list)


@receiver(pre_delete, sender=Product)
def deleted_product(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'archives/product', f"{instance.slug}_{instance.id}.json")
    time_utc = timezone.now()
    time_local = timezone.localtime(time_utc)

    product_info = {
        'id': instance.id,
        'name': instance.name,
        'slug': instance.slug,
        'description': instance.description,
        'price': instance.price,
        'discount': instance.discount,
        'created_at': str(instance.created_at),
        'updated_at': str(instance.updated_at),
        'deleted_at': str(time_local), }

    with open(file_path, 'w') as file:
        json.dump(product_info, file, indent=4)

    print(f"Product \"{instance.name}\" has deleted")


@receiver(pre_delete, sender=Category)
def deleted_product(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'archives/category', f"{instance.slug}_{instance.id}.json")
    time_utc = timezone.now()
    time_local = timezone.localtime(time_utc)

    product_info = {
        'id': instance.id,
        'title': instance.title,
        'slug': instance.slug,
        'deleted_at': str(time_local), }

    with open(file_path, 'w') as file:
        json.dump(product_info, file, indent=4)

    print(f"Category \"{instance.title}\" has deleted")
