from setuptools import find_packages, setup

setup(
    name="files-dbt-duckdb",
    version="0.1",
    description="Meltano project files for dbt-duckdb",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/models/.gitkeep",
            "transform/profiles/duckdb/profiles.yml",
            "transform/.gitignore",
            "transform/dbt_project.yml",
        ]
    },
)
