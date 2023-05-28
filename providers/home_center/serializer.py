# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.home_center.settings import *


class HomeCenterSerializer(BaseSerializer):
    query_dataset = '<data:results/>'
    class model(BaseProductModel):
        name = '"<displayName/>"'
        origin = f'"{BASE_URL}" + "<productId/>"'
        preview = f'"{MEDIA_URL}" + "<productId/>"'
        actual_price = f'float("<prices:0:priceWithoutFormatting/>")'
        provider_icon = f'"{PROVIDER_ICON}"'
