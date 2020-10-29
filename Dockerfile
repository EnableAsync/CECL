FROM python:3.7
COPY ./ /CECL
WORKDIR /CECL
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple -r /CECL/server/requirements.txt
ENV PATH=$PATH:/CECL
ENV PYTHONPATH /CECL
EXPOSE 5000/tcp
CMD ["python", "/CECL/server/main.py"]