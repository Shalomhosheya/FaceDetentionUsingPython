import screen_brightness_control as sbc

try:
    print(sbc.get_brightness(method='vcp'))  # Try 'vcp' method
except Exception as e:
    print(f"Error using 'vcp' method: {e}")

try:
    print(sbc.get_brightness(method='windows'))  # Try 'windows' method
except Exception as e:
    print(f"Error using 'windows' method: {e}")
