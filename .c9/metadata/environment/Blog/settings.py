{"filter":false,"title":"settings.py","tooltip":"/Blog/settings.py","undoManager":{"mark":43,"position":43,"stack":[[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":102},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["''"],"id":103}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["s"],"id":104},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["t"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["o"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["r"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["a"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["g"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["e"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":[","],"id":105}],[{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"remove","lines":[","],"id":106}],[{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":[","],"id":107}],[{"start":{"row":126,"column":49},"end":{"row":127,"column":0},"action":"insert","lines":["",""],"id":108},{"start":{"row":127,"column":0},"end":{"row":128,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":128,"column":0},"end":{"row":139,"column":62},"action":"insert","lines":["AWS_S3_OBJECT_PARAMETERS={","    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl':'max-age=946800'","}","","AWS_STORAGE_BUCKET_NAME=\"<s3 bucket name here>\"","AWS_S3_REGION_NAME=\"<region name>\"","AWS_ACCESS_KEY_ID=os.environ[\"AWS_ACCESS_KEY_ID\"]","AWS_SECRET_ACCESS_KEY=os.environ[\"AWS_SECRET_ACCESS_KEY\"]","AWS_S3_CUSTOM_DOMAIN=\"{}.s3.amazonaws.com\".format(AWS_STORAGE_BUCKET_NAME)","","STATICFILES_STORAGE=\"storages.backends.s3boto3.S3Boto3Storage\""],"id":109}],[{"start":{"row":133,"column":25},"end":{"row":133,"column":46},"action":"remove","lines":["<s3 bucket name here>"],"id":110},{"start":{"row":133,"column":25},"end":{"row":133,"column":39},"action":"insert","lines":["kx-test-deploy"]}],[{"start":{"row":134,"column":32},"end":{"row":134,"column":33},"action":"remove","lines":[">"],"id":111},{"start":{"row":134,"column":31},"end":{"row":134,"column":32},"action":"remove","lines":["e"]},{"start":{"row":134,"column":30},"end":{"row":134,"column":31},"action":"remove","lines":["m"]},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["a"]},{"start":{"row":134,"column":28},"end":{"row":134,"column":29},"action":"remove","lines":["n"]},{"start":{"row":134,"column":27},"end":{"row":134,"column":28},"action":"remove","lines":[" "]},{"start":{"row":134,"column":26},"end":{"row":134,"column":27},"action":"remove","lines":["n"]},{"start":{"row":134,"column":25},"end":{"row":134,"column":26},"action":"remove","lines":["o"]},{"start":{"row":134,"column":24},"end":{"row":134,"column":25},"action":"remove","lines":["i"]},{"start":{"row":134,"column":23},"end":{"row":134,"column":24},"action":"remove","lines":["g"]},{"start":{"row":134,"column":22},"end":{"row":134,"column":23},"action":"remove","lines":["e"]},{"start":{"row":134,"column":21},"end":{"row":134,"column":22},"action":"remove","lines":["r"]}],[{"start":{"row":134,"column":20},"end":{"row":134,"column":21},"action":"remove","lines":["<"],"id":112}],[{"start":{"row":134,"column":20},"end":{"row":134,"column":34},"action":"insert","lines":["ap-southeast-1"],"id":113}],[{"start":{"row":139,"column":62},"end":{"row":140,"column":0},"action":"insert","lines":["",""],"id":114},{"start":{"row":140,"column":0},"end":{"row":141,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":141,"column":0},"end":{"row":144,"column":27},"action":"insert","lines":["STATICFILES_LOCATION=\"static\"","DEFAULT_FILE_STORAGE='custom_storages.MediaStorage'","","MEDIAFILES_LOCATION=\"media\""],"id":115}],[{"start":{"row":123,"column":23},"end":{"row":124,"column":0},"action":"insert","lines":["",""],"id":116},{"start":{"row":124,"column":0},"end":{"row":125,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":125,"column":0},"end":{"row":128,"column":1},"action":"insert","lines":["STATICFILES_DIRS = [","    os.path.join(BASE_DIR, \"static\"),","    '/var/www/static/',","]"],"id":117}],[{"start":{"row":127,"column":2},"end":{"row":127,"column":23},"action":"remove","lines":["  '/var/www/static/',"],"id":118},{"start":{"row":127,"column":1},"end":{"row":127,"column":2},"action":"remove","lines":[" "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":1},"action":"remove","lines":[" "]},{"start":{"row":126,"column":37},"end":{"row":127,"column":0},"action":"remove","lines":["",""]},{"start":{"row":126,"column":36},"end":{"row":126,"column":37},"action":"remove","lines":[","]}],[{"start":{"row":143,"column":60},"end":{"row":143,"column":61},"action":"remove","lines":["e"],"id":119},{"start":{"row":143,"column":59},"end":{"row":143,"column":60},"action":"remove","lines":["g"]},{"start":{"row":143,"column":58},"end":{"row":143,"column":59},"action":"remove","lines":["a"]},{"start":{"row":143,"column":57},"end":{"row":143,"column":58},"action":"remove","lines":["r"]},{"start":{"row":143,"column":56},"end":{"row":143,"column":57},"action":"remove","lines":["o"]},{"start":{"row":143,"column":55},"end":{"row":143,"column":56},"action":"remove","lines":["t"]},{"start":{"row":143,"column":54},"end":{"row":143,"column":55},"action":"remove","lines":["S"]},{"start":{"row":143,"column":53},"end":{"row":143,"column":54},"action":"remove","lines":["3"]},{"start":{"row":143,"column":52},"end":{"row":143,"column":53},"action":"remove","lines":["o"]},{"start":{"row":143,"column":51},"end":{"row":143,"column":52},"action":"remove","lines":["t"]},{"start":{"row":143,"column":50},"end":{"row":143,"column":51},"action":"remove","lines":["o"]},{"start":{"row":143,"column":49},"end":{"row":143,"column":50},"action":"remove","lines":["B"]},{"start":{"row":143,"column":48},"end":{"row":143,"column":49},"action":"remove","lines":["3"]},{"start":{"row":143,"column":47},"end":{"row":143,"column":48},"action":"remove","lines":["S"]},{"start":{"row":143,"column":46},"end":{"row":143,"column":47},"action":"remove","lines":["."]},{"start":{"row":143,"column":45},"end":{"row":143,"column":46},"action":"remove","lines":["3"]},{"start":{"row":143,"column":44},"end":{"row":143,"column":45},"action":"remove","lines":["o"]},{"start":{"row":143,"column":43},"end":{"row":143,"column":44},"action":"remove","lines":["t"]},{"start":{"row":143,"column":42},"end":{"row":143,"column":43},"action":"remove","lines":["o"]},{"start":{"row":143,"column":41},"end":{"row":143,"column":42},"action":"remove","lines":["b"]},{"start":{"row":143,"column":40},"end":{"row":143,"column":41},"action":"remove","lines":["3"]},{"start":{"row":143,"column":39},"end":{"row":143,"column":40},"action":"remove","lines":["s"]},{"start":{"row":143,"column":38},"end":{"row":143,"column":39},"action":"remove","lines":["."]},{"start":{"row":143,"column":37},"end":{"row":143,"column":38},"action":"remove","lines":["s"]},{"start":{"row":143,"column":36},"end":{"row":143,"column":37},"action":"remove","lines":["d"]},{"start":{"row":143,"column":35},"end":{"row":143,"column":36},"action":"remove","lines":["n"]},{"start":{"row":143,"column":34},"end":{"row":143,"column":35},"action":"remove","lines":["e"]},{"start":{"row":143,"column":33},"end":{"row":143,"column":34},"action":"remove","lines":["k"]},{"start":{"row":143,"column":32},"end":{"row":143,"column":33},"action":"remove","lines":["c"]},{"start":{"row":143,"column":31},"end":{"row":143,"column":32},"action":"remove","lines":["a"]},{"start":{"row":143,"column":30},"end":{"row":143,"column":31},"action":"remove","lines":["b"]},{"start":{"row":143,"column":29},"end":{"row":143,"column":30},"action":"remove","lines":["."]},{"start":{"row":143,"column":28},"end":{"row":143,"column":29},"action":"remove","lines":["s"]},{"start":{"row":143,"column":27},"end":{"row":143,"column":28},"action":"remove","lines":["e"]},{"start":{"row":143,"column":26},"end":{"row":143,"column":27},"action":"remove","lines":["g"]},{"start":{"row":143,"column":25},"end":{"row":143,"column":26},"action":"remove","lines":["a"]},{"start":{"row":143,"column":24},"end":{"row":143,"column":25},"action":"remove","lines":["r"]}],[{"start":{"row":143,"column":23},"end":{"row":143,"column":24},"action":"remove","lines":["o"],"id":120},{"start":{"row":143,"column":22},"end":{"row":143,"column":23},"action":"remove","lines":["t"]},{"start":{"row":143,"column":21},"end":{"row":143,"column":22},"action":"remove","lines":["s"]}],[{"start":{"row":143,"column":21},"end":{"row":143,"column":22},"action":"insert","lines":["c"],"id":121},{"start":{"row":143,"column":22},"end":{"row":143,"column":23},"action":"insert","lines":["u"]},{"start":{"row":143,"column":23},"end":{"row":143,"column":24},"action":"insert","lines":["s"]},{"start":{"row":143,"column":24},"end":{"row":143,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":143,"column":21},"end":{"row":143,"column":25},"action":"remove","lines":["cust"],"id":122},{"start":{"row":143,"column":21},"end":{"row":143,"column":36},"action":"insert","lines":["custom_storages"]}],[{"start":{"row":143,"column":36},"end":{"row":143,"column":37},"action":"insert","lines":["."],"id":123},{"start":{"row":143,"column":37},"end":{"row":143,"column":38},"action":"insert","lines":["S"]},{"start":{"row":143,"column":38},"end":{"row":143,"column":39},"action":"insert","lines":["t"]},{"start":{"row":143,"column":39},"end":{"row":143,"column":40},"action":"insert","lines":["a"]},{"start":{"row":143,"column":40},"end":{"row":143,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":143,"column":37},"end":{"row":143,"column":41},"action":"remove","lines":["Stat"],"id":124},{"start":{"row":143,"column":37},"end":{"row":143,"column":50},"action":"insert","lines":["StaticStorage"]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["# "],"id":125}],[{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"insert","lines":["#"],"id":126}],[{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"remove","lines":["#"],"id":127}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["# "],"id":128}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"remove","lines":["# "],"id":129}],[{"start":{"row":143,"column":0},"end":{"row":143,"column":2},"action":"insert","lines":["# "],"id":130}],[{"start":{"row":143,"column":0},"end":{"row":143,"column":2},"action":"remove","lines":["# "],"id":131}],[{"start":{"row":125,"column":0},"end":{"row":125,"column":2},"action":"insert","lines":["# "],"id":132},{"start":{"row":126,"column":0},"end":{"row":126,"column":2},"action":"insert","lines":["# "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":125,"column":0},"end":{"row":125,"column":2},"action":"remove","lines":["# "],"id":133},{"start":{"row":126,"column":0},"end":{"row":126,"column":2},"action":"remove","lines":["# "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":39,"column":5},"end":{"row":42,"column":11},"action":"remove","lines":["storages',","    # 'annoying',","    'posts',","    'donate"],"id":134,"ignore":true},{"start":{"row":39,"column":5},"end":{"row":39,"column":10},"action":"insert","lines":["posts"]},{"start":{"row":121,"column":0},"end":{"row":145,"column":27},"action":"remove","lines":["","STATICFILES_DIRS = [","    os.path.join(BASE_DIR, \"static\")","]","","STRIPE_PUBLISHABLE_KEY=os.environ[\"STRIPE_PUBLISHABLE_KEY\"]","STRIPE_SECRET_KEY=os.environ[\"STRIPE_SECRET_KEY\"]","","AWS_S3_OBJECT_PARAMETERS={","    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl':'max-age=946800'","}","","AWS_STORAGE_BUCKET_NAME=\"kx-test-deploy\"","AWS_S3_REGION_NAME=\"ap-southeast-1\"","AWS_ACCESS_KEY_ID=os.environ[\"AWS_ACCESS_KEY_ID\"]","AWS_SECRET_ACCESS_KEY=os.environ[\"AWS_SECRET_ACCESS_KEY\"]","AWS_S3_CUSTOM_DOMAIN=\"{}.s3.amazonaws.com\".format(AWS_STORAGE_BUCKET_NAME)","","STATICFILES_STORAGE=\"custom_storages.StaticStorage\"","","STATICFILES_LOCATION=\"static\"","DEFAULT_FILE_STORAGE='custom_storages.MediaStorage'","","MEDIAFILES_LOCATION=\"media\""]}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":10},"action":"remove","lines":["posts"],"id":135,"ignore":true},{"start":{"row":39,"column":5},"end":{"row":42,"column":11},"action":"insert","lines":["storages',","    # 'annoying',","    'posts',","    'donate"]},{"start":{"row":124,"column":0},"end":{"row":148,"column":27},"action":"insert","lines":["","STATICFILES_DIRS = [","    os.path.join(BASE_DIR, \"static\")","]","","STRIPE_PUBLISHABLE_KEY=os.environ[\"STRIPE_PUBLISHABLE_KEY\"]","STRIPE_SECRET_KEY=os.environ[\"STRIPE_SECRET_KEY\"]","","AWS_S3_OBJECT_PARAMETERS={","    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl':'max-age=946800'","}","","AWS_STORAGE_BUCKET_NAME=\"kx-test-deploy\"","AWS_S3_REGION_NAME=\"ap-southeast-1\"","AWS_ACCESS_KEY_ID=os.environ[\"AWS_ACCESS_KEY_ID\"]","AWS_SECRET_ACCESS_KEY=os.environ[\"AWS_SECRET_ACCESS_KEY\"]","AWS_S3_CUSTOM_DOMAIN=\"{}.s3.amazonaws.com\".format(AWS_STORAGE_BUCKET_NAME)","","STATICFILES_STORAGE=\"custom_storages.StaticStorage\"","","STATICFILES_LOCATION=\"static\"","DEFAULT_FILE_STORAGE='custom_storages.MediaStorage'","","MEDIAFILES_LOCATION=\"media\""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":22},"action":"insert","lines":["import dj_database_url"],"id":136}],[{"start":{"row":79,"column":0},"end":{"row":79,"column":2},"action":"insert","lines":["# "],"id":137},{"start":{"row":80,"column":0},"end":{"row":80,"column":2},"action":"insert","lines":["# "]},{"start":{"row":81,"column":0},"end":{"row":81,"column":2},"action":"insert","lines":["# "]},{"start":{"row":82,"column":0},"end":{"row":82,"column":2},"action":"insert","lines":["# "]},{"start":{"row":83,"column":0},"end":{"row":83,"column":2},"action":"insert","lines":["# "]},{"start":{"row":84,"column":0},"end":{"row":84,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":84,"column":3},"end":{"row":85,"column":0},"action":"insert","lines":["",""],"id":138},{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":86,"column":0},"end":{"row":86,"column":74},"action":"insert","lines":["DATABASES = {'default': dj_database_url.parse(os.environ[\"DATABASE_URL\"])}"],"id":139}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"remove","lines":["*"],"id":141}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":46},"action":"insert","lines":["kx-test-deploy.herokuapp.com"],"id":142}],[{"start":{"row":27,"column":47},"end":{"row":27,"column":48},"action":"insert","lines":[","],"id":143}],[{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"insert","lines":[" "],"id":144}],[{"start":{"row":27,"column":49},"end":{"row":27,"column":51},"action":"insert","lines":["\"\""],"id":145}],[{"start":{"row":27,"column":50},"end":{"row":27,"column":51},"action":"insert","lines":["*"],"id":146}]]},"ace":{"folds":[],"scrolltop":452,"scrollleft":0,"selection":{"start":{"row":27,"column":51},"end":{"row":27,"column":51},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":46,"state":"start","mode":"ace/mode/python"}},"timestamp":1576034936620,"hash":"092f3b2d16df4568b49297443bdf3981316b660d"}