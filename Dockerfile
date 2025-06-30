FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy


# setting working directory in container
WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN pip install allure-behave

#copy all files to container
COPY . .

CMD ["python", "run_behave.py"]