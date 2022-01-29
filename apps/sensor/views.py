import base64
from datetime import date, timedelta
from io import BytesIO
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import matplotlib.pyplot as plt
from apps.sensor.models import Measurement


class DashBoardView(LoginRequiredMixin, TemplateView):

    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        today = date.today()
        context = super().get_context_data(**kwargs)
        obj = Measurement.objects.filter(type=Measurement.Type.HUMIDITY, created_at__gte=today - timedelta(1))
        x_list = [created_at.strftime('%m/%d %H:%M') for created_at in obj.values_list('created_at', flat=True)]
        graph = self._create_graph(x_list, obj.values_list('value', flat=True))
        context['graph'] = graph

        return context

    def _create_graph(self, x, y):
        plt.switch_backend("AGG")
        plt.figure(figsize=(10, 5))
        plt.xticks(rotation=30)
        plt.bar(x, y)
        plt.title('Humidity Graph')
        plt.ylabel('Humidity(%)')
        plt.tight_layout()
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        img = buffer.getvalue()
        graph = base64.b64encode(img)
        graph = graph.decode("utf-8")
        buffer.close()

        return graph
