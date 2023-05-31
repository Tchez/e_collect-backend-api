from django.contrib import messages
from django.shortcuts import redirect
from django.views import View


class UpdatePassword(View):
    def post(self, request, *args, **kwargs):
        try:
            data = request.POST
            new_password = data.get("new-password")
            check_password = data.get("confirm-password")

            if new_password == check_password:
                request.user.set_password(new_password)
                request.user.save()
                return redirect("core:login")

        except Exception as error:
            messages.error(request, "Your password was successfully updated!")
            print(f"Error: {error}")
            return redirect("core:profile")
