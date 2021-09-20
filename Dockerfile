# FROM python:3-slim AS builder
FROM python:3 AS builder
ADD . /app
WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app -r requirements.txt
RUN apt-get update && apt-get install -y git

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
# FROM gcr.io/distroless/python3-debian10
# COPY --from=builder /app /app
# WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/diff.py"]

# RUN git clone https://github.com/kevteo/test_action.git
RUN ls
RUN git add -A
RUN git commit -m "test999"
RUN git push
