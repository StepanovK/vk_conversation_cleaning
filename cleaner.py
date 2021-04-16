import vk_api
import config
import datetime


def clean():
    vk = vk_api.VkApi(config.admin_phone, config.admin_pass)
    vk.auth()
    vk = vk.get_api()

    time_now = datetime.datetime.today()
    all_boards = vk.board
    for conv in config.conversations:
        comments = all_boards.getComments(group_id=conv.group_id, topic_id=conv.id)

        for comment in comments.get('items'):
            from_id = comment.get('from_id')
            comment_id = comment.get('id')
            comment_link = "{}?post={}".format(conv.get_link(), comment_id)
            if isinstance(from_id, str) and (from_id.startswith('_') or from_id.startswith('-')):
                # print("{}:\nПропущен коммент {}".format(conv.name, comment_link))
                continue
            elif isinstance(from_id, int) and from_id <= 0:
                # print("{}:\nПропущен коммент {}".format(conv.name, comment_link))
                continue

            days_for_cleaning = conv.days_for_cleaning

            users_set = conv.special_users_settings.get(from_id)
            if users_set is not None:
                days_for_cleaning = users_set
                # print("Коммент от {} особый {}".format(from_id, comment_link))

            if days_for_cleaning == 0:
                continue

            comment_set = conv.special_comments_settings.get(comment_id)
            if comment_set is not None:
                days_for_cleaning = comment_set
                # print("Коммент от {} особый {}".format(from_id, comment_link))

            if days_for_cleaning == 0:
                continue

            date_of_comment = datetime.datetime.utcfromtimestamp(comment.get('date'))
            days_from_comment = (time_now - date_of_comment).days

            if days_from_comment > days_for_cleaning:
                result = all_boards.deleteComment(group_id=conv.group_id, topic_id=conv.id, comment_id=comment_id)
                if result == 1:
                    print("Коммент от {} удалён {}".format(date_of_comment, comment_link))
                else:
                    print("При удалении коммента {} возникла ошибка с кодом: {}".format(comment_link, result))


if __name__ == '__main__':
    clean()
