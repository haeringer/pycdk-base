#!/usr/bin/env python3

from aws_cdk import core

from pycdk.pycdk_stack import PycdkStack


app = core.App()
PycdkStack(app, "PycdkStack", env=core.Environment(region="eu-central-1"))

app.synth()
