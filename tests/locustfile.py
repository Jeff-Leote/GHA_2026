from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(2, 5)

    @task
    def get_square(self):
        self.client.get("/5")
