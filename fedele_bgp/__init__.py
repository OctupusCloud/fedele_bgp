from extras.plugins import PluginConfig
from .version import __version__


class BGPConfig(PluginConfig):
    name = 'fedele_bgp'
    verbose_name = 'BGP'
    description = 'Subsystem for tracking bgp related objects'
    version = __version__
    author = 'Octupus'
    author_email = 'maxi@octupus.com'
    base_url = 'bgp'
    required_settings = []
    min_version = '3.5.0'
    max_version = '3.6.99'
    default_settings = {
        'device_ext_page': 'right',
        'top_level_menu' : False,
    }


config = BGPConfig # noqa
