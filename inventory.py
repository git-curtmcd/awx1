#!/usr/bin/env python3
import json
import os

tf_state = json.load(open(os.environ['TF_STATE_PATH']))
print(json.dumps({
    "_meta": {"hostvars": {}},
    "new_vms": {
        "hosts": [vm["attributes"]["default_ipv4_address"] for vm in tf_state["resources"]]
    }
}))