FROM python:3.8-slim as base

RUN apt-get update && apt-get install -y python3-venv

# RUN useradd --create-home appuser
# RUN chmod 777 -R /home/appuser
# WORKDIR /home/appuser
# USER appuser

# Install application into container
RUN mkdir /scripts
WORKDIR /scripts
COPY . .

RUN python3 -m venv myenv
# RUN source myenv/bin/activate
# RUN pip install -r requirements.txt

CMD ["bash"]