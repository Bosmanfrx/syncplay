from syncplay.client import SyncplayClient
from syncplay.ui.ConfigurationGetter import ConfigurationGetter
from syncplay import ui
from syncplay.messages import getMessage

class SyncplayClientManager(object):
    def run(self):
        config = ConfigurationGetter().getConfiguration()
        interface = ui.getUi(graphical=not config["noGui"])
        syncplayClient = SyncplayClient(config["playerClass"], interface, config)
        if(syncplayClient):
            interface.addClient(syncplayClient)
            syncplayClient.start(config['host'], config['port'])
        else:
            interface.showErrorMessage(getMessage("en", "unable-to-start-client-error"))
        
