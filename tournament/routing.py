from channels.routing import route


channel_routing = [
    route('websocket.recieve', 'tournament.views.ws_receive')
]