import requests

class kanban_manager:
    def __init__(self, auth, subdomain):
        self.session = requests.session()
        self.session.headers.update({
            'Authorization': 'Bearer {}'.format(auth)
            })
        self.subdomain = subdomain
    def get_user_info(self):
        r = self.session.get('https://{}.kanbantool.com/api/v3/users/current.json'.format(self.subdomain))
        return r
    def get_board_info(self, board_id):
        r = self.session.get('https://{}.kanbantool.com/api/v3/boards/{}/preload.json'.format(self.subdomain, board_id))
        return r
    def get_board_tasks(self, board_id):
        r = self.session.get('https://{}.kanbantool.com/api/v3/boards/{}.json'.format(self.subdomain, board_id))
        return r
    def create_task(self, payload):
        r = self.session.post('https://{}.kanbantool.com/api/v3/tasks.json'.format(self.subdomain), json=payload)
        return r
    def delete_task(self, task_id):
        r = self.session.patch('https://{}.kanbantool.com/api/v3/tasks/{}.json'.format(self.subdomain, task_id), json={'_action':'delete'})
        return r
    def update_task(self, task_id, payload):
        r = self.session.patch('https://{}.kanbantool.com/api/v3/tasks/{}.json'.format(self.subdomain, task_id), json=payload)
        return r