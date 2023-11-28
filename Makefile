generate-requirements:
	poetry export --without-hashes --format=requirements.txt > docker/requirements.txt
