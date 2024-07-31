import octoprint.plugin

class BrowserNotificationsPlugin(octoprint.plugin.StartupPlugin,
                                 octoprint.plugin.TemplatePlugin,
                                 octoprint.plugin.SettingsPlugin,
                                 octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("Browser notifications - Hello world! (more: %s)" % self._settings.get(["url"]))


    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")
    
    def get_template_vars(self):
        return dict(url=self._settings.get(["url"]))

__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = BrowserNotificationsPlugin()

def get_assets(self):
     return dict(
         js=["js/browser_notification.js"]
     )