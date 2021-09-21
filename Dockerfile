FROM python:3-slim AS builder
# FROM python:3 AS builder
ADD . /app
RUN useradd -u 777 appuser && chown -R appuser /app
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
# RUN ls
# RUN git init
# RUN git remote add origin https://github.com/kevteo/test_action.git
# RUN git config --global user.name ai-sdk
# RUN git config --global user.email ai-sdk@users.noreply.github.com
# RUN git add requirements.txt
# RUN git commit -m test999
# RUN git push origin main
