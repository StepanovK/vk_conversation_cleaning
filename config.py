import os

from conversations import Conversation

token_group = "525ea09babd8d70e3ab77d4898cd31782a6e2e405ed2a8be17f3d838e7ea5eee75705e478cc9eae84c0be"
admin_id = int(os.getenv("vk_admin_id"))
admin_phone = os.getenv("vk_admin_phone")
admin_pass = os.getenv("vk_admin_pass")

new_conv1 = Conversation()
new_conv1.name = 'Пристрой животных'
new_conv1.id = 38814067
new_conv1.group_id = 494898
new_conv1.days_for_cleaning = 30
new_conv1.special_users_settings = {
    325014493: 6,
    242678947: 6,
    19679185: 6,
    52961711: 6,
    313841815: 6,
    162506186: 6,
    26405593: 6,
    544380880: 6,
    332316269: 6,
    361827724: 6,
    148107170: 6,
    471308691: 6,
    3221014: 6,
    22547300: 6,
    169872027: 6,
    12797538: 6
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

conversations = [
    new_conv1,
    new_conv2,
    new_conv3,
    new_conv4,
    new_conv5,
]