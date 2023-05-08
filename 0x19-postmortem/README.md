Issue Summary:
On May 5th, 2023, at 2:00 PM EST, the Nginx server hosting our company's website experienced an outage that lasted for 2 hours. During this time, users were unable to access the website, resulting in a 100% outage rate.

Root Cause:
The root cause of the outage was a configuration issue in the Nginx server that caused it to crash when handling a sudden spike in traffic. This was due to an incorrect setting in the server configuration file that was not caught during the testing phase.

Timeline:

2:00 PM: The issue was first detected by our monitoring system, which alerted our team of the server's unresponsiveness.
2:05 PM: An engineer noticed the issue and attempted to restart the Nginx server, but it failed to start.
2:10 PM: The team investigated the server logs and found no indication of any hardware or network failure.
2:20 PM: Assumptions were made that the issue was related to the server configuration and the team began investigating.
3:00 PM: The team discovered the incorrect configuration setting, which was quickly fixed.
3:15 PM: The server was restarted, and the website was once again accessible to users.
Misleading Investigation/Debugging Paths:
During the investigation, the team initially focused on hardware and network issues, as these were common causes of server outages. This led to some time being wasted on checking hardware logs and network connectivity, which ultimately had no relevance to the root cause of the issue.

Escalation:
The incident was initially escalated to the server team responsible for managing the Nginx server. When the issue was found to be related to the configuration file, it was escalated to the development team responsible for website deployment and configuration management.

Resolution:
The incorrect configuration setting was found and corrected, allowing the Nginx server to be restarted and the website to become accessible again.

Corrective and Preventative Measures:
To prevent similar issues from occurring in the future, the following measures will be taken:

Implement better testing procedures for server configuration changes to catch issues before they become live.
Improve the monitoring system to provide more detailed alerts that can help diagnose issues more quickly.
Develop a more robust failover system to ensure that website access can be maintained in the event of a server outage.
In conclusion, the Nginx server outage on May 5th, 2023, was caused by a configuration issue that led to a sudden spike in traffic, resulting in the server crashing. The issue was quickly resolved, but measures will be taken to prevent similar issues from occurring in the future.
