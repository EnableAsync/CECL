FROM python:3.7
COPY . /CECL
COPY rootfs /
WORKDIR /CECL
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple -r /CECL/server/requirements.txt
ENV PATH=$PATH:/CECL
ENV PYTHONPATH /CECL
EXPOSE 5000 50051 50052 50053 50054 50055 50056
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "/CECL/server/main.py"]