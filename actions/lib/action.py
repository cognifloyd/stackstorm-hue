from hue import Hue
from st2common.runners.base_action import Action


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.hue = self._get_client()

    def _get_client(self):
        hue = Hue()
        hue.station_ip = self.config['station_ip']
        hue.client_identifier = self.config['client_identifier']
        hue.get_state()

        return hue
