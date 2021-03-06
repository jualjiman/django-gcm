from django.conf import settings

GCM_DEVICE_MODEL = getattr(settings, 'GCM_DEVICE_MODEL', 'gcm.models.Device')

GCM_APIKEY = getattr(settings, 'GCM_APIKEY', None)

GCM_MAX_RECIPIENTS = getattr(settings, 'GCM_MAX_RECIPIENTS', 1000)

GCM_API_ENDPOINT = getattr(settings, 'GCM_API_ENDPOINT', "https://fcm.googleapis.com/fcm/send")
