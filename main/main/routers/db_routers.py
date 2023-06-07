from django.conf import settings

class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.model_name, None)

    def db_for_write(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.model_name, None)

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        return None

    def allow_migrate(db, model): 
        return None

    def allow_migrate(db, app_label, model_name=None, **hints): 
        return None