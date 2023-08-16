from waffle_hub.hub import Hub

name = "PeopleDet_v1.2.0"

hub = Hub.load(name=name)

hub.export(device=0)
