# Request Ciphering Key Data Service Operation Request

curl -X 'POST' \
  'http://localhost:8080/nlmf-broadcast/v1/cipher-key-data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "amfCallBackURI": "amfCallBackURI",
  "supportedFeatures": "1"
}'
