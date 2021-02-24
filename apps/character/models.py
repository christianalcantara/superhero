from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Character(models.Model):
    created = models.DateTimeField(
        verbose_name=_("Created"), editable=False, blank=True, auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), editable=False, blank=True, auto_now=True
    )
    name = models.CharField(
        verbose_name=_("Name"), max_length=40, unique=True, db_index=True
    )
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    thumbnail = models.ImageField(
        verbose_name=_("Image Thumbnail"), upload_to="character", null=True
    )

    class Meta:
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")
        ordering = ("-created",)

    def __str__(self):
        return self.name

    @property
    def thumb_url(self):
        domain = settings.DOMAIN
        media_url = settings.MEDIA_URL
        return f"//{domain}{media_url}{self.thumbnail}"


class Favorite(models.Model):
    created = models.DateTimeField(
        verbose_name=_("Created"), editable=False, blank=True, auto_now_add=True
    )
    user = models.ForeignKey(
        verbose_name=_("User"), to=User, related_name="user+", on_delete=models.CASCADE
    )
    character = models.ForeignKey(
        verbose_name=_("Character"),
        to=Character,
        related_name="character+",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Favorite")
        verbose_name_plural = _("Favorites")

    def __str__(self):
        return f"{self.user.name} -> {self.character.name}"
