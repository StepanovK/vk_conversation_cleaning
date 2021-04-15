import time


class Conversation:
    id: int
    name: str
    group_id: int
    days_for_cleaning: int
    special_users_settings: dict
    special_comments_settings: dict

    def __init__(self):
        self.special_users_settings = {}
        self.special_comments_settings = {}
        self.days_for_cleaning = 0
        self.id = 0
        self.name = ''
        self.group_id = ''

    def __repr__(self):
        link = self.get_link()
        return f"{self.name} ({link})"

    def get_link(self):
        return f"https://vk.com/topic-{self.group_id}_{self.id}"

