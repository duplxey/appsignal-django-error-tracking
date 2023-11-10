from appsignal import Appsignal

appsignal = Appsignal(
    active=True,
    name='django-error-tracking',
    # Please do not commit this key to your source control management system.
    # Move this to your app's security credentials or environment variables.
    # https://docs.appsignal.com/python/configuration/options.html#option-push_api_key
    push_api_key='509632e6-d67f-4545-a107-7065419a7802',
)
