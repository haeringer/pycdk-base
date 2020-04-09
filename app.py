#!/usr/bin/env python3

from aws_cdk import core
from pycdk.pycdk_stack import PycdkStack


env = core.Environment(region="eu-central-1")
tags = {'bha':'teststack'}

app = core.App()
PycdkStack(app, "PycdkStack", env=env, tags=tags)

app.synth()
