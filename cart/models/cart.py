from models import models


class Cart(models.Model):
    session_key = models.CharField(max_length=255)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
