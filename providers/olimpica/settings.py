

PROVIDER_URL = 'https://master--olimpica.myvtex.com/_v/private/graphql/v1?workspace=master'
ORIGIN_URL = 'https://www.olimpica.com/'

BODY = r'''{
  "operationName": "PRODUCT_QUERY_NEW",
  "variables": {
    "query": "query_keyboard",
    "to": 9,
    "from": 0,
    "collection": ""
  },
  "query": "query PRODUCT_QUERY_NEW($query: String = \"\", $priceRange: String = \"0 TO 10000000000\", $orderBy: String = \"\", $to: Int = 9, $from: Int = 0, $category: String = \"\", $collection: String = \"\") {\n  products(\n    from: $from\n    query: $query\n    priceRange: $priceRange\n    orderBy: $orderBy\n    to: $to\n    category: $category\n    collection: $collection\n    hideUnavailableItems: true\n  ) @context(provider: \"vtex.search-graphql\") {\n    productId\n    productName\n    brand\n    categoryId\n    productClusters {\n      id\n      name\n      __typename\n    }\n    properties {\n      name\n      values\n      __typename\n    }\n    skuSpecifications {\n      field {\n        name\n        originalName\n        __typename\n      }\n      values {\n        name\n        originalName\n        __typename\n      }\n      __typename\n    }\n    priceRange {\n      sellingPrice {\n        highPrice\n        lowPrice\n        __typename\n      }\n      listPrice {\n        highPrice\n        lowPrice\n        __typename\n      }\n      __typename\n    }\n    items {\n      itemId\n      images {\n        imageUrl\n        __typename\n      }\n      sellers {\n        sellerId\n        commertialOffer {\n          AvailableQuantity\n          Price\n          ListPrice\n          PriceWithoutDiscount\n          teasers {\n            name\n            conditions {\n              minimumQuantity\n              parameters {\n                name\n                value\n                __typename\n              }\n              __typename\n            }\n            effects {\n              parameters {\n                name\n                value\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}'''


PAYLOAD_BIR = 'providers/olimpica/payload'


