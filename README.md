
# CDK Python Test Project

This is a project with a simple Lambda and an API Gateway for Python development with CDK.
The project publishes a most simple HTTP endpoint which can be reached publicly.


### Preparing the environment

Create a virtualenv:

```
$ python3 -m venv .venv
```

Activate the virtualenv:

```
$ source .venv/bin/activate
```

Install the required dependencies:

```
$ pip install -r requirements.txt
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.


### Deploying the CDK Stack

Synthesize the CloudFormation template for the app:

```
$ cdk synth
```

Show the difference between your local environment and the current deployment on AWS:

```
$ cdk diff
```

Deploy the stack to AWS:

```
$ cdk deploy
```

When the deployment is complete, there should be a line at the end of the output showing the URL at which the API Gateway endpoint is published, for example:

```
PycdkStack.PycdkStackEndpoint8024A810 = https://4kwrtw1a2e.execute-api.eu-central-1.amazonaws.com/prod/
```
