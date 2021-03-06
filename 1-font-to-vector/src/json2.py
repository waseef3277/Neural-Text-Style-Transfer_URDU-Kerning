from __future__ import absolute_import

import ujson


data = [{"font_name": "xb-kayhan-bold.ttf", "font_path": "../../shared-data/fonts/xb-kayhan-bold.ttf", "id": "0"},
        {"font_name": "xb-khoramshahr-bold.ttf", "font_path": "../../shared-data/fonts/xb-khoramshahr-bold.ttf", "id": "1"},
        {"font_name": "xb-niloofar-bold.ttf", "font_path": "../../shared-data/fonts/xb-niloofar-bold.ttf", "id": "2"},
        {"font_name": "xb-riyaz-bold-1.ttf", "font_path": "../../shared-data/fonts/xb-riyaz-bold-1.ttf", "id": "3"},
        {"font_name": "xb-roya-bold-1.ttf", "font_path": "../../shared-data/fonts/xb-roya-bold-1.ttf", "id": "4"},
        {"font_name": "xb-shafigh-bold-1.ttf", "font_path": "../../shared-data/fonts/xb-shafigh-bold-1.ttf", "id": "5"},
        {"font_name": "xb-shafigh-kurd-bold-1.ttf", "font_path": "../../shared-data/fonts/xb-shafigh-kurd-bold-1.ttf", "id": "6"},
        {"font_name": "xb-shiraz-bold-1.ttf", "font_path": "../../shared-data/fonts/xb-shiraz-bold-1.ttf", "id": "7"},
        {"font_name": "xb-sols-bold.ttf", "font_path": "../../shared-data/fonts/xb-sols-bold.ttf", "id": "8"},
        {"font_name": "xb-tabriz-bold-1.ttf", "font_path": "../../shared-data/fonts/xb-tabriz-bold-1.ttf", "id": "9"},
        {"font_name": "xb-titre-regular-1.ttf", "font_path": "../../shared-data/fonts/xb-titre-regular-1.ttf", "id": "10"},
        {"font_name": "xb-yas-bold-1.ttf", "font_path": "../../shared-data/fonts/xb-yas-bold-1.ttf", "id": "11"},
        {"font_name": "xm-traffic-bold-1.ttf", "font_path": "../../shared-data/fonts/xm-traffic-bold-1.ttf", "id": "12"},
        {"font_name": "xm-vahid-bold-1.ttf", "font_path": "../../shared-data/fonts/xm-vahid-bold-1.ttf", "id": "13"}]

with open("../../shared-data/font_infos.json","w") as json_file:
    ujson.dump(data, json_file)
