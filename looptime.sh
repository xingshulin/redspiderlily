#!/usr/bin/env bash

function date2days {
    echo "$*" | awk '{
        z=int((14-$2)/12); y=$1+4800-z; m=$2+12*z-3;
        j=int((153*m+2)/5)+$3+y*365+int(y/4)-int(y/100)+int(y/400)-2472633;
        print j
    }'
}

if [ "$1" = "" ]; then
    echo "Please input server address"
    exit 1
elif [ "$1" = "help" ]; then
    echo "Parameter 1: server address"
    echo "Parameter 2: target mail address"
    exit 1
elif [ "$2" = "" ]; then
    echo "Please input target mail address"
    exit 1
else
    echo "start..."
fi

server=$1
mail=$2

initDate="2016-10-24"
startDays=$(date2days ${initDate:0:4} ${initDate:5:2} ${initDate:8:2})
sysDays=$(date2days `date +"%Y %m %d"`)

let result=sysDays-startDays
let dayGap=$[result%14]
echo "Duration from init date:" ${result}
echo "mod days:" ${dayGap}

_to=`date +%Y-%m-%d`

if [ "$dayGap" = "7" ]; then
    _from=`date -v -7d +%Y-%m-%d`
    cmd="curl http://"${server}"/app/?_from="${_from}"&_to="${_to}"&mail_group="${mail}
    echo ${cmd}
    ${cmd}
elif [ "$dayGap" = "0" ]; then
    _from=`date -v -14d +%Y-%m-%d`
    cmd="curl http://"${server}"/app/?_from="${_from}"&_to="${_to}"&mail_group="${mail}
    echo ${cmd}
    ${cmd}
else
    echo "not fit to mail criteria"
fi