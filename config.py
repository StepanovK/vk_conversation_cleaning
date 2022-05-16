import os
from environs import Env

from conversations import Conversation


env = Env()
env.read_env()


token_group = env.str("token_group")
admin_id = int(os.getenv("vk_admin_id"))
admin_phone = os.getenv("vk_admin_phone")
admin_pass = os.getenv("vk_admin_pass")

new_conv1 = Conversation()
new_conv1.name = 'Пристрой животных'
new_conv1.id = 38814067
new_conv1.group_id = 494898
new_conv1.days_for_cleaning = 30
new_conv1.special_users_settings = {
    102636113: 6,
    12797538: 6,
    148107170: 6,
    156852152: 6,
    162506186: 6,
    169872027: 6,
    19679185: 6,
    22547300: 6,
    242678947: 6,
    26405593: 6,
    279518145: 6,
    313841815: 6,
    3221014: 6,
    325014493: 6,
    32560966: 6,
    33132416: 6,
    332316269: 6,
    358628409: 6,
    358678477: 6,
    361827724: 6,
    38487444: 6,
    471308691: 6,
    52961711: 6,
    544380880: 6,
    556442186: 6,
    625059538: 6,
    657899465: 6
}  # Зоошизы

new_conv2 = Conversation()
new_conv2.name = 'Детская барахолка'
new_conv2.id = 39867020
new_conv2.group_id = 494898
new_conv2.days_for_cleaning = 60
new_conv2.special_comments_settings = {
    1852: 0  # Сашина реклама
}

new_conv3 = Conversation()
new_conv3.name = 'Шмотки'
new_conv3.id = 39960811
new_conv3.group_id = 494898
new_conv3.days_for_cleaning = 30

new_conv4 = Conversation()
new_conv4.name = 'Мебель'
new_conv4.id = 39960829
new_conv4.group_id = 494898
new_conv4.days_for_cleaning = 30

new_conv5 = Conversation()
new_conv5.name = 'Недвижимость'
new_conv5.id = 38947818
new_conv5.group_id = 494898
new_conv5.days_for_cleaning = 60

new_conv6 = Conversation()
new_conv6.name = 'Реклама'
new_conv6.id = 30606622
new_conv6.group_id = 494898
new_conv6.days_for_cleaning = 60

conversations = [
    new_conv1,
    new_conv2,
    new_conv3,
    new_conv4,
    new_conv5,
    new_conv6,
]
