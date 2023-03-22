## plugin-google-cloud-log-mon-datasource

![Google Cloud Services](https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/cloud_logging.png)

**Plugin to collect log data of Google Cloud logging**

>Cloudforet's [plugin-google-cloud-log-mon-datasource](https://github.com/cloudforet-io/plugin-google-cloud-log-mon-datasource)
is a convenient tool
> to get Cloud Logging log data from Google.


Find us also at [Dockerhub](https://hub.docker.com/repository/docker/spaceone/plugin-google-cloud-log-mon-datasource)
> Latest stable version : 1.0.1

Please contact us if you need any further information. (<support@spaceone.dev>)

---

<br>
<br>

## Google Service Endpoint (in use)

There is an endpoints used to collect resources information of GCP.  
Endpoint of served GCP is a URL consisting of a service code.

```text
https://[service-code].googleapis.com
```

<br>
<br>

## Authorization Scopes

Requires one of the following OAuth scopes:

```text
https://www.googleapis.com/auth/logging.read
https://www.googleapis.com/auth/logging.admin
https://www.googleapis.com/auth/cloud-platform.read-only
https://www.googleapis.com/auth/cloud-platform
```

<br>
<br>

## Authentication Overview

Registered service account on SpaceONE must have certain permissions to collect cloud service data  
Please, set authentication privilege for followings:

```text
logging.logEntries.list
logging.privateLogEntries.list
logging.views.access
```