from waffle_hub.hub import Hub

hub = Hub.load(
   name='Laycom_v1.0.0',
   root_dir='/home/ljj/waffle/hubs/laycom'
)
hub.inference(
    source = "/home/ljj/data/Laycom/Kwater_240520.mp4",
    draw=True
)

