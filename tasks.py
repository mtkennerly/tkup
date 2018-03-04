from invoke import task


@task
def dist(context):
    context.run("python setup.py bdist_wheel")


@task
def test(context):
    context.run("tox")
