source_joined = False
active_targets = {}

def set_source_joined(val):
    global source_joined
    source_joined = val

def add_target(group_id, info):
    active_targets[group_id] = info

def remove_target(group_id):
    active_targets.pop(group_id, None)

def get_targets():
    return active_targets
