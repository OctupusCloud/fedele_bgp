from django.conf import settings

from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices


_menu_items = (
    PluginMenuItem(
        link='plugins:fedele_bgp:community_list',
        link_text='Communities',
        permissions=['fedele_bgp.view_community'],
        buttons=(
            PluginMenuButton(
                link='plugins:fedele_bgp:community_add',
                title='Communities',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['fedele_bgp.add_community'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:fedele_bgp:bgpsession_list',
        link_text='Sessions',
        permissions=['fedele_bgp.view_bgpsession'],
        buttons=(
            PluginMenuButton(
                link='plugins:fedele_bgp:bgpsession_add',
                title='Sessions',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['fedele_bgp.add_bgpsession'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:fedele_bgp:routingpolicy_list',
        link_text='Routing Policies',
        permissions=['fedele_bgp.view_routingpolicy'],
        buttons=(
            PluginMenuButton(
                link='plugins:fedele_bgp:routingpolicy_add',
                title='Routing Policies',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['fedele_bgp.add_routingpolicy'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:fedele_bgp:prefixlist_list',
        link_text='Prefix Lists',
        permissions=['fedele_bgp.view_prefixlist'],
        buttons=(
            PluginMenuButton(
                link='plugins:fedele_bgp:prefixlist_add',
                title='Prefix Lists',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['fedele_bgp.add_prefixlist'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:fedele_bgp:bgppeergroup_list',
        link_text='Peer Groups',
        permissions=['fedele_bgp.view_bgppeergroup'],
        buttons=(
            PluginMenuButton(
                link='plugins:fedele_bgp:bgppeergroup_add',
                title='Peer Groups',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['fedele_bgp.add_bgppeergroup'],
            ),
        ),
    )
)

plugin_settings = settings.PLUGINS_CONFIG.get('fedele_bgp', {})

if plugin_settings.get('top_level_menu'):
    menu = PluginMenu(  
        label="BGP",
        groups=(("BGP", _menu_items),),
        icon_class="mdi mdi-bootstrap",
    )
else:
    menu_items = _menu_items
