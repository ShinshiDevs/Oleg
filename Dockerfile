# MIT License
#
# Copyright (c) 2023-Present "Shinshi Developers Team"
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# Specify the required Python version.
ARG PYTHON_IMAGE=python:3.12-alpine
FROM ${PYTHON_IMAGE}
# Required dependencies for compiling project's packages
RUN apk --no-cache add gcc libffi-dev musl-dev
# Create the working directory.
WORKDIR /usr/Oleg/
# Project files copy
COPY . .
# Install the project's dependencies.
RUN pip install --no-cache-dir --quiet -U poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --quiet --no-interaction --no-root --no-dev
# Start
STOPSIGNAL SIGINT
ENV OLEG_PYTHON_EXECUTABLE=python3.12
ENTRYPOINT ["/bin/sh", "-c", "poetry run ${OLEG_PYTHON_EXECUTABLE} -OOm oleg"]
