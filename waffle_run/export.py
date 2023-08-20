from waffle_hub.hub import Hub

name = "Falldown_v1.0.0"

hub = Hub.load(name=name)

hub.export(device=0, image_size=224)
