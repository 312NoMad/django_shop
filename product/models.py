from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Category Name'))
    description = models.TextField(verbose_name=_('Category Description'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    tags = models.ManyToManyField('product.Tag', verbose_name=_('Tags'), related_name='category_tags')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Product Name'))
    description = models.TextField(verbose_name=_('Product Description'), blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Product Price'))
    image = models.ImageField(blank=True, null=True, upload_to='media/', verbose_name=_('Product Image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, related_name='products', verbose_name=_('Product Category'),
        blank=True, null=True
    )
    tags = models.ManyToManyField('product.Tag', verbose_name=_('Tags'), related_name='product_tags',
                                  blank=True, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Tag name'))

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews',
                                verbose_name=_('review product'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews',
                             verbose_name=_('review user'))
    text = models.TextField(verbose_name=_('review text'), blank=True, null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(10)], verbose_name=_('review rating'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

