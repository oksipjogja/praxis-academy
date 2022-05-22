#  example $jsonSchema

{
  "$jsonSchema": {
    "bsonType": 'object',
    "required": [
      'properties.Name',
      'properties.Country',
      'geometry.type',
      'geometry.coordinates'
    ],
    "properties": {
      "Country": {
        "bsonType": 'string',
        "description": 'Must be supplied'
      },
      "Name": {
        "bsonType": 'string',
        "description": 'Must be supplied'
      },
      "description": {
        "bsonType": 'string',
        "description": 'Optional description'
      },
      "geometry": {
        "type": 'object',
        "properties": {
          "type": {
            'enum': [
              'Point'
            ],
            "description": 'Must be Point'
          },
          "coordinates": {
            "bsonType": [
              'object'
            ],
            "description": 'Contains Longitude, Latitude',
            "properties": {
              "longitude": {
                "type": 'number',
                "description": 'Decimal representation of longitude'
              },
              "latitude": {
                "type": 'number',
                "description": 'Decimal representation of latitude'
              }
            }
          }
        }
      },
      "datePosted": {
        "bsonType": 'date',
        "description": 'Auto-added field'
      },
      "image": {
        "bsonType": 'string',
        "description": 'URL of image location'
      }
    }
  }
}