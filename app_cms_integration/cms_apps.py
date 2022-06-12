from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class AppApphook(CMSApp):
    app_name = "app"
    name = "Uoop Application"
    

    def get_urls(self, page=None, language=None, **kwargs):
        return ["app.urls"]