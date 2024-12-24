import nox


@nox.session(python=["3.10"])
def tests(session):
    session.install("pipenv")
    session.run("pipenv", "install")
    session.run("coverage", "run", "-m", "unittest")
    session.run("coverage", "report")


@nox.session
def lint(session):
    session.install("pipenv")
    session.run("pipenv", "install")
    session.run("black", "--check", ".")
    session.run("ruff", ".")


@nox.session
def typing(session):
    session.install("pipenv")
    session.run("pipenv", "install")
    session.run("mypy", ".")
