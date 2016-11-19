FROM progrium/busybox

# Java config
ENV TRANQUILITY_VERSION   0.8.1
ENV JAVA_HOME       /opt/jre1.8.0_40
ENV PATH            $PATH:/opt/jre1.8.0_40/bin

RUN opkg-install wget tar bash

RUN wget -q --no-check-certificate --no-cookies -O - \
    http://static.druid.io/tranquility/releases/tranquility-distribution-$TRANQUILITY_VERSION.tgz | tar -xzf - -C /opt \
    && ln -s /opt/tranquility-$TRANQUILITY_VERSION /opt/tranquility

COPY conf /opt/tranquility/conf
COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
