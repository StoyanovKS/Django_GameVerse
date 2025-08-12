from django.core.validators import MinLengthValidator, RegexValidator, MaxLengthValidator
from django.db import models

nick_validator = RegexValidator(
    regex=r"^[A-Za-z0-9]+$",
    message="Nickname must contain only letters and digits!"
)

class Player(models.Model):
    nickname = models.CharField(
        max_length=60,
        unique=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(60), nick_validator],
        help_text="*Allowed nicknames contain letters and digits.",
        error_messages={"unique": "That nickname is already in use!"},
    )
    email = models.CharField(
        max_length=60,
        unique=True,
        error_messages={"unique": "That email is already registered!"},
    )
    achievements = models.TextField(
        blank=True, null=True,
        help_text="*Share your achievements."
    )
    is_pro = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
