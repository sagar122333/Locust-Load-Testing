MojoAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJhdXRoLmpvdmVvLmNvbSIsImV4cCI6IjIwMjEtMTEtMjlUMDk6" \
                  "NTE6MjUuNzEwWiIsInN1YiI6InNhZ2FyLmd1cHRhK3Rlc3RAam92ZW8uY29tIn0.1r5WSKWwRaCmJVmwqhvpB-kWvfEXw1uGP" \
                  "BiSKaPtiq_8w4PPqi3-tDhPqoU-nCXa4zPrvmx_W8WtjaKGYnlWbw"
MojoAgencyId = "HCLMojoGo"
X_MOJO_USERNAME = "sagar.gupta+test@joveo.com"
client_id = "90590d7e-6d8f-4f2c-b270-366c3041b983"

# MojoAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJhdXRoLXN0YWdpbmcuam92ZW8uY29tIiwiZXhwIjoiMjAyMS0x" \
#                   "MS0yNlQxMTozMzowMi40NDNaIiwic3ViIjoia2dyb3ZvcithZGVjY29Aam92ZW8uY29tIn0.HyGeDsi-XFZJyHvSCMQejCdtR" \
#                   "zbGhDU3RERYRvZEcjyvt3dUpKN5uZZ4QHIaf7keEgUEPu9qL76c3tTkkih-EQ"
# MojoAgencyId = "adecco-france"
# X_MOJO_USERNAME = "kgrovor+adecco@joveo.com"
# client_id = "a0bda522-97d8-4862-ab42-6750849e26de"

start_date = "10/01/2021"
end_date = "10/27/2021"
level_id = "1f1a5d8c-7c19-41ae-a993-17758ac0ba40"
filters = {}
requests = [
    {
        "HTTPMethod": "post",
        "url": "",
        "body": {},
        "headers": {},
        "weight": 1
    }
]

export_command = 'export PATH="/Users/sagargupta/Library/Python/3.9/bin:$PATH"'
lucust_run_command = 'locust -f locustfile_job.py --host=https://mojogo.staging.joveo.com'
