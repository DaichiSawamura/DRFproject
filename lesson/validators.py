from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('url_video'):
            if 'youtube.com' not in value.get('url_video'):
                raise ValidationError('Ссылка должна быть с youtube.com')
