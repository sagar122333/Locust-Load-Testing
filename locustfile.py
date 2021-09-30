import time
from locust import HttpUser, task, between
from constants import MojoAccessToken, MojoAgencyId, X_MOJO_USERNAME


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def log_in(self):
        with self.client.get(
                url="/api/mojogo/loginv2",
                headers={
                    "Authorization": "Basic a2dyb3ZvcithZGVjY29Aam92ZW8uY29tOmpvdmVvMTUyMA=="
                },
                name="log_in"
        ) as response:
            print(response)

    @task
    def job_api_created_on_validity(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "EQUAL",
                                "field": "VALIDITY",
                                "data": True
                            },
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "createdOn"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_created_on_validity",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_created_on_overview(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs/overview?clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "createdOn"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_created_on_overview",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_created_on_sponsorship_unpublished(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "EQUAL",
                                "field": "SPONSORSHIP",
                                "data": "UNPUBLISHED"
                            },
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "createdOn"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_created_on_sponsorship_unpublished",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_created_on_sponsorship_free(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "EQUAL",
                                "field": "SPONSORSHIP",
                                "data": "FREE"
                            },
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "createdOn"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_created_on_sponsorship_free",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_created_on_sponsorship_sponsored(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "EQUAL",
                                "field": "SPONSORSHIP",
                                "data": "SPONSORED"
                            },
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "createdOn"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_created_on_sponsorship_sponsored",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_all_jobs(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "createdOn"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_all_jobs",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_goal(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": False,
                    "sortBy": "goal"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_goal",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_spent(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "spent"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_spent",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_clicks(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "clicks"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_clicks",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_applies(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "applies"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_applies",
                catch_response=True
        ) as response:
            print(response)

    @task
    def job_api_cta(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=a0bda522-97d8-4862-ab42-6750849e26de",
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": "09/01/2021"
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": "09/29/2021"
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "CTA"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="job_api_cta",
                catch_response=True
        ) as response:
            print(response)
