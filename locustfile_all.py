import time
from locust import HttpUser, task, between
from constants import MojoAccessToken, MojoAgencyId, X_MOJO_USERNAME, client_id, start_date, end_date, level_id, filters


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # JOBS PAGE
    @task(10)
    def job_api_created_on_validity(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
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
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(20)
    def job_api_created_on_overview(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs/overview?clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(10)
    def job_api_created_on_sponsorship_unpublished(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
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
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(5)
    def job_api_created_on_sponsorship_free(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
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
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(5)
    def job_api_created_on_sponsorship_sponsored(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
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
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(10)
    def job_api_all_jobs(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(10)
    def job_api_goal(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(6)
    def job_api_spent(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(8)
    def job_api_clicks(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(8)
    def job_api_applies(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    @task(5)
    def job_api_cta(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs?page=1&limit=10&clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
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

    # PUBLISHER PAGE
    @task(8)
    def list_publishers(self):
        with self.client.get(
                url="/flash/api/mojogo/publishers?clientId=" + client_id,
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="List Publisher",
                catch_response=True
        ) as response:
            print(response)

    @task(8)
    def publisher_stat(self):
        with self.client.post(
                url="/flash/api/mojogo/publishers?clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": False,
                    "sortBy": "inventory"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Publishers' stat",
                catch_response=True
        ) as response:
            print(response)

    @task(5)
    def inventory(self):
        with self.client.post(
                url="/flash/api/mojogo/publishers/inventory?clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": False,
                    "sortBy": "inventory"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Publishers' stat",
                catch_response=True
        ) as response:
            print(response)

    # CANDIDATE PAGE
    @task(3)
    def application_summary(self):
        with self.client.post(
                url="/flash/api/mojogo/application/summary?page=1&limit=10&clientIds=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": True,
                    "sortBy": "matchScore"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Application Summary",
                catch_response=True
        ) as response:
            print(response)

    @task(3)
    def application(self):
        with self.client.post(
                url="/flash/api/mojogo/application?page=1&limit=10&clientIds=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
                            }
                        ]
                    },
                    "page": 1,
                    "limit": 10,
                    "sortOrderAsc": False,
                    "sortBy": "appliedAt"
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Application",
                catch_response=True
        ) as response:
            print(response)

    @task(5)
    def list_users(self):
        with self.client.get(
                url="/flash/api/mojogo/user?page=1&limit=10&query=&sortOrderAsc=false&activeFilter=all&"
                    "clientId=" + client_id,
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="List Users",
                catch_response=True
        ) as response:
            print(response)

    @task(10)
    def recruiter(self):
        with self.client.post(
                url="/flash/api/mojogo/jobs/recruiters?clientId=" + client_id,
                json={
                    "filters": {
                        "operator": "AND",
                        "rules": [
                            {
                                "operator": "GTE",
                                "field": "startDate",
                                "data": start_date
                            },
                            {
                                "operator": "LTE",
                                "field": "endDate",
                                "data": end_date
                            }
                        ]
                    }
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Recruiters",
                catch_response=True
        ) as response:
            print(response)

    @task(5)
    def get_levels(self):
        with self.client.get(
                url="/flash/api/mojogo/levels?clientId=" + client_id,
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Get Levels",
                catch_response=True
        ) as response:
            print(response)

    @task(10)
    def roles(self):
        with self.client.get(
                url="/flash/api/mojogo/roles?clientId=" + client_id,
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Roles",
                catch_response=True
        ) as response:
            print(response)

    @task(10)
    def level_values(self):
        with self.client.post(
                url="/flash/api/mojogo/levels",
                json={
                    "clientId": client_id,
                    "levelId": level_id,
                    "filters": filters
                },
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Level Values",
                catch_response=True
        ) as response:
            print(response)

    @task(1)
    def job_template(self):
        with self.client.get(
                url="/flash/api/mojogo/job-template?query=&page=1&limit=10&query=&sortOrder=desc&sortBy=createdAt&"
                    "clientIds=" + client_id,
                headers={
                    "MojoAccessToken": MojoAccessToken,
                    "MojoAgencyId": MojoAgencyId,
                    "X-MOJO-USERNAME": X_MOJO_USERNAME,
                    "Content-Type": "application/json"
                },
                name="Job Template",
                catch_response=True
        ) as response:
            print(response)
