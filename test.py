from core.mapping import Mapping
# from core.clasification import Clasification


PROVIDERS = [
    'clonesyperifericos',
    'mercadolibre',
    'olx'
]

Mapping().get_provider_class(providers=PROVIDERS)

# data = Clasification('Poco f4 gt').get_provider().search('Iphone',options={})
# print(data)



