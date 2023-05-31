from decouple import config

APP_ID = "e_collect"

ELASTIC_APM = {
    "SERVICE_NAME": "e_collect",
    "SERVER_URL": config("ELASTIC_APM_SERVER_URL"),
    "DEBUG": config("DEBUG", default=False, cast=bool),
    "ENVIRONMENT": config("ENVIRONMENT", default="desenvolvimento"),
}