# Relative Location Service Operation Request

curl -X 'POST' \
  'http://localhost:8080/nlmf-newservice/v1/relative-location' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "amfId": "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "gpsi": "gpsi",
  "pei": "pei",
  "radius": "false",
  "supi": "supi"
}'
