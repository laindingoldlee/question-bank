"""Print the file list for publishing site/ as the Claude artifact
(publish_files takes [{"as": served path, "path": local path}])."""
import json, os
from qbcommon import ROOT
site = os.path.join(ROOT, "site")
fs = ["index.html", "data/index.json", "data/base_state.json"] + \
     [f"data/text/t{h}.json" for h in "0123456789abcdef"] + [f"data/svg/s{k:02x}.json" for k in range(64)]
print(json.dumps([{"as": f, "path": os.path.join(site, f)} for f in fs]))
