# Cancel Location Service Operation Request

curl -X 'POST' \
  'http://localhost:8080/nlmf-loc/v1/cancel-location' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "hgmlcCallBackURI": "hgmlcCallBackURI",
  "ldrReference": "ldrReference",
  "supportedFeatures": "1"
}'
