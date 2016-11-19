FROM progrium/busybox

# Java config
ENV DRUID_VERSION   0.9.1.1
ENV JAVA_HOME       /opt/jre1.8.0_40
ENV PATH            $PATH:/opt/jre1.8.0_40/bin

ENV DRUID_XMS               '256'
ENV DRUID_XMX               '256'
ENV DRUID_LOGLEVEL          'DEBUG'
ENV DRUID_MAXNEWSIZE        '256'
ENV DRUID_NEWSIZE           '256'

RUN opkg-install wget tar bash \
    && mkdir /tmp/druid

RUN wget -q --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O - \
    http://download.oracle.com/otn-pub/java/jdk/8u40-b26/jre-8u40-linux-x64.tar.gz | tar -xzf - -C /opt 

RUN wget -q --no-check-certificate --no-cookies -O - \ 
    http://static.druid.io/artifacts/releases/druid-$DRUID_VERSION-bin.tar.gz | tar -xzf - -C /opt \
    && ln -s /opt/druid-$DRUID_VERSION /opt/druid

COPY conf /opt/druid-$DRUID_VERSION/conf 
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN mkdir -p /tmp/druid


ENTRYPOINT ["/docker-entrypoint.sh"]
