set -eux

# CITY=Nanjing
# LANGUAGE="zh-CN"
# UNIT=m
# UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"

# curl \
#   -H "Accept-Language: $LANGUAGE" \
#   -H "User-Agent: $UA" \
#   -o result.html \
#   wttr.in/$CITY?format=3\&$UNIT

python weather-emailbot/code.py