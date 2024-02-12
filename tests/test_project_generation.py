from pathlib import Path

from cookiecutter.main import cookiecutter


TEMPLATE_DIRECTORY = str(Path(__file__).parent.parent)


def paths(directory):
    paths = list(Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}


def test_static_and_templates(tmpdir):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(tmpdir),
        no_input=True,
        extra_context={
            "author_name": "John Doe",
            "author_email": "john.doe@mail.com",
            "github_username": "johndoe",
            "project_name": "example_project",
            "project_short_description": "A short description of the project",
            "license": "MIT",
            "python_interpreter": "3.10",
        },
    )
    generated_paths = paths(tmpdir)

    expected_paths = [
        "example_project",
        "example_project/.github",
        "example_project/src/example_project",
        "example_project/tests",
    ]
    for expected_path in expected_paths:
        assert expected_path in generated_paths, f"Expected path {expected_path} is missing."


def test_removing_docs_from_template(tmpdir):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(tmpdir),
        no_input=True,
        extra_context={"project_name": "example_project", "include_docs_folder": "false"},
    )

    generated_paths = paths(tmpdir)

    expected_path = "example_project/docs"

    assert expected_path not in generated_paths, "The docs directory should not be present."
