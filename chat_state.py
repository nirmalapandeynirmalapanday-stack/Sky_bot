target_groups = {}
current_volume = 1000
current_bass = 5
current_eq = "normal"
authorized_users = set()

def update_volume(vol):
    global current_volume
    current_volume = vol

def update_bass(bass):
    global current_bass
    current_bass = bass

def update_eq(eq):
    global current_eq
    current_eq = eq
