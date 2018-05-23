from invoke import task


@task
def dist(context):
    context.run("poetry build")


@task
def test(context):
    context.run("poetry run tox")
