

import json
from consumers.testing import TestConsumer

result = TestConsumer().search(
    keyboard='iphone 13',
    options={
        'is_descount':False,
        'is_free_shipping':False,
        'range':'',
        'score':None
    }
)

print(json.dumps(result,indent=2))


