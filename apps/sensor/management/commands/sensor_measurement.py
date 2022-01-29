from django.core.management.base import BaseCommand
import cgsensor
from apps.sensor.models import Measurement


class Command(BaseCommand):

    def handle(self, *args, **options):
        bme280 = cgsensor.BME280(i2c_addr=0x77)
        bme280.forced()
        Measurement.objects.create(Type=Measurement.Type.TEMPERATURE, value=bme280.temperature)
        Measurement.objects.create(Type=Measurement.Type.HUMIDITY, value=bme280.humidity)
        Measurement.objects.create(Type=Measurement.Type.PRESSURE, value=bme280.pressure)
