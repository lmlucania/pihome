from django.contrib.auth import views
from apps.accounts.form import LoginForm, PasswordResetForm, SetPasswordForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


class LoginView(views.LoginView):
    form_class = LoginForm


class LogoutView(views.LogoutView):
    next_page = 'accounts:login'


class PasswordResetView(views.PasswordResetView):
    template_name = 'pw_reset/form.html'
    email_template_name = 'pw_reset/email.html'
    success_url = reverse_lazy('accounts:pw_reset_done')
    subject_template_name = 'pw_reset/email_subject.txt'
    form_class = PasswordResetForm

    def post(self, request, *args, **kwargs):
        request.session['reset_email'] = request.POST['email']
        super().post(self, request, *args, **kwargs)

        return HttpResponseRedirect(self.success_url)


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'pw_reset/done.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['reset_email'] = self.request.session.get('reset_email')

        return context_data


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'pw_reset/confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('accounts:pw_reset_complete')


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'pw_reset/complete.html'
