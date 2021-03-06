From ubuntu:latest
ADD templates /app/templates
RUN apt update
RUN apt install python3 git pip vim -y
RUN git clone https://github.com/lupo218/World-of-games.git /app/git_temp
RUN cp -r /app/git_temp/* /app && rm -R /app/git_temp/*
RUN pip install -r /app/requirements.txt
WORKDIR /app
#CMD python3 MainScores.py
CMD ["python3", "MainScores.py"] #run in background
