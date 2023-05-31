import secrets
import string

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views import View


class ResetPassword(View):
    def get(self, request, *args, **kwargs):
        try:
            data = request.GET
            username = data.get("username")
            user = User.objects.get(username=username)
            email = data.get("email")
            alphabet = string.ascii_letters + string.digits
            password = "".join(secrets.choice(alphabet) for _ in range(10))
            user.set_password(password)
            user.save()
            print(password)
            # Send new password to email
            email = EmailMessage(
                "Rercuperação de Senha",
                f"Aqui está sua nova senha\n{password}",
                "guilherme.carvalho.carneiro@gmail.com",
                [
                    user.email,
                ],
            )
            email.send()

        except Exception as error:
            print(error)

        finally:
            return HttpResponse("Finalizado")
