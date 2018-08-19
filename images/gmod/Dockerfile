FROM steamcmd

USER root


USER steam
WORKDIR /steam/steamcmd_linux
RUN mkdir -p /steam/gmodds

RUN ./steamcmd.sh +login anonymous +force_install_dir ../gmodds +app_update 4020 validate +quit

ADD start.sh /steam/gmodds/

WORKDIR /steam/gmodds

CMD ["./start.sh"]